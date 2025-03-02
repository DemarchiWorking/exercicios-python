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

    def obter_vizinhos(self, vertice):
        return self.lista_adjacencia.get(vertice, [])

class MostrarVizinhos:
    def __init__(self, grafo):
        self.grafo = grafo

    def exibir_vizinhos(self, vertice):
        vizinhos = self.grafo.obter_vizinhos(vertice)
        if vizinhos:
            vizinhos_str = ", ".join(vizinhos)
            print(f"Vizinhos de {vertice}: {vizinhos_str}")
        else:
            print(f"{vertice} não tem vizinhos ou não existe no grafo.")

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

    # Criar a classe MostrarVizinhos e exibir vizinhos para cada centro
    mostrar_vizinhos = MostrarVizinhos(grafo)
    for vertice in vertices:
        mostrar_vizinhos.exibir_vizinhos(vertice)

if __name__ == "__main__":
    main()
