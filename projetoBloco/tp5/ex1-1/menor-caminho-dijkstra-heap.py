import heapq
import timeit
#dijksta
def calcular_menores_caminhos(grafo, origem):
    if origem not in grafo:
        raise ValueError("parametro não está no grafo.")

    def executar_algoritmo():
        distancias = {vertice: float('inf') for vertice in grafo}
        distancias[origem] = 0
        predecessores = {}

        heap = [(0, origem)]

        while heap:
            distancia_atual, vertice_atual = heapq.heappop(heap)

            if distancia_atual > distancias[vertice_atual]:
                continue

            for vizinho, peso in grafo[vertice_atual]:
                nova_distancia = distancia_atual + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = vertice_atual
                    heapq.heappush(heap, (nova_distancia, vizinho))

        return distancias, predecessores

    tempo_total = timeit.timeit(executar_algoritmo, number=1)
    print(f"Tempo total de execução: {tempo_total:.6f} segundos")

    distancias, predecessores = executar_algoritmo()
    return distancias, predecessores

def mostrar_resultado(distancias, origem):
    print(f"distancia menor a partir de {origem}:")
    for vertice, distancia in distancias.items():
        print(f"distancia ate {vertice}: {distancia}")
grafo = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)],
}

#grafo = {
#    "A": [("B", 2), ("C", 5)],
#    "B": [("A", 2), ("D", 4)],
#    "C": [("A", 5), ("D", 1), ("E", 7)],
#    "D": [("B", 4), ("C", 1), ("E", 3)],
#    "E": [("C", 7), ("D", 3)]
#}

origem = "A"
try:
    distancias, predecessores = calcular_menores_caminhos(grafo, origem)
    mostrar_resultado(distancias, origem)
except ValueError as e:
    print(e)
