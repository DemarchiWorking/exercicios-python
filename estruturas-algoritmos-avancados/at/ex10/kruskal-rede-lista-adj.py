import heapq
from collections import defaultdict
import time

def kruskal(grafo):
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
    for no in grafo:
        for vizinho, custo in grafo[no]:
            arestas.append((custo, no, vizinho))
    arestas.sort()

    parent = {no: no for no in grafo}
    rank = {no: 0 for no in grafo}

    mst = []
    custo_total = 0

    for custo, no1, no2 in arestas:
        if find(no1) != find(no2):
            union(no1, no2)
            mst.append((no1, no2, custo))
            custo_total += custo

    return mst, custo_total

if __name__ == "__main__":
#    grafo = {
#        'A': [('B', 2), ('C', 3)],
#        'B': [('A', 2), ('C', 1), ('D', 4)],
#        'C': [('A', 3), ('B', 1)],
#       'D': [('B', 4)]
#    }
    grafo = {
    'A': [('B', 2), ('C', 3), ('D', 6), ('E', 5)],
    'B': [('A', 2), ('C', 8), ('D', 4), ('F', 7)],
    'C': [('A', 3), ('B', 8), ('E', 1), ('G', 9)],
    'D': [('A', 6), ('B', 4), ('F', 3), ('H', 2)],
    'E': [('A', 5), ('C', 1), ('G', 4), ('I', 7)],
    'F': [('B', 7), ('D', 3), ('H', 6), ('J', 8)],
    'G': [('C', 9), ('E', 4), ('I', 2), ('K', 1)],
    'H': [('D', 2), ('F', 6), ('J', 5), ('L', 8)],
    'I': [('E', 7), ('G', 2), ('K', 3), ('M', 5)],
    'J': [('F', 8), ('H', 5), ('L', 4), ('N', 7)],
    'K': [('G', 1), ('I', 3), ('M', 2), ('O', 4)],
    'L': [('H', 8), ('J', 4), ('N', 6)],
    'M': [('I', 5), ('K', 2), ('O', 1)],
    'N': [('J', 7), ('L', 6), ('O', 3)],
    'O': [('K', 4), ('M', 1), ('N', 3)]
}


try:
    inicio_tempo = time.perf_counter()
    mst, custo_total = kruskal(grafo)
    fim_tempo = time.perf_counter()
    tempo_execucao_ms = (fim_tempo - inicio_tempo) * 1000

    print("arvore geradora minima:")
    for aresta in mst:
        print(f"{aresta[0]} - {aresta[1]} | custo = [{aresta[2]}]")
    print(f"custo total: {custo_total}")
    print(f"tempo de execucao: {tempo_execucao_ms:.5f} ms")
except ValueError as e:
    print(f"(erro): {e}")
