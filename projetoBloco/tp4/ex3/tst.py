import random
from collections import deque
import timeit
import sys


class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_aresta(self, u, v):
        if u not in self.adjacencia:
            self.adjacencia[u] = []
        if v not in self.adjacencia:
            self.adjacencia[v] = []
        self.adjacencia[u].append(v)
        self.adjacencia[v].append(u)


def gerar_grafo_aleatorio(num_nos, num_arestas):
    """Gera grafo conexo aleatório garantido"""
    grafo = Grafo()
    nos = list(range(num_nos))

    for i in range(1, num_nos):
        grafo.adicionar_aresta(random.randint(0, i - 1), i)

    for _ in range(num_arestas - num_nos + 1):
        u, v = random.sample(nos, 2)
        grafo.adicionar_aresta(u, v)

    return grafo


def dfs(grafo, inicio):
    visitados = set()
    pilha = [inicio]
    while pilha:
        no = pilha.pop()
        if no not in visitados:
            visitados.add(no)
            pilha.extend(reversed([v for v in grafo.adjacencia[no] if v not in visitados]))


def bfs(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    while fila:
        no = fila.popleft()
        if no not in visitados:
            visitados.add(no)
            fila.extend([v for v in grafo.adjacencia[no] if v not in visitados])


def medir_desempenho():
    tamanhos = [100, 200, 300, 400, 500, 1000, 1500, 3000]
    resultados = []

    print("Configuração do sistema:")
    print(f"Python {sys.version}")
    print(f"Plataforma: {sys.platform}")
    print("\nIniciando testes...\n")

    for num_nos in tamanhos:
        num_arestas = int(num_nos * 1.5)  # Grafo esparso
        grafo = gerar_grafo_aleatorio(num_nos, num_arestas)

        dfs(grafo, 0)
        bfs(grafo, 0)

        dfs_time = timeit.timeit(
            lambda: dfs(grafo, 0),
            number=100
        ) * 10

        bfs_time = timeit.timeit(
            lambda: bfs(grafo, 0),
            number=100
        ) * 10

        resultados.append((num_nos, dfs_time, bfs_time))

    print(
        f"{'Tamanho':<8} | {'DFS (ms)':<12} | {'BFS (ms)':<12} | {'Diferença (BFS-DFS)':<15} | {'Razão (BFS/DFS)':<10}")
    print("-" * 80)
    for n, dfs_t, bfs_t in resultados:
        diff = bfs_t - dfs_t
        ratio = bfs_t / dfs_t if dfs_t != 0 else float('inf')
        print(f"{n:<8} | {dfs_t:.8f} | {bfs_t:.8f} | {diff:+.8f}        | {ratio:.4f}")


if __name__ == "__main__":
    medir_desempenho()