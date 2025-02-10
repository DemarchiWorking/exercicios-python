#Exercício 9: Inserção e Busca em Trie
#Enunciado: Dado o seguinte código para inserir palavras em uma Trie, complete a função search(word) para verificar se uma palavra está presente na estrutura.

class TrieNode:
    def __init__(self):
        self.children = {}  # Dicionário de decendentes
        self.is_end_of_word = False  # Marca se o nó é o final

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Nó raiz

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Cria nó para o caractere
            node = node.children[char]  # Move para próximo
        node.is_end_of_word = True  # Marca o final da palavra

    def search(self, word):
        no = self.root  # Comece
        for caracter in word:  # Para cada caractere da palavra
            if caracter not in no.children:  # Se o caractere não está nos filhos
                return False  # A palavra não existe na Trie
            no = no.children[caracter]  # Mova para o próximo nó
        return no.is_end_of_word  # Se o último nó for o final de uma palavra, retorna True

trie = Trie()
trie.insert("casa")
trie.insert("carro")
trie.insert("caminhão")
trie.insert("cachorro")
trie.insert("cadeira")

print('Não existem:')
print(trie.search("ca"))
print(trie.search("cas"))
print('Existem:')
print(trie.search("casa"))
print(trie.search("carro"))
print(trie.search("caminhão"))
print(trie.search("cachorro"))
print(trie.search("cadeira"))