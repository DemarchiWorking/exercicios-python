#Exercício 10: Aplicação de Trie
#Enunciado: Explique como a estrutura Trie pode ser usada para desenvolver um sistema de autocomplete. Implemente uma função que, dado um prefixo, retorne todas as palavras armazenadas na Trie que começam com esse prefixo.

from flask import Flask, render_template, jsonify, request

class NodoTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_da_palavra = False

class Trie:
    def __init__(self):
        self.raiz = NodoTrie()

    def inserir(self, palavra):
        nodo = self.raiz
        for letra in palavra:
            if letra not in nodo.filhos:
                nodo.filhos[letra] = NodoTrie()
            nodo = nodo.filhos[letra]
        nodo.fim_da_palavra = True

    def buscar_autocompletamento(self, prefixo):
        nodo = self.raiz
        for letra in prefixo:
            if letra not in nodo.filhos:
                return []
            nodo = nodo.filhos[letra]
        return self._coletar_palavras(nodo, prefixo)

    def _coletar_palavras(self, nodo, prefixo):
        palavras = []
        if nodo.fim_da_palavra:
            palavras.append(prefixo)
        for letra, filho in nodo.filhos.items():
            palavras.extend(self._coletar_palavras(filho, prefixo + letra))
        return palavras


app = Flask(__name__)
trie = Trie()

palavras_iniciais = ["casa", "carro", "caminhão", "cachorro", "cadeira"]
for palavra in palavras_iniciais:
    trie.inserir(palavra)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    prefixo = request.args.get('prefixo', '')
    sugestoes = trie.buscar_autocompletamento(prefixo)
    return jsonify(sugestoes)

@app.route('/inserir', methods=['POST'])
def inserir_palavra():
    palavra = request.form.get('palavra', '')
    if palavra:
        trie.inserir(palavra)
        return jsonify({"status": "Palavra inserida com sucesso!", "palavra": palavra})
    return jsonify({"status": "Erro ao inserir palavra!"})

if __name__ == "__main__":
    app.run(debug=True)
