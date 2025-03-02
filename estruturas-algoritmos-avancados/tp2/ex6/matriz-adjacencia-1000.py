import time
import sys

# Definindo as arestas
arestas = [
    (0, 1), (0, 2), (0, 3), (4, 5), (6, 7),
    (8, 9), (10, 11), (12, 13), (14, 15), (16, 17)
]

# Criando a matriz de adjacência
matriz_adj = [[0] * 1000 for _ in range(1000)]
for u, v in arestas:
    matriz_adj[u][v] = 1
    matriz_adj[v][u] = 1

# Medindo uso de memória
memoria_matriz = sys.getsizeof(matriz_adj) + sum(sys.getsizeof(linha) for linha in matriz_adj)

# Medindo tempo para buscar vizinhos
inicio = time.perf_counter()
vizinhos = [i for i, v in enumerate(matriz_adj[0]) if v == 1]
tempo_vizinhos_matriz = (time.perf_counter() - inicio) * 1000  # Convertendo para ms

# Medindo tempo para verificar se uma aresta existe
inicio = time.perf_counter()
existe_aresta = matriz_adj[0][1] == 1
tempo_aresta_matriz = (time.perf_counter() - inicio) * 1000  # Convertendo para ms

print("=== Matriz de Adjacência ===")
print(f"Uso de Memória: {memoria_matriz} bytes")
print(f"Tempo para buscar vizinhos: {tempo_vizinhos_matriz:.10f} ms")
print(f"Tempo para verificar aresta: {tempo_aresta_matriz:.10f} ms")
