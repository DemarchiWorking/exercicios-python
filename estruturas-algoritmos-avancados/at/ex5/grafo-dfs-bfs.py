from collections import deque
import time
import tracemalloc


class Grafo:

    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        self.lista_adjacencia[vertice1].append(vertice2)
        self.lista_adjacencia[vertice2].append(vertice1)

    def dfs(self, vertice, visitados=None):
        if visitados is None:
            visitados = set()
        visitados.add(vertice)
        resultado = [vertice]
        for vizinho in self.lista_adjacencia[vertice]:
            if vizinho not in visitados:
                resultado.extend(self.dfs(vizinho, visitados))
        return resultado

    def bfs(self, inicio):
        visitados = set()
        fila = deque([inicio])
        visitados.add(inicio)
        resultado = []
        while fila:
            vertice = fila.popleft()
            resultado.append(vertice)
            for vizinho in self.lista_adjacencia[vertice]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)
        return resultado


def medir_performance(func, *args):
    tracemalloc.start()
    inicio_tempo = time.perf_counter()
    resultado = func(*args)
    fim_tempo = time.perf_counter()
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tempo_ms = (fim_tempo - inicio_tempo) * 1000
    return resultado, tempo_ms, memoria_pico


grafo = Grafo()
vertices = ["A", "B", "C", "D", "E", "F"]
for v in vertices:
    grafo.adicionar_vertice(v)

arestas = [
    ("A", "B"), ("A", "C"),
    ("B", "D"), ("B", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F")
]
for v1, v2 in arestas:
    grafo.adicionar_aresta(v1, v2)

inicio = "A"

print("xxx busca em profundidade (DFS): xxx")
resultado_dfs, tempo_dfs, pico_dfs = medir_performance(grafo.dfs, inicio)
print(f"ordem de visitacao: {' -> '.join(resultado_dfs)}")
print(f"tempo: {tempo_dfs:.4f} ms")
print(f"memoria pico: {pico_dfs} bytes")

# Execução BFS
print("xxx Busca em largura (BFS): xxx")
resultado_bfs, tempo_bfs, pico_bfs = medir_performance(grafo.bfs, inicio)
print(f"ordem de visitacao: {' -> '.join(resultado_bfs)}")
print(f"tempo: {tempo_bfs:.4f} ms")
print(f"memória pico: {pico_bfs} bytes")
