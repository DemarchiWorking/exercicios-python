import heapq


def dijkstra(grafo, origem):
    distancias = {cidade: float('infinity') for cidade in grafo}
    distancias[origem] = 0

    fila_prioridade = [(0, origem)]

    while fila_prioridade:
        custo_atual, cidade_atual = heapq.heappop(fila_prioridade)

        if custo_atual > distancias[cidade_atual]:
            continue

        for vizinho, peso in grafo[cidade_atual].items():
            novo_custo = custo_atual + peso

            if novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo
                heapq.heappush(fila_prioridade,
                               (novo_custo, vizinho))

    return distancias

grafo = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

cidade_origem = 'A'
resultado = dijkstra(grafo, cidade_origem)

print(f"Menores custos para cada cidade partindo de {cidade_origem}: {resultado}")
