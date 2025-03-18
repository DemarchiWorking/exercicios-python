import time
import random
import heapq
import numpy as np

def dijkstra(grafo, vertice_inicial):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[vertice_inicial] = 0
    fila_prioridade = [(0, vertice_inicial)]

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo[vertice_atual]:
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    return distancias

def floyd_warshall(matriz_adjacencia):
    n = len(matriz_adjacencia)
    distancias = np.array(matriz_adjacencia, copy=True)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

    return distancias

def gerar_grafo_aleatorio(vertices, densidade):
    grafo = {i: [] for i in range(vertices)}
    matriz_adjacencia = [[float('inf')] * vertices for _ in range(vertices)]

    for i in range(vertices):
        matriz_adjacencia[i][i] = 0

    num_arestas = int(densidade * vertices * (vertices - 1) / 2)
    arestas = set()

    while len(arestas) < num_arestas:
        u = random.randint(0, vertices - 1)
        v = random.randint(0, vertices - 1)
        if u != v and (u, v) not in arestas:
            peso = random.randint(1, 20)
            arestas.add((u, v))
            arestas.add((v, u))
            grafo[u].append((v, peso))
            grafo[v].append((u, peso))
            matriz_adjacencia[u][v] = peso
            matriz_adjacencia[v][u] = peso

    return grafo, matriz_adjacencia

def comparar_algoritmos(vertices, densidade):
    grafo, matriz_adjacencia = gerar_grafo_aleatorio(vertices, densidade)

    inicio_dijkstra = time.time()
    for vertice in grafo:
        dijkstra(grafo, vertice)
    tempo_dijkstra = time.time() - inicio_dijkstra

    inicio_floyd = time.time()
    floyd_warshall(matriz_adjacencia)
    tempo_floyd = time.time() - inicio_floyd

    print(f"Comparação para {vertices} vértices e densidade {densidade}:")
    print(f"Tempo de execução do Dijkstra: {tempo_dijkstra:.4f} segundos")
    print(f"Tempo de execução do Floyd-Warshall: {tempo_floyd:.4f} segundos")

print("----- Teste 1: Poucos vértices e baixa densidade -----")
comparar_algoritmos(10, 0.3)

print("\n----- Teste 2: Muitos vértices e baixa densidade -----")
comparar_algoritmos(100, 0.1)

print("\n----- Teste 3: Muitos vértices e alta densidade -----")
comparar_algoritmos(100, 0.9)
