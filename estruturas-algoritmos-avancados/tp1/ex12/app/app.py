from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.termina_palavra = False
        self.telefone = None


class Trie:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, palavra, telefone):
        no_atual = self.raiz
        for char in palavra:
            if char not in no_atual.filhos:
                no_atual.filhos[char] = NoTrie()
            no_atual = no_atual.filhos[char]
        no_atual.termina_palavra = True
        no_atual.telefone = telefone

    def buscar_prefixo(self, prefixo):
        no_atual = self.raiz
        for char in prefixo:
            if char not in no_atual.filhos:
                return []
            no_atual = no_atual.filhos[char]

        return self._buscar_palavras_com_prefixo(no_atual, prefixo)

    def _buscar_palavras_com_prefixo(self, no, prefixo):
        contatos = []
        if no.termina_palavra:
            contatos.append((prefixo, no.telefone))

        for char, filho in no.filhos.items():
            contatos.extend(self._buscar_palavras_com_prefixo(filho, prefixo + char))

        return contatos


# Criando uma instância da Trie
trie = Trie()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    if nome and telefone:
        trie.inserir(nome, telefone)
        return '', 200
    return '', 400


@app.route('/buscar', methods=['GET'])
def buscar():
    prefixo = request.args.get('prefixo', '')
    resultados = trie.buscar_prefixo(prefixo)
    return jsonify(resultados)


if __name__ == '__main__':
    app.run(debug=True)
