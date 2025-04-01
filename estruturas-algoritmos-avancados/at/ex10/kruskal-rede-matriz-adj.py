import time

def kruskal_matriz_adjacencia(matriz, vertices):
    def find(vertice):
        if parent[vertice] != vertice:
            parent[vertice] = find(parent[vertice])
        return parent[vertice]

    def union(vertice1, vertice2):
        root1 = find(vertice1)
        root2 = find(vertice2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    arestas = []
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if matriz[i][j] != 0:
                arestas.append((matriz[i][j], i, j))

    arestas.sort()

    parent = {v: v for v in range(vertices)}
    rank = {v: 0 for v in range(vertices)}

    mst = []
    custo_total = 0

    for custo, no1, no2 in arestas:
        if find(no1) != find(no2):
            union(no1, no2)
            mst.append((no1, no2, custo))
            custo_total += custo

    return mst, custo_total

if __name__ == "__main__":

#   grafo_matriz = [
#        [0, 2, 3, 0],  # A
#        [2, 0, 1, 4],  # B
#        [3, 1, 0, 0],  # C
#        [0, 4, 0, 0]   # D
#    ]


    grafo_matriz = [
    [0, 2, 3, 6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A
    [2, 0, 8, 4, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # B
    [3, 8, 0, 0, 1, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0],  # C
    [6, 4, 0, 0, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0],  # D
    [5, 0, 1, 0, 0, 0, 4, 0, 7, 0, 0, 0, 0, 0, 0],  # E
    [0, 7, 0, 3, 0, 0, 0, 6, 0, 8, 0, 0, 0, 0, 0],  # F
    [0, 0, 9, 0, 4, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0],  # G
    [0, 0, 0, 2, 0, 6, 0, 0, 0, 5, 0, 8, 0, 0, 0],  # H
    [0, 0, 0, 0, 7, 0, 2, 0, 0, 0, 3, 0, 5, 0, 0],  # I
    [0, 0, 0, 0, 0, 8, 0, 5, 0, 0, 0, 4, 0, 7, 0],  # J
    [0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0, 4],  # K
    [0, 0, 0, 0, 0, 0, 0, 8, 0, 4, 0, 0, 0, 6, 0],  # L
    [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 1],  # M
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 6, 0, 0, 3],  # N
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 1, 3, 0]  # O
]

    vertices = len(grafo_matriz)

    try:
        inicio_tempo = time.perf_counter()
        mst, custo_total = kruskal_matriz_adjacencia(grafo_matriz, vertices)
        fim_tempo = time.perf_counter()
        tempo_execucao_ms = (fim_tempo - inicio_tempo) * 1000

        print("arvore geradora minima:")
        for aresta in mst:
            print(f"vertice {aresta[0]} - vertice {aresta[1]} | custo = [{aresta[2]}]")
        print(f"custo total: {custo_total}")
        print(f"tempo de execucao: {tempo_execucao_ms:.5f} ms")
    except ValueError as e:
        print(f"(erro): {e}")
