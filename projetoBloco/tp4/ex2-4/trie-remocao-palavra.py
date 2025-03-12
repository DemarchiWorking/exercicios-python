import time

class NoTrie:
    def __init__(self):
        self.filhos = {}  # Cada caractere leva a outro nó
        self.fim_palavra = False  # Indica se é fim da palavra

class Trie:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir_palavra(self, palavra):
        inicio = time.perf_counter_ns()
        atual = self.raiz
        for letra in palavra:
            if letra not in atual.filhos:
                atual.filhos[letra] = NoTrie()
            atual = atual.filhos[letra]
        atual.fim_palavra = True
        fim = time.perf_counter_ns()
        print(f"Palavra '{palavra}' inserida em {(fim - inicio) / 1_000_000:.6f} ms")

    def exibir_palavras(self):
        inicio = time.perf_counter_ns()
        palavras = []
        self.dfs(self.raiz, "", palavras)
        fim = time.perf_counter_ns()
        print(f"Palavras armazenadas: {palavras}")
        print(f"Tempo para exibir palavras: {(fim - inicio) / 1_000_000:.6f} ms")
        return palavras

    def dfs(self, no, prefixo, palavras):
        if no.fim_palavra:
            palavras.append(prefixo)
        for letra, filho in no.filhos.items():
            self.dfs(filho, prefixo + letra, palavras)

    def buscar_palavra(self, palavra):
        inicio = time.perf_counter_ns()
        atual = self.raiz
        for letra in palavra:
            if letra not in atual.filhos:
                fim = time.perf_counter_ns()
                print(f"'{palavra}' não encontrada (tempo: {(fim - inicio) / 1_000_000:.6f} ms)")
                return False
            atual = atual.filhos[letra]
        fim = time.perf_counter_ns()
        if atual.fim_palavra:
            print(f"'{palavra}' encontrada em {(fim - inicio) / 1_000_000:.6f} ms")
            return True
        else:
            print(f"'{palavra}' não encontrada (tempo: {(fim - inicio) / 1_000_000:.6f} ms)")
            return False

    def remover_palavra(self, palavra):
        """
        Remove uma palavra do Trie e ajusta os nós, removendo os desnecessários.
        """
        inicio = time.perf_counter_ns()

        def _remover(no, palavra, profundidade):
            if profundidade == len(palavra):  # Fim da palavra
                if not no.fim_palavra:
                    return False  # A palavra não existe
                no.fim_palavra = False  # Desmarca o final da palavra
                return len(no.filhos) == 0  # Retorna True se o nó não tiver filhos

            letra = palavra[profundidade]
            if letra not in no.filhos:
                return False  # A palavra não existe

            deve_remover_filho = _remover(no.filhos[letra], palavra, profundidade + 1)

            # Remove o nó filho se for desnecessário
            if deve_remover_filho:
                del no.filhos[letra]
                return len(no.filhos) == 0 and not no.fim_palavra

            return False

        resultado = _remover(self.raiz, palavra, 0)
        fim = time.perf_counter_ns()

        if resultado:
            print(f"Palavra '{palavra}' removida com sucesso em {(fim - inicio) / 1_000_000:.6f} ms")
        else:
            print(f"Falha ao remover a palavra '{palavra}' (tempo: {(fim - inicio) / 1_000_000:.6f} ms)")

    def mostrar_estrutura(self):
        inicio = time.perf_counter_ns()
        self.mostrar_recursivo(self.raiz, "")
        fim = time.perf_counter_ns()
        print(f"Tempo para exibir estrutura: {(fim - inicio) / 1_000_000:.6f} ms")

    def mostrar_recursivo(self, no, prefixo):
        if no.fim_palavra:
            print(f"Palavra: {prefixo}")
        for letra, filho in no.filhos.items():
            self.mostrar_recursivo(filho, prefixo + letra)

def menu():
    trie = Trie()
    while True:
        print("\n======= MENU TRIE ======")
        print("1. Inserir palavra")
        print("2. Exibir todas as palavras")
        print("3. Buscar palavra")
        print("4. Remover palavra")
        print("5. Mostrar estrutura do Trie")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            palavra = input("Digite a palavra: ").strip()
            trie.inserir_palavra(palavra)
        elif opcao == "2":
            trie.exibir_palavras()
        elif opcao == "3":
            palavra = input("Digite a palavra para buscar: ").strip()
            trie.buscar_palavra(palavra)
        elif opcao == "4":
            palavra = input("Digite a palavra para remover: ").strip()
            trie.remover_palavra(palavra)
        elif opcao == "5":
            trie.mostrar_estrutura()
        elif opcao == "6":
            print("Encerrando...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
