import heapq
from collections import deque
import time

def grafo_conexo(grafo, no_inicial):
    visitados = set()
    fila = deque([no_inicial])

    while fila:
        no_atual = fila.popleft()
        if no_atual not in visitados:
            visitados.add(no_atual)
            for vizinho, _ in grafo[no_atual]:
                if vizinho not in visitados:
                    fila.append(vizinho)

    return len(visitados) == len(grafo)


def algoritmo_prim(grafo, no_inicial):
    if not grafo_conexo(grafo, no_inicial):
        raise ValueError("O grafo fornecido nao e conexo. Nao e possível formar uma arvore geradora minima.")

    mst = []
    visitados = set()
    fila_prioridade = [(0, no_inicial, None)]  # (custo, nó atual, nó anterior)
    custo_total = 0

    while fila_prioridade:
        custo, no_atual, no_anterior = heapq.heappop(fila_prioridade)

        if no_atual in visitados:
            continue

        visitados.add(no_atual)
        custo_total += custo

        if no_anterior is not None:
            mst.append((no_anterior, no_atual, custo))

        for vizinho, custo_aresta in grafo[no_atual]:
            if vizinho not in visitados:
                heapq.heappush(fila_prioridade, (custo_aresta, vizinho, no_atual))

    return mst, custo_total


if __name__ == "__main__":
#    grafo = {
#        'A': [('B', 2), ('C', 3)],
#        'B': [('A', 2), ('C', 1), ('D', 4)],
#        'C': [('A', 3), ('B', 1)],
#        'D': [('B', 4)]
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

    no_inicial = 'A'
    try:
        inicio_tempo = time.perf_counter()
        mst, custo_total = algoritmo_prim(grafo, no_inicial)
        fim_tempo = time.perf_counter()
        tempo_execucao_ms = (fim_tempo - inicio_tempo) * 1000  # Tempo em milissegundos

        print("arvore geradora minima:")
        for aresta in mst:
            print(f"{aresta[0]} - {aresta[1]} | custo = [{aresta[2]}]")
        print(f"custo total: {custo_total}")
        print(f"Tempo de execução: {tempo_execucao_ms:.5f} ms")
    except ValueError as e:
        print(f"(erro): {e}")
