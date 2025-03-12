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

    def autocomplete(self, prefixo):
        inicio = time.perf_counter_ns()
        atual = self.raiz

        for letra in prefixo:
            if letra not in atual.filhos:
                print(f"Nenhuma palavra encontrada com o prefixo '{prefixo}'")
                return []
            atual = atual.filhos[letra]

        palavras = []
        self.dfs(atual, prefixo, palavras)

        fim = time.perf_counter_ns()
        print(f"Palavras com o prefixo '{prefixo}': {palavras}")
        print(f"Tempo para autocomplete: {(fim - inicio) / 1_000_000:.6f} ms")
        return palavras

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
        print("======= MENU TRIE ====== \n")
        print("1. Inserir palavra")
        print("2. Exibir todas as palavras")
        print("3. Autocomplete por prefixo")
        print("4. Mostrar estrutura do Trie")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            palavra = input("Digite a palavra : ").strip()
            trie.inserir_palavra(palavra)
        elif opcao == "2":
            trie.exibir_palavras()
        elif opcao == "3":
            prefixo = input("Digite o prefixo : ").strip()
            trie.autocomplete(prefixo)
        elif opcao == "4":
            trie.mostrar_estrutura()
        elif opcao == "5":
            print("Encerrando ...")
            break
        else:
            print("Inválido! Tente novamente.")


if __name__ == "__main__":
    menu()
