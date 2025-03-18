def floyd_warshall(grafo):
    bairros = list(grafo.keys())
    quantidade_bairros = len(bairros)
    distancias = {bairro: {vizinho: float('inf') for vizinho in bairros} for bairro in bairros}

    for bairro in bairros:
        distancias[bairro][bairro] = 0

    for bairro in grafo:
        for vizinho, peso in grafo[bairro]:
            distancias[bairro][vizinho] = peso

    for k in bairros:
        for i in bairros:
            for j in bairros:
                distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])

    return distancias


grafo = {
    'A': [('B', 3), ('C', 8), ('D', float('inf'))],
    'B': [('A', 3), ('C', 2), ('D', 5)],
    'C': [('A', 8), ('B', 2), ('D', 1)],
    'D': [('A', float('inf')), ('B', 5), ('C', 1)],
}

matriz_distancias = floyd_warshall(grafo)

print("Menores distâncias entre todos os pares de bairros:")
for i in matriz_distancias:
    for j in matriz_distancias[i]:
        print(f"{i} -> {j}: {matriz_distancias[i][j]}")
