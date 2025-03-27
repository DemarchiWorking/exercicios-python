import timeit

#djikstra
def calcular_menores_caminhos(grafo, origem):
    def executar_algoritmo():
        distancias = {vertice: float('inf') for vertice in grafo}
        distancias[origem] = 0
        predecessores = {}

        nao_visitados = set(grafo.keys())

        while nao_visitados:
            vertice_atual = min(
                nao_visitados, key=lambda vertice: distancias[vertice]
            )

            if distancias[vertice_atual] == float('inf'):
                break

            for vizinho, peso in grafo[vertice_atual]:
                nova_distancia = distancias[vertice_atual] + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = vertice_atual

            nao_visitados.remove(vertice_atual)

        return distancias, predecessores

    tempo_total = timeit.timeit(executar_algoritmo, number=1)
    print(f"Tempo total de execução: {tempo_total:.6f} segundos")

    distancias, predecessores = executar_algoritmo()
    return distancias, predecessores

def mostrar_resultado(distancias, origem):
    print(f"distancia menor a começando de {origem} :")
    for vertice, distancia in distancias.items():
        print(f"distancia ate {vertice} - {distancia}")

grafo = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)],
}

origem = "A"
distancias, predecessores = calcular_menores_caminhos(grafo, origem)
mostrar_resultado(distancias, origem)
