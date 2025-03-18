import heapq
from collections import defaultdict


def dijkstra_modificado(grafo, inicio, destino, autonomia, estacoes_recarga):
    tempos = {inicio: 0}
    distancias = {inicio: 0}
    caminhos = {inicio: [inicio]}
    visitados = set()

    fila = [(0, inicio, 0)]

    while fila:
        tempo_atual, vertice_atual, dist_atual = heapq.heappop(fila)

        if vertice_atual in visitados:
            continue

        visitados.add(vertice_atual)

        if vertice_atual == destino:
            return tempos[vertice_atual], caminhos[vertice_atual]

        for vizinho, (tempo, distancia) in grafo[vertice_atual].items():
            if vizinho in visitados:
                continue

            nova_dist = dist_atual + distancia

            if nova_dist > autonomia:
                if vertice_atual not in estacoes_recarga:
                    continue
                nova_dist = distancia

            novo_tempo = tempo_atual + tempo

            if vizinho not in tempos or novo_tempo < tempos[vizinho]:
                tempos[vizinho] = novo_tempo
                distancias[vizinho] = nova_dist
                caminhos[vizinho] = caminhos[vertice_atual] + [vizinho]
                heapq.heappush(fila, (novo_tempo, vizinho, nova_dist))

    return None, None


def main():
    grafo = {
        'A': {'B': (4, 10), 'C': (10, 20)},
        'B': {'A': (4, 10), 'D': (8, 15), 'E': (10, 30)},
        'C': {'A': (10, 20), 'D': (5, 10)},
        'D': {'B': (8, 15), 'C': (5, 10), 'E': (2, 10)},
        'E': {'B': (10, 30), 'D': (2, 10)}
    }

    estacoes_recarga = {'B', 'D'}

    inicio = 'A'
    destino = 'E'
    autonomia = 25

    tempo_total, caminho = dijkstra_modificado(grafo, inicio, destino, autonomia, estacoes_recarga)

    if caminho:
        print(f"Menor tempo: {tempo_total} unidades de tempo")
        print(f"Caminho: {' -> '.join(caminho)}")
        print(f"Recargas necessárias em: {[v for v in caminho if v in estacoes_recarga and v != inicio]}")
    else:
        print("Não há caminho viável com a autonomia fornecida.")


if __name__ == "__main__":
    main()