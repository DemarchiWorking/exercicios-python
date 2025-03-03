from collections import deque


# Classe para representar o grafo usando lista de adjacência ponderada
class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}  # Dicionário para armazenar o grafo

    # Adiciona um vértice ao grafo
    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    # Adiciona uma aresta bidirecional (grafo não direcionado)
    def adicionar_aresta(self, vertice1, vertice2, peso):
        self.lista_adjacencia[vertice1].append((vertice2, peso))
        self.lista_adjacencia[vertice2].append((vertice1, peso))

    # Implementação do algoritmo BFS adaptado para encontrar o caminho mais curto em termos de distância
    def bfs_caminho_mais_curto(self, inicio, destino):
        # Fila para gerenciar os nós a serem visitados e o caminho até eles
        fila = deque([(inicio, [inicio], 0)])  # Cada elemento é uma tupla (vértice_atual, caminho, distancia_acumulada)
        visitados = set()  # Conjunto para controlar os visitados
        melhor_caminho = None
        menor_distancia = float('inf')

        while fila:
            vertice_atual, caminho, distancia_atual = fila.popleft()

            if vertice_atual == destino:
                if distancia_atual < menor_distancia:
                    menor_distancia = distancia_atual
                    melhor_caminho = caminho
                continue

            for vizinho, peso in self.lista_adjacencia[vertice_atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append((vizinho, caminho + [vizinho], distancia_atual + peso))

        return melhor_caminho, menor_distancia if melhor_caminho else (None, None)


# Criando o grafo conforme o enunciado
grafo = Grafo()
vertices = ["A", "B", "C", "D", "E", "F"]
for v in vertices:
    grafo.adicionar_vertice(v)

arestas = [
    ("A", "B", 1.5), ("A", "C", 2.0), ("B", "D", 2.5),
    ("C", "E", 1.8), ("D", "F", 3.0), ("E", "F", 2.2)
]
for v1, v2, peso in arestas:
    grafo.adicionar_aresta(v1, v2, peso)

# Executando o BFS adaptado para encontrar o caminho mais curto de A para F
caminho, distancia = grafo.bfs_caminho_mais_curto("A", "F")
print("Caminho mais curto de A para F:", caminho)
print("Distância total:", distancia, "km")
