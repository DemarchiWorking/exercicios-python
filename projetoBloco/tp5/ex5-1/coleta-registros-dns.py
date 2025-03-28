import dns.resolver
from typing import List, Dict


def consultar_registros_dns_completos(dominio: str) -> dict:
    registros = {
        "A": [], "AAAA": [], "MX": [], "NS": [],
        "SOA": [], "TXT": [], "CNAME": []
    }
    tipos_registros = list(registros.keys())  # Gera a lista de tipos suportados
    resolvedor = dns.resolver.Resolver()

    for tipo in tipos_registros:
        try:
            respostas = resolvedor.resolve(dominio, tipo)
            registros[tipo] = [str(dado) for dado in respostas]
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.exception.DNSException):
            registros[tipo] = []

    return registros


def consultar_servidores_autoritativos(dominio: str) -> List[str]:
    try:
        respostas = dns.resolver.resolve(dominio, "NS")
        return [str(ns) for ns in respostas]
    except dns.exception.DNSException:
        return []


def exibir_resultados_completos(registros: Dict[str, List[str]], servidores_ns: List[str]):
    print("\nresultados da consulta dns:")
    for tipo, valores in registros.items():
        print(f"registros {tipo}:")
        if valores:
            for valor in valores:
                print(f"  - {valor}")
        else:
            print(" nenhum registro encontrado.")

    print("\nservidores dns autoritativos:")
    if servidores_ns:
        for servidor in servidores_ns:
            print(f"  - {servidor}")
    else:
        print("nenhum servidor ns encontrado.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("python3 coleta-info.py <dominio>")
        sys.exit(1)

    dominio = sys.argv[1]

    print(f"consultando dns para o dominio: {dominio}...")
    registros_dns = consultar_registros_dns_completos(dominio)
    servidores_autoritativos = consultar_servidores_autoritativos(dominio)

    exibir_resultados_completos(registros_dns, servidores_autoritativos)
