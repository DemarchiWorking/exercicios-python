import time
import random
import ipaddress
import matplotlib.pyplot as plt
import os
from flask import Flask, render_template_string


# Classe Trie para armazenar prefixos
class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.eh_fim_do_prefixo = False


class Trie:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, prefixo):
        no = self.raiz
        for parte in prefixo.split("."):
            if parte not in no.filhos:
                no.filhos[parte] = NoTrie()
            no = no.filhos[parte]
        no.eh_fim_do_prefixo = True

    def maior_prefixo(self, ip):
        no = self.raiz
        melhor_correspondencia = ""
        correspondencia_atual = ""
        for parte in ip.split("."):
            if parte in no.filhos:
                correspondencia_atual += parte + "."
                no = no.filhos[parte]
                if no.eh_fim_do_prefixo:
                    melhor_correspondencia = correspondencia_atual[:-1]
            else:
                break
        return melhor_correspondencia


# Função de busca linear
def maior_prefixo_linear(ip, lista_prefixos):
    melhor_correspondencia = ""
    for prefixo in lista_prefixos:
        if ip.startswith(prefixo) and len(prefixo) > len(melhor_correspondencia):
            melhor_correspondencia = prefixo
    return melhor_correspondencia


# Gerar prefixos aleatórios
def gerar_prefixos_aleatorios(n=1000):
    prefixos = set()
    while len(prefixos) < n:
        prefixos.add(str(ipaddress.IPv4Address(random.randint(0, 2 ** 32 - 1)))[:random.randint(3, 10)])
    return list(prefixos)


# Criando a aplicação Flask
app = Flask(__name__)


@app.route('/')
def index():
    # Gerar prefixos e medir tempos sempre que a página for carregada
    prefixos = gerar_prefixos_aleatorios()
    ip_teste = "192.168.1.55"

    trie = Trie()
    inicio_tempo = time.perf_counter_ns()
    for prefixo in prefixos:
        trie.inserir(prefixo)
    tempo_insercao_trie = time.perf_counter_ns() - inicio_tempo

    inicio_tempo = time.perf_counter_ns()
    maior_linear = maior_prefixo_linear(ip_teste, prefixos)
    tempo_busca_linear = time.perf_counter_ns() - inicio_tempo

    inicio_tempo = time.perf_counter_ns()
    maior_trie = trie.maior_prefixo(ip_teste)
    tempo_busca_trie = time.perf_counter_ns() - inicio_tempo

    caminho_static = "static"
    if not os.path.exists(caminho_static):
        os.makedirs(caminho_static)

    caminho_imagem = os.path.join(caminho_static, "comparacao.png")
    plt.figure()
    plt.bar(["Inserção Trie", "Busca Linear", "Busca Trie"],
            [tempo_insercao_trie, tempo_busca_linear, tempo_busca_trie],
            color=["blue", "red", "green"])
    plt.ylabel("Tempo (ns)")
    plt.title("Comparação de Desempenho")
    plt.savefig(caminho_imagem)
    plt.close()

    html = f'''
    <html>
    <head><title>Comparação de Desempenho</title></head>
    <body>
        <h1>Comparação de Desempenho</h1>
        <p>Tempo de inserção na Trie: {tempo_insercao_trie} ns</p>
        <p>Tempo de busca linear: {tempo_busca_linear} ns</p>
        <p>Tempo de busca na Trie: {tempo_busca_trie} ns</p>
        <p>Prefixo mais longo na busca linear: {maior_linear}</p>
        <p>Prefixo mais longo na Trie: {maior_trie}</p>
        <img src="/{caminho_imagem}" width="600">
    </body>
    </html>
    '''
    return render_template_string(html)


if __name__ == '__main__':
    app.run(debug=True)
