#Exercício 10: Aplicação de Trie
#Enunciado: Explique como a estrutura Trie pode ser usada para desenvolver um sistema de autocomplete. Implemente uma função que, dado um prefixo, retorne todas as palavras armazenadas na Trie que começam com esse prefixo.

class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.eh_fim_da_palavra = False

class Trie:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, palavra):
        no = self.raiz
        for caractere in palavra:
            if caractere not in no.filhos:
                no.filhos[caractere] = NoTrie()
            no = no.filhos[caractere]
        no.eh_fim_da_palavra = True

    def buscar(self, palavra):
        no = self.raiz
        for caractere in palavra:
            if caractere not in no.filhos:
                return False
            no = no.filhos[caractere]
        return no.eh_fim_da_palavra

    def autocompletar(self, prefixo):
        no = self.raiz
        # Navegar até o nó do último caractere do prefixo
        for caractere in prefixo:
            if caractere not in no.filhos:
                return []  # Se o prefixo não existir, retorna uma lista vazia
            no = no.filhos[caractere]

        # Coletar todas as palavras que começam com o prefixo
        return self.coletar_palavras(no, prefixo)

    def coletar_palavras(self, no, prefixo):
        palavras = []
        if no.eh_fim_da_palavra:
            palavras.append(prefixo)

        for caractere, no_filho in no.filhos.items():
            palavras.extend(self.coletar_palavras(no_filho, prefixo + caractere))

        return palavras

trie = Trie()
trie.inserir("casa")
trie.inserir("carro")
trie.inserir("caminhão")
trie.inserir("cachorro")
trie.inserir("cadeira")

prefixo = "ca"
resultado = trie.autocompletar(prefixo)
print(f"Palavras que inicia com '{prefixo}':")
for palavra in resultado:
    print(palavra)
