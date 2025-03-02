class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.lista_adjacencia and vertice2 in self.lista_adjacencia:
            self.lista_adjacencia[vertice1].append(vertice2)
            self.lista_adjacencia[vertice2].append(vertice1)

    def mostrar_grafo(self):
        for vertice in self.lista_adjacencia:
            vizinhos = ", ".join(self.lista_adjacencia[vertice])
            print(f"{vertice}: {vizinhos}")

def main():
    # Criar o grafo e adicionar os vértices
    grafo = Grafo()
    vertices = ["A", "B", "C", "D", "E"]
    for vertice in vertices:
        grafo.adicionar_vertice(vertice)

    # Adicionar as arestas conforme a questão
    arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "E")]
    for vertice1, vertice2 in arestas:
        grafo.adicionar_aresta(vertice1, vertice2)

    # Exibir o grafo
    grafo.mostrar_grafo()

if __name__ == "__main__":
    main()
