from flask import Flask, render_template, jsonify, request
import csv
import os

class NodoTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_da_palavra = False

class Trie:
    def __init__(self):
        self.raiz = NodoTrie()
    def inserir(self, palavra):
        palavra = palavra.lower()  # Normalização para minúsculas
        nodo = self.raiz
        for letra in palavra:
            if letra not in nodo.filhos:
                nodo.filhos[letra] = NodoTrie()
            nodo = nodo.filhos[letra]
        nodo.fim_da_palavra = True
    def buscar_autocompletamento(self, prefixo):
        prefixo = prefixo.lower()  # Normalização para minúsculas
        nodo = self.raiz
        for letra in prefixo:
            if letra not in nodo.filhos:
                return []
            nodo = nodo.filhos[letra]
        return self._coletar_palavras(nodo, prefixo)
    def buscar_correcao(self, palavra):
        palavra = palavra.lower()  # Normalização para minúsculas

        def calcular_distancia(a, b):
            m, n = len(a), len(b)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(m + 1):
                for j in range(n + 1):
                    if i == 0:
                        dp[i][j] = j
                    elif j == 0:
                        dp[i][j] = i
                    elif a[i - 1] == b[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
            return dp[m][n]
        palavras = self._coletar_palavras(self.raiz, "")
        palavras_proximas = []
        for p in palavras:
            distancia = calcular_distancia(palavra, p)
            if distancia <= 2:  # Ajuste o limite conforme necessário
                palavras_proximas.append(p)
        return palavras_proximas

    def _coletar_palavras(self, nodo, prefixo):
        palavras = []
        if nodo.fim_da_palavra:
            palavras.append(prefixo)
        for letra, filho in nodo.filhos.items():
            palavras.extend(self._coletar_palavras(filho, prefixo + letra))
        return palavras

app = Flask(__name__)
trie = Trie()


def carregar_palavras_do_arquivo(arquivo):
    if not os.path.exists(arquivo):
        with open(arquivo, 'w', newline='') as f:
            writer = csv.writer(f)
            # Adicionando títulos de exemplo
            writer.writerow(["O Senhor dos Anéis".lower()])
            writer.writerow(["Harry Potter e a Pedra Filosofal".lower()])
            writer.writerow(["O Código Da Vinci".lower()])
            writer.writerow(["A Culpa é das Estrelas".lower()])
            writer.writerow(["Game of Thrones".lower()])
    else:
        with open(arquivo, 'r') as f:
            reader = csv.reader(f)
            for linha in reader:
                trie.inserir(linha[0].lower())  # Normalização para minúsculas

carregar_palavras_do_arquivo("livros.csv")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    prefixo = request.args.get('prefixo', '')
    sugestoes = trie.buscar_autocompletamento(prefixo)
    return jsonify(sugestoes)

@app.route('/correcao', methods=['GET'])
def correcao():
    palavra = request.args.get('palavra', '')
    sugestoes = trie.buscar_correcao(palavra)
    return jsonify(sugestoes)

@app.route('/processar', methods=['GET'])
def processar():
    entrada = request.args.get('entrada', '')
    autocompletos = trie.buscar_autocompletamento(entrada)
    correcoes = trie.buscar_correcao(entrada)
    return jsonify({"autocompletos": autocompletos, "correcoes": correcoes})

@app.route('/inserir', methods=['POST'])
def inserir_palavra():
    palavra = request.form.get('palavra', '')
    if palavra:
        trie.inserir(palavra)
        return jsonify({"status": "Palavra inserida com sucesso!", "palavra": palavra})
    return jsonify({"status": "Erro ao inserir palavra!"})

if __name__ == "__main__":
    app.run(debug=True)
