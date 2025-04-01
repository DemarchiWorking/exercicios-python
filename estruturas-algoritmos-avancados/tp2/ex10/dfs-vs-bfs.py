import time
import tracemalloc
from collections import deque



# Função DFS com print da ordem de visitação
def dfs(grafo, inicio, visitado=None):
    if visitado is None:
        visitado = set()
    visitado.add(inicio)
    print(inicio, end=' ')  # Print da ordem de visitação
    for vizinho in grafo[inicio]:
        if vizinho not in visitado:
            dfs(grafo, vizinho, visitado)

# Função BFS com print da ordem de visitação
def bfs(grafo, inicio):
    visitado = set()
    fila = deque([inicio])
    visitado.add(inicio)
    while fila:
        vertice = fila.popleft()
        print(vertice, end=' ')  # Print da ordem de visitação
        for vizinho in grafo[vertice]:
            if vizinho not in visitado:
                visitado.add(vizinho)
                fila.append(vizinho)

# Função para medir tempo e memória
def medir_tempo_memoria(func, *args):
    tracemalloc.start()
    inicio_tempo = time.perf_counter()
    func(*args)
    fim_tempo = time.perf_counter()
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tempo_ms = (fim_tempo - inicio_tempo) * 1000  # Converte para milissegundos
    return tempo_ms, memoria_pico

# Medindo DFS com ordem de visitação
print("=== DFS (Ordem):\n")
tempo_dfs, memoria_dfs = medir_tempo_memoria(dfs, grafo, 1)
print(f"=== DFS - Tempo: {tempo_dfs:.4f} ms, Mem: {memoria_dfs} bytes\n")

# Medindo BFS com ordem de visitação
print("=== BFS (Ordem):\n")
tempo_bfs, memoria_bfs = medir_tempo_memoria(bfs, grafo, 1)
print(f"=== BFS - Tempo: {tempo_bfs:.4f} ms, Mem: {memoria_bfs} bytes\n")
