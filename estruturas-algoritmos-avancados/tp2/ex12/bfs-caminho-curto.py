from collections import deque


# Classe para representar o grafo usando lista de adjacência
class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}  # Dicionário para armazenar o grafo

    # Adiciona um vértice ao grafo
    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    # Adiciona uma aresta bidirecional (grafo não direcionado)
    def adicionar_aresta(self, vertice1, vertice2):
        self.lista_adjacencia[vertice1].append(vertice2)
        self.lista_adjacencia[vertice2].append(vertice1)

    # Implementação do algoritmo BFS para encontrar o caminho mais curto
    def bfs_caminho_mais_curto(self, inicio, destino):
        # Fila para gerenciar os nós a serem visitados e o caminho até eles
        fila = deque([(inicio, [inicio])])
        visitados = set()  # Conjunto para controlar os visitados

        while fila:
            vertice_atual, caminho = fila.popleft()

            if vertice_atual == destino:
                return caminho  # Retorna o caminho encontrado

            for vizinho in self.lista_adjacencia[vertice_atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append((vizinho, caminho + [vizinho]))

        return None  # Retorna None se não houver caminho


# Criando o grafo conforme o enunciado
grafo = Grafo()
vertices = ["A", "B", "C", "D", "E", "F"]
for v in vertices:
    grafo.adicionar_vertice(v)

arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"), ("D", "F"), ("E", "F")]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

# Executando o BFS para encontrar o caminho mais curto de A para F
caminho = grafo.bfs_caminho_mais_curto("A", "F")
print("Caminho mais curto de A para F:", caminho)
