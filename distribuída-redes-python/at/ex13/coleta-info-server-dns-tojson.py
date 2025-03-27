import dns.resolver
import dns.query
import dns.zone
import dns.reversename
import dns.rdatatype
import dns.exception
import subprocess
import json
import sys
from typing import List, Set, Dict


def consultar_registros_dns(dominio: str, tipos_registros: List[str], servidor_dns: str = None) -> dict:
    resultados = {}
    resolvedor = dns.resolver.Resolver()

    if servidor_dns:
        resolvedor.nameservers = [servidor_dns]

    for tipo in tipos_registros:
        try:
            respostas = resolvedor.resolve(dominio, tipo)
            resultados[tipo] = [str(dado) for dado in respostas]
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.exception.DNSException):
            resultados[tipo] = []
    return resultados

def consultar_registros_adicionais(dominio: str) -> Dict[str, List[str]]:
    registros_adicionais = {}

    try:
        registros_caa = dns.resolver.resolve(dominio, "CAA")
        registros_adicionais["CAA"] = [str(dado) for dado in registros_caa]
    except dns.exception.DNSException:
        registros_adicionais["CAA"] = []

    try:
        registros_rrsig = dns.resolver.resolve(dominio, "RRSIG")
        registros_adicionais["RRSIG"] = [str(dado) for dado in registros_rrsig]
    except dns.exception.DNSException:
        registros_adicionais["RRSIG"] = []

    try:
        registros_srv = dns.resolver.resolve(f"_sip._tcp.{dominio}", "SRV")
        registros_adicionais["SRV"] = [str(dado) for dado in registros_srv]
    except dns.exception.DNSException:
        registros_adicionais["SRV"] = []

    return registros_adicionais


def consulta_reversa(ip: str) -> List[str]:
    try:
        nome_reverso = dns.reversename.from_address(ip)
        respostas = dns.resolver.resolve(nome_reverso, "PTR")
        return [str(dado) for dado in respostas]
    except dns.exception.DNSException:
        return []

def tentar_transferencia_zona(dominio: str, servidor_dns: str) -> Set[str]:
    registros = set()
    try:
        print(f"tentando transfzona com o servidor {servidor_dns}...")
        zona = dns.zone.from_xfr(dns.query.xfr(servidor_dns, dominio))
        if zona:
            for nome, dado in zona.iterate_rdatas():
                registros.add(f"{nome} {dado}")
        else:
            print(f"transferencia falhou: nenhuma informação retornada.")
    except dns.exception.FormError:
        print(f"transferencia falhou: formato invalido {dominio}.")
    except dns.query.TransferError:
        print(f"transferencia falhou: servidor {servidor_dns} não permitiu a operação.")
    except ConnectionResetError:
        print(f"transferencia falhou: conexao com o servidor {servidor_dns} foi recusada.")
    except Exception as e:
        print(f"ERRO: durante a transferência de zona: {e}")
    return registros


def executar_dnsrecon(dominio: str, opcoes: List[str] = ["-t", "std"]) -> dict:
    comando = ["dnsrecon", "-d", dominio] + opcoes
    try:
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        return {"saida": resultado.stdout, "erro": resultado.stderr}
    except subprocess.CalledProcessError as e:
        return {"saida": e.stdout, "erro": e.stderr}

def exportar_para_json(nome_arquivo: str, dados: dict):
    """
    Exporta os resultados para um arquivo JSON
    """
    with open(nome_arquivo, "w") as arquivo_json:
        json.dump(dados, arquivo_json, indent=2, ensure_ascii=False)
    print(f"\nResultados exportados para o arquivo: {nome_arquivo}")

def principal(dominio: str, servidor_dns: str = None):
    tipos_registros = ["A", "AAAA", "MX", "NS", "SOA", "TXT", "CNAME"]

    resultados_completos = {}

    print(f"\nconsultando registros de DNS para o dominio {dominio}")
    registros_basicos = consultar_registros_dns(dominio, tipos_registros, servidor_dns)
    resultados_completos["Registros Básicos"] = registros_basicos

    print(f"\nconsultando registros adicionais  {dominio}")
    registros_adicionais = consultar_registros_adicionais(dominio)
    resultados_completos["Registros Adicionais"] = registros_adicionais

    if servidor_dns:
        print(f"\ntentando transferencia de zona no domínio {dominio} usando o servidor {servidor_dns}")
        registros_zona = tentar_transferencia_zona(dominio, servidor_dns)
        resultados_completos["Transferência de Zona"] = list(registros_zona)

    print(f"\nexecutando DNSRecon (padrão) para o dominio {dominio}...")
    resultado_std = executar_dnsrecon(dominio)
    resultados_completos["DNSRecon - Padrão"] = resultado_std

    print(f"\n3executando DNSRecon (brute) para o dominio {dominio}...")
    resultado_brute = executar_dnsrecon(dominio, ["-t", "brute", "-D", "/usr/share/dnsrecon/namelist.txt"])
    resultados_completos["DNSRecon - Força Bruta"] = resultado_brute

    print(f"\nexecutando DNSRecon para buscar registros SRV no dominio {dominio}...")
    resultado_srv = executar_dnsrecon(dominio, ["-t", "srv"])
    resultados_completos["DNSRecon - SRV"] = resultado_srv

    exportar_para_json("resultados_dns.json", resultados_completos)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("parametros: python3 coleta-info.py <dominio> [servidor_dns]")
        sys.exit(1)

    dominio = sys.argv[1]
    servidor_dns = sys.argv[2] if len(sys.argv) > 2 else None
    principal(dominio, servidor_dns)
