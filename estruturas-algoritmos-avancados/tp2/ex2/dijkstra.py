import heapq


def dijkstra(grafo, inicio):
    dist = {v: float('inf') for v in grafo}
    dist[inicio] = 0
    heap = [(0, inicio)]

    while heap:
        custo, atual = heapq.heappop(heap)
        for vizinho in grafo[atual]:
            novo_custo = custo + 1  # Supondo arestas de peso 1
            if novo_custo < dist[vizinho]:
                dist[vizinho] = novo_custo
                heapq.heappush(heap, (novo_custo, vizinho))

    return dist
