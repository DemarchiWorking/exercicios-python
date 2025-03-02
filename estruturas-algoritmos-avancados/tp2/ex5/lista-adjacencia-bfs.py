from collections import deque


class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2, peso):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append((vertice2, peso))
            self.lista_adjacencia[vertice2].append((vertice1, peso))

    def obter_vizinhos(self, vertice):
        return self.lista_adjacencia.get(vertice, [])

    def bfs_rota_mais_curta(self, inicio, fim):
        if inicio not in self.lista_adjacencia or fim not in self.lista_adjacencia:
            return None

        visitado = {vertice: False for vertice in self.lista_adjacencia}
        predecessores = {vertice: None for vertice in self.lista_adjacencia}

        fila = deque([inicio])
        visitado[inicio] = True

        while fila:
            vertice_atual = fila.popleft()

            if vertice_atual == fim:
                caminho = []
                while vertice_atual:
                    caminho.append(vertice_atual)
                    vertice_atual = predecessores[vertice_atual]
                caminho.reverse()
                return caminho

            for vizinho, _ in self.obter_vizinhos(vertice_atual):
                if not visitado[vizinho]:
                    visitado[vizinho] = True
                    predecessores[vizinho] = vertice_atual
                    fila.append(vizinho)

        return None


def exibir_menu():
    print("\nMenu:")
    print("1. Encontrar rota mais curta")
    print("2. Adicionar vértice")
    print("3. Adicionar aresta")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha


def main():
    # Criar o grafo e adicionar os vértices
    grafo = Grafo()
    vertices = ["A", "B", "C", "D", "E"]
    for vertice in vertices:
        grafo.adicionar_vertice(vertice)

    # Adicionar as arestas com pesos conforme a questão
    arestas = [("A", "B", 3), ("A", "C", 2), ("B", "D", 4), ("C", "E", 5), ("D", "E", 1)]
    for vertice1, vertice2, peso in arestas:
        grafo.adicionar_aresta(vertice1, vertice2, peso)

    # Execução inicial para encontrar a rota de A para E
    inicio = "A"
    fim = "E"
    rota_mais_curta = grafo.bfs_rota_mais_curta(inicio, fim)
    if rota_mais_curta:
        print(f"Rota mais curta de {inicio} para {fim}: {' -> '.join(rota_mais_curta)}")
    else:
        print(f"Não existe rota de {inicio} para {fim}.")

    while True:
        escolha = exibir_menu()
        if escolha == "1":
            inicio = input("Digite o vértice de início: ")
            fim = input("Digite o vértice de fim: ")
            rota_mais_curta = grafo.bfs_rota_mais_curta(inicio, fim)
            if rota_mais_curta:
                print(f"Rota mais curta de {inicio} para {fim}: {' -> '.join(rota_mais_curta)}")
            else:
                print(f"Não existe rota de {inicio} para {fim}.")
        elif escolha == "2":
            vertice = input("Digite o vértice a ser adicionado: ")
            grafo.adicionar_vertice(vertice)
            print(f"Vértice {vertice} adicionado.")
        elif escolha == "3":
            vertice1 = input("Digite o primeiro vértice: ")
            vertice2 = input("Digite o segundo vértice: ")
            peso = int(input("Digite o peso da aresta: "))
            grafo.adicionar_aresta(vertice1, vertice2, peso)
            print(f"Aresta entre {vertice1} e {vertice2} com peso {peso} adicionada.")
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
