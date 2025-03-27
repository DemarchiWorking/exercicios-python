import socket
import dns.resolver
import whois
import subprocess
import nmap
from scapy.all import traceroute
from datetime import datetime

def escrever_no_arquivo(arquivo, texto, secao):
    with open(arquivo, 'a') as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"Seção: {secao} - {datetime.now()}\n")
        f.write(f"{'='*50}\n")
        f.write(f"{texto}\n")

def coletar_informacoes(alvo, arquivo_saida="resultado_analise.txt"):
    with open(arquivo_saida, 'w') as f:
        f.write(f"analise do alvo: {alvo}\n")
        f.write(f"inicio: {datetime.now()}\n")

    try:
        ip = socket.gethostbyname(alvo)
        resultado = f"IP de {alvo}: {ip}"
        escrever_no_arquivo(arquivo_saida, resultado, "Consulta de IP socket")
    except Exception as e:
        escrever_no_arquivo(arquivo_saida, f"Erro: {e}", "Consulta de IP socket")

    try:
        respostas_a = dns.resolver.resolve(alvo, 'A')
        respostas_mx = dns.resolver.resolve(alvo, 'MX')
        respostas_ns = dns.resolver.resolve(alvo, 'NS')
        resultado = "Registros A:\n"
        for ip in respostas_a:
            resultado += f"  IP: {ip}\n"
        resultado += "Registros MX:\n"
        for mx in respostas_mx:
            resultado += f"  MX: {mx}\n"
        resultado += "Registros NS:\n"
        for ns in respostas_ns:
            resultado += f"  NS: {ns}\n"
        escrever_no_arquivo(arquivo_saida, resultado, "Consulta DNS (dnspython)")
    except Exception as e:
        escrever_no_arquivo(arquivo_saida, f"Erro: {e}", "Consulta DNS (dnspython)")

    try:
        w = whois.whois(alvo)
        resultado = f"Domínio: {w.domain_name}\n"
        resultado += f"Servidores de nomes: {w.name_servers}\n"
        resultado += f"Data de criação: {w.creation_date}\n"
        resultado += f"Data de expiração: {w.expiration_date}\n"
        resultado += f"Registrador: {w.registrar}\n"
        escrever_no_arquivo(arquivo_saida, resultado, "Consulta WHOIS")
    except Exception as e:
        escrever_no_arquivo(arquivo_saida, f"Erro: {e}", "Consulta WHOIS")

    try:
        resultado = subprocess.run(['ping', '-c', '4', alvo], capture_output=True, text=True)
        escrever_no_arquivo(arquivo_saida, resultado.stdout, "Ping (subprocess)")
    except Exception as e:
        escrever_no_arquivo(arquivo_saida, f"Erro: {e}", "Ping (subprocess)")

    try:
        nm = nmap.PortScanner()
        nm.scan(alvo, '1-100')
        resultado = ""
        for host in nm.all_hosts():
            resultado += f"Host: {host}\n"
            resultado += f"Estado: {nm[host].state()}\n"
            for proto in nm[host].all_protocols():
                portas = nm[host][proto].keys()
                resultado += f"Protocolo: {proto}\n"
                for porta in portas:
                    resultado += f"  Porta {porta}: {nm[host][proto][porta]['state']}\n"
        escrever_no_arquivo(arquivo_saida, resultado, "Escaneamento de Portas (nmap)")
    except Exception as e:
        escrever_no_arquivo(arquivo_saida, f"Erro: {e}", "Escaneamento de Portas (nmap)")

    try:
        resultado, _ = traceroute(alvo, maxttl=20)
        texto = str(resultado)
        escrever_no_arquivo(arquivo_saida, texto, "Traceroute (scapy)")
    except Exception as e:
        escrever_no_arquivo(arquivo_saida, f"Erro: {e}", "Traceroute (scapy)")

    with open(arquivo_saida, 'a') as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"Fim da análise: {datetime.now()}\n")

if __name__ == "__main__":
    alvo = input("Digite o alvo a ser analisado: ")
    coletar_informacoes(alvo)
    print(f"analise concluida! Resultados salvos 'resultado_analise.txt'")