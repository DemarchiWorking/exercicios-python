from scapy.all import *
import requests
import random
import string
import json
from datetime import datetime
import re
import threading
import queue
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

pacote_queue = queue.Queue()


def gerar_variacoes():
    entradas = [
        ''.join(random.choices(string.ascii_letters + string.digits, k=50)),  # Texto grande aleatório
        '<script>alert("Falha XSS")</script>',  # XSS básico
        "' OR 1=1 --",  # Injeção SQL simples
        "; DROP TABLE usuarios;",  # SQL destrutivo
        "admin' OR '1'='1",  # Bypass de autenticação
        "<img src=x onerror=alert('XSS')>",  # XSS alternativo
        "1; WAITFOR DELAY '0:0:5' --",  # SQL Injection com atraso (blind)
        "%00' UNION SELECT NULL, NULL --",  # SQL Injection com UNION
    ]
    logger.info("Entradas de fuzzing geradas com sucesso.")
    return entradas


def validar_url(url):
    regex = re.compile(
        r'^https?://'  # Protocolo
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # Domínio
        r'localhost|'  # Localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
        r'(?::\d+)?'  # Porta opcional
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None


def analisar_resposta(resposta, variacao):
    vulneravel = False
    detalhes = {}

    if resposta.status_code >= 500:
        vulneravel = True
        detalhes["motivo"] = "Erro interno do servidor (500+)"

    if variacao in resposta.text:
        vulneravel = True
        detalhes["motivo"] = "Possível XSS refletido"

    sql_erros = ["mysql", "sql server", "sqlite", "ora-", "syntax error"]
    if any(erro in resposta.text.lower() for erro in sql_erros):
        vulneravel = True
        detalhes["motivo"] = "Erro de SQL detectado"

    if resposta.elapsed.total_seconds() > 4:  # Limiar de 4 segundos
        vulneravel = True
        detalhes["motivo"] = "Atraso suspeito (Blind SQL?)"

    return vulneravel, detalhes


def testar_enderecos(url_base, caminhos, variacoes):
    if not validar_url(url_base):
        logger.error("URL base inválida. Encerrando testes.")
        return []

    vulnerabilidades = []
    logger.info("Iniciando testes de fuzzing em %s", url_base)
    print("xxx iniciando testes xxx")

    for caminho in caminhos:
        for variacao in variacoes:
            url = f"{url_base}/{caminho}?q={variacao}"
            try:
                resposta = requests.get(url, timeout=5)
                print(f"testando {url} -  HTTP: {resposta.status_code}")
                logger.info("Requisição enviada: %s - Status: %d", url, resposta.status_code)

                vulneravel, detalhes = analisar_resposta(resposta, variacao)
                if vulneravel or resposta.status_code >= 500 or "erro" in resposta.text.lower():
                    vulnerabilidades.append({
                        "url": url,
                        "entrada_usada": variacao,
                        "codigo_http": resposta.status_code,
                        "tamanho_resposta": len(resposta.text),
                        "tempo_resposta": resposta.elapsed.total_seconds(),
                        "detalhes": detalhes
                    })
            except requests.exceptions.Timeout:
                logger.warning("Timeout ao acessar %s", url)
                vulnerabilidades.append({
                    "url": url,
                    "entrada_usada": variacao,
                    "erro": "Timeout após 5 segundos"
                })
            except requests.exceptions.ConnectionError:
                logger.warning("Erro de conexão ao acessar %s", url)
                vulnerabilidades.append({
                    "url": url,
                    "entrada_usada": variacao,
                    "erro": "Falha de conexão"
                })
            except requests.exceptions.RequestException as e:
                print(f"erro ao acessar {url}: {e}")
                logger.error("Exceção não esperada: %s", e)
                vulnerabilidades.append({
                    "url": url,
                    "entrada_usada": variacao,
                    "erro": str(e)
                })
    return vulnerabilidades


def capturar_pacotes_http(interface):
    def captura_thread():
        logger.info("Iniciando captura de pacotes na interface %s", interface)
        print("xxx Observando pacotes HTTP na interface:", interface)
        sniff(iface=interface, filter="tcp port 80 or tcp port 443", prn=processar_pacote, count=20)

    thread = threading.Thread(target=captura_thread)
    thread.start()
    return thread


def processar_pacote(pacote):
    if pacote.haslayer(IP):
        ip_origem = pacote[IP].src
        ip_destino = pacote[IP].dst
        print(f"xxx Pacote capturado: {ip_origem} => {ip_destino}")
        if pacote.haslayer(TCP) and (pacote[TCP].sport == 80 or pacote[TCP].dport == 80 or
                                     pacote[TCP].sport == 443 or pacote[TCP].dport == 443):
            payload = bytes(pacote[TCP].payload).decode('utf-8', errors='ignore')
            logger.debug("Payload capturado: %s", payload[:100])
            pacote_queue.put({
                "ip_origem": ip_origem,
                "ip_destino": ip_destino,
                "payload": payload[:100]
            })


def salvar_resultados(arquivo_dados, nome_arquivo="resultados.json"):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(arquivo_dados, arquivo, indent=4)
    print(f"xxx resultados salvos em {nome_arquivo}")
    logger.info("Resultados salvos em %s", nome_arquivo)


def gerar_relatorio(vulnerabilidades):
    print("\n=== Relatório de Vulnerabilidades ===")
    for falha in vulnerabilidades:
        print(f"URL: {falha['url']}")
        print(f"Entrada usada: {falha['entrada_usada']}")
        print(f"Código HTTP: {falha.get('codigo_http', 'Erro')}")
        print(f"Tempo de resposta: {falha.get('tempo_resposta', 'N/A')} segundos")
        print(f"Detalhes: {falha.get('detalhes', 'Nenhum')}")
        print("-" * 50)


if __name__ == "__main__":
    interfaces = get_if_list()
    print("xxx interfaces :", interfaces)
    interface = input("Entre com o nome da interface que deseja monitorar: ")

    if interface not in interfaces:
        logger.error("Interface %s inválida. Encerrando.", interface)
        exit(1)

    captura_thread = capturar_pacotes_http(interface)

    url_base = input("Qual a URL base do servidor para os testes: ")

    caminhos = ["admin", "login", "teste", "configuracao"]
    variacoes = gerar_variacoes()
    vulnerabilidades = testar_enderecos(url_base, caminhos, variacoes)

    captura_thread.join()

    print("xxx enderecos vulneraveis detectados:")
    for falha in vulnerabilidades:
        print(
            f"URL: {falha['url']} - Entrada usada: {falha['entrada_usada']} - Código HTTP: {falha.get('codigo_http', 'Erro')}")

    salvar_resultados(vulnerabilidades)
    gerar_relatorio(vulnerabilidades)