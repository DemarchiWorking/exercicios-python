import time
import tracemalloc


class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        # Adiciona um vértice ao grafo
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        # Adiciona uma aresta não-direcionada entre dois vértices
        self.lista_adjacencia[vertice1].append(vertice2)
        self.lista_adjacencia[vertice2].append(vertice1)

    def dfs_recursivo(self, vertice, visitados=None):
        # Implementa DFS de forma recursiva
        if visitados is None:
            visitados = set()

        print(vertice, end=" ")  # Exibe o vértice visitado
        visitados.add(vertice)  # Marca como visitado

        # Percorre os vizinhos do vértice
        for vizinho in self.lista_adjacencia[vertice]:
            if vizinho not in visitados:
                self.dfs_recursivo(vizinho, visitados)


# Criando o grafo
grafo = Grafo()
vertices = ["A", "B", "C", "D", "E"]  # Removido o vértice F
for v in vertices:
    grafo.adicionar_vertice(v)

# Adicionando as arestas conforme o enunciado
arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E")]  # Removida a aresta ("C", "F")
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

# Medindo tempo e memória
tracemalloc.start()
start_time = time.perf_counter()
print("Busca em Profundidade (DFS) iniciando em A:")
grafo.dfs_recursivo("A")
end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()

# Resultados
print(f"\nTempo de execução: {(end_time - start_time) * 1000:.4f} ms")
print(f"Memória usada: {current / 1024:.4f} KB; Pico: {peak / 1024:.4f} KB")
tracemalloc.stop()


# Definindo o grafo como um dicionário de listas de adjacência
#grafo = {
#    'A': ['B', 'C'],
#    'B': ['D'],
#    'C': ['E'],
#    'D': [],
#    'E': []
#}

# Função de DFS recursiva
#def dfs(grafo, vertice, visitados):
#    if vertice not in visitados:
#        print(vertice)
#        visitados.add(vertice)
#        for vizinho in grafo[vertice]:
#            dfs(grafo, vizinho, visitados)

# Iniciando a DFS a partir do vértice A
#visitados = set()
#dfs(grafo, 'A', visitados)
