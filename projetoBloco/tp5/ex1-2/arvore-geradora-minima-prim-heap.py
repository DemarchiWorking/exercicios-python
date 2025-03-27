import timeit
import heapq

def calcular_arvore_geradora_minima(grafo, vertice_inicial):
    mst = []
    visitados = set()
    fila_prioridade = [(0, vertice_inicial, None)]
    custo_total = 0

    while fila_prioridade:
        peso, vertice_atual, vertice_anterior = heapq.heappop(fila_prioridade)

        if vertice_atual in visitados:
            continue

        visitados.add(vertice_atual)
        custo_total += peso

        if vertice_anterior is not None:
            mst.append((vertice_anterior, vertice_atual, peso))

        for vizinho, peso_aresta in grafo[vertice_atual]:
            if vizinho not in visitados:
                heapq.heappush(fila_prioridade, (peso_aresta, vizinho, vertice_atual))

    return mst, custo_total

grafo = {
    "A": [("B", 2), ("C", 3)],
    "B": [("A", 2), ("C", 1), ("D", 4)],
    "C": [("A", 3), ("B", 1), ("D", 5)],
    "D": [("B", 4), ("C", 5)]
}

vertice_inicial = "A"

def executar_algoritmo():
    mst, custo_total = calcular_arvore_geradora_minima(grafo, vertice_inicial)
    print("arvore geradora minima:")
    for origem, destino, peso in mst:
        print(f"a orgigem = {origem} - O destino = {destino} com peso = {peso}")
    print(f"custo: {custo_total}")

tempo_ms = timeit.timeit(lambda: calcular_arvore_geradora_minima(grafo, vertice_inicial), number=1) * 1000

executar_algoritmo()
print(f"tempo medio de execucao: {tempo_ms:.4f} ms")
