class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_aresta(self, bairro1, bairro2):
        if bairro1 not in self.grafo:
            self.grafo[bairro1] = []
        if bairro2 not in self.grafo:
            self.grafo[bairro2] = []
        self.grafo[bairro1].append(bairro2)
        self.grafo[bairro2].append(bairro1)

    def vizinhos(self, bairro):
        return self.grafo.get(bairro, [])

def inicializar_grafo(grafo):
    # Adicionar os dados informados na questão como padrão
    grafo.adicionar_aresta("Centro", "Bairro A")
    grafo.adicionar_aresta("Centro", "Bairro B")
    grafo.adicionar_aresta("Bairro A", "Bairro C")
    grafo.adicionar_aresta("Bairro B", "Bairro C")
    grafo.adicionar_aresta("Bairro C", "Bairro D")

def menu():
    print("\nMenu:")
    print("1. Adicionar aresta")
    print("2. Consultar vizinhos")
    print("3. Exibir grafo")
    print("4. Sair")

def main():
    grafo = Grafo()
    inicializar_grafo(grafo)
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            bairro1 = input("Digite o nome do primeiro bairro: ")
            bairro2 = input("Digite o nome do segundo bairro: ")
            grafo.adicionar_aresta(bairro1, bairro2)
            print(f"Aresta adicionada entre {bairro1} e {bairro2}.")
        elif opcao == '2':
            bairro = input("Digite o nome do bairro: ")
            vizinhos = grafo.vizinhos(bairro)
            print(f"Vizinhos de {bairro}: {vizinhos}")
        elif opcao == '3':
            print("Grafo atual:")
            for bairro, vizinhos in grafo.grafo.items():
                print(f"{bairro}: {vizinhos}")
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
