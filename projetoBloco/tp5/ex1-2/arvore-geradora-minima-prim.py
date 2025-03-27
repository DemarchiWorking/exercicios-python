import timeit

def calcular_arvore_geradora_minima(grafo, vertice_inicial):
    mst = []
    visitados = set()
    arestas_possiveis = []
    custo_total = 0

    visitados.add(vertice_inicial)

    for vizinho, peso in grafo[vertice_inicial]:
        arestas_possiveis.append((peso, vertice_inicial, vizinho))

    while arestas_possiveis:
        arestas_possiveis.sort(key=lambda x: x[0])
        peso, origem, destino = arestas_possiveis.pop(0)

        if destino not in visitados:
            visitados.add(destino)
            custo_total += peso
            mst.append((origem, destino, peso))

            for vizinho, peso_vizinho in grafo[destino]:
                if vizinho not in visitados:
                    arestas_possiveis.append((peso_vizinho, destino, vizinho))

    return mst, custo_total

grafo = {
    "A": [("B", 2), ("C", 3)],
    "B": [("A", 2), ("C", 1), ("D", 4)],
    "C": [("A", 3), ("B", 1), ("D", 5)],
    "D": [("B", 4), ("C", 5)],
}

vertice_inicial = "A"

def executar_para_tempo():
    calcular_arvore_geradora_minima(grafo, vertice_inicial)

tempo_ms = timeit.timeit(executar_para_tempo, number=1) * 1000

mst, custo_total = calcular_arvore_geradora_minima(grafo, vertice_inicial)

print("arvore geradora minima:")
for origem, destino, peso in mst:
    print(f"a orgigem = {origem} - O destino = {destino} com peso = {peso}")
print(f"custo: {custo_total}")
print(f"tempo medio de execucao: {tempo_ms:.2f} ms")
