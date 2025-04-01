import heapq
from collections import deque
import time

def matriz_para_lista_adjacencia(matriz, rotulos):
    grafo = {rotulo: [] for rotulo in rotulos}
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != 0:  # Há uma conexão entre os nós i e j
                grafo[rotulos[i]].append((rotulos[j], matriz[i][j]))
    return grafo


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
    fila_prioridade = [(0, no_inicial, None)]
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
#    matriz = [
#        [0, 2, 3, 0],  # A
#        [2, 0, 1, 4],  # B
#        [3, 1, 0, 0],  # C
#        [0, 4, 0, 0]   # D
#    ]


    matriz = [
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

    rotulos = ['A', 'B', 'C', 'D','E', 'F','G','H','I','J','K', 'L', 'M', 'N','O']

    grafo = matriz_para_lista_adjacencia(matriz, rotulos)

    no_inicial = 'A'

    try:
        inicio_tempo = time.perf_counter()

        mst, custo_total = algoritmo_prim(grafo, no_inicial)

        fim_tempo = time.perf_counter()
        tempo_execucao_ms = (fim_tempo - inicio_tempo) * 1000  # Tempo em milissegundos

        print("Arvore Geradora Minima:")
        for aresta in mst:
            print(f"{aresta[0]} - {aresta[1]} | custo = [{aresta[2]}]")
        print(f"Custo total: {custo_total}")
        print(f"Tempo de execução: {tempo_execucao_ms:.5f} ms")
    except ValueError as e:
        print(f"(Erro): {e}")
