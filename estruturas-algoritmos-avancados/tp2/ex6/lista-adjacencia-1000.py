import time
import sys

# Criando a lista de adjacência
lista_adj = {i: [] for i in range(1000)}
arestas = [(0, 1), (0, 2), (0, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15), (16, 17)]
for u, v in arestas:
    lista_adj[u].append(v)
    lista_adj[v].append(u)

# Medindo uso de memória
memoria_lista = sys.getsizeof(lista_adj) + sum(sys.getsizeof(v) for v in lista_adj.values())

# Medindo tempo para buscar vizinhos
inicio = time.perf_counter()
vizinhos = lista_adj[0]
tempo_vizinhos_lista = (time.perf_counter() - inicio) * 1000  # Convertendo para ms

# Medindo tempo para verificar se uma aresta existe
inicio = time.perf_counter()
existe_aresta = 1 in lista_adj[0]
tempo_aresta_lista = (time.perf_counter() - inicio) * 1000  # Convertendo para ms

print("=== Lista de Adjacência ===")
print(f"Uso de Memória: {memoria_lista} bytes")
print(f"Tempo para buscar vizinhos: {tempo_vizinhos_lista:.10f} ms")
print(f"Tempo para verificar aresta: {tempo_aresta_lista:.10f} ms\n")
