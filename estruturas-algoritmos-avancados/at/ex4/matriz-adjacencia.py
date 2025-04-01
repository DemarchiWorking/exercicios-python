def matriz_adjacencia(vertices, arestas):
    n = len(vertices)
    matriz = [[0] * n for _ in range(n)]

    for origem, destino, peso in arestas:
        i, j = vertices.index(origem), vertices.index(destino)
        matriz[i][j] = peso
        matriz[j][i] = peso

    return matriz

bairros = ['A', 'B', 'C', 'D', 'E', 'F']
conexoes = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 8), ('C', 'E', 3),
    ('D', 'F', 6),
    ('E', 'F', 1)
]

matriz = matriz_adjacencia(bairros, conexoes)

print("matriz de adjacencia:")
for linha in matriz:
    print(linha)
