#Exercício 7: Implementação de Trie
#Enunciado: Implemente uma Trie em Python para armazenar um conjunto de palavras. A implementação deve conter métodos para inserir e buscar palavras.

class NoTrie:
    def __init__(self):
        # Cada nó pode ter múltiplos filhos, que são armazenados como um dicionário
        # As chaves do dicionário são caracteres, e os valores são instâncias de NoTrie
        self.filhos = {}
        # Atributo que indica se o nó atual é o final de uma palavra
        self.final = False


class Trie:
    def __init__(self):
        # Inicializa a Trie com um nó raiz que é uma instância de NoTrie
        self.raiz = NoTrie()

    def inserir(self, palavra):
        """Insere uma palavra na Trie"""
        # Começa a inserção a partir do nó raiz
        no_atual = self.raiz
        for letra in palavra:
            # Se o filho para a letra não existir, cria um novo nó
            if letra not in no_atual.filhos:
                no_atual.filhos[letra] = NoTrie()
            # Move para o nó filho correspondente à letra atual
            no_atual = no_atual.filhos[letra]
        # Marca o nó final da palavra como True para indicar o fim da palavra
        no_atual.final = True

    def buscar(self, palavra):
        """Busca uma palavra na Trie"""
        # Começa a busca a partir do nó raiz
        no_atual = self.raiz
        for letra in palavra:
            # Se algum caractere não existir nos filhos, retorna False
            if letra not in no_atual.filhos:
                return False
            # Move para o nó filho correspondente à letra atual
            no_atual = no_atual.filhos[letra]
        # Retorna True se o nó final foi encontrado, indicando que a palavra existe na Trie
        return no_atual.final

    def listar_palavras(self, no_atual=None, prefixo='', resultado=None):
        """Lista todas as palavras na Trie"""
        # Inicializa a lista de resultados se ainda não foi feita
        if resultado is None:
            resultado = []
        # Começa a partir do nó raiz se nenhum nó for passado
        if no_atual is None:
            no_atual = self.raiz

        # Se o nó atual marca o fim de uma palavra, adiciona o prefixo ao resultado
        if no_atual.final:
            resultado.append(prefixo)

        # Recursivamente percorre os filhos do nó atual
        for letra, filho in no_atual.filhos.items():
            # Adiciona a letra ao prefixo e chama listar_palavras recursivamente
            self.listar_palavras(filho, prefixo + letra, resultado)

        # Retorna a lista de palavras encontradas
        return resultado


# Função principal para o menu
def menu():
    # Cria uma instância da Trie
    trie = Trie()

    while True:
        # Exibe as opções do menu
        print("\nEscolha uma opção:")
        print("1 - Inserir palavras")
        print("2 - Buscar palavras")
        print("3 - Listar todas as palavras")
        print("4 - Sair")

        # Lê a opção escolhida pelo usuário
        opcao = input("Digite o número da opção: ")

        if opcao == '1':
            # Se a opção for 1, lê a palavra a ser inserida
            palavra = input("Digite a palavra para inserir: ")
            # Insere a palavra na Trie
            trie.inserir(palavra)
            # Informa que a palavra foi inserida com sucesso
            print(f"Palavra '{palavra}' inserida com sucesso.")

        elif opcao == '2':
            # Se a opção for 2, lê a palavra a ser buscada
            palavra = input("Digite a palavra para buscar: ")
            # Busca a palavra na Trie e informa se foi encontrada
            if trie.buscar(palavra):
                print(f"A palavra '{palavra}' foi encontrada.")
            else:
                print(f"A palavra '{palavra}' não foi encontrada.")

        elif opcao == '3':
            # Se a opção for 3, lista todas as palavras na Trie
            palavras = trie.listar_palavras()
            if palavras:
                # Exibe todas as palavras encontradas
                print("Palavras na Trie:")
                for palavra in palavras:
                    print(palavra)
            else:
                # Informa que nenhuma palavra foi inserida ainda
                print("Nenhuma palavra foi inserida ainda.")

        elif opcao == '4':
            # Se a opção for 4, sai do menu
            print("Saindo...")
            break

        else:
            # Se a opção for inválida, informa o usuário
            print("Opção inválida. Tente novamente.")


# Chama a função do menu para iniciar a interação com o usuário
menu()
