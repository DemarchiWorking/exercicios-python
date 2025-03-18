import heapq

def algoritmo_prim(grafo, cidade_inicial):
    arvore_geradora_minima = []
    cidades_visitadas = set()
    fila_prioridade = [(0, cidade_inicial, None)]
    custo_total = 0

    while fila_prioridade:
        custo, cidade_atual, cidade_anterior = heapq.heappop(fila_prioridade)

        if cidade_atual in cidades_visitadas:
            continue

        cidades_visitadas.add(cidade_atual)
        custo_total += custo

        if cidade_anterior is not None:
            arvore_geradora_minima.append((cidade_anterior, cidade_atual, custo))

        for vizinho, custo_conexao in grafo[cidade_atual]:
            if vizinho not in cidades_visitadas:
                heapq.heappush(fila_prioridade, (custo_conexao, vizinho, cidade_atual))

    return arvore_geradora_minima, custo_total

grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 7)],
    'C': [('A', 2), ('B', 1), ('D', 3)],
    'D': [('B', 7), ('C', 3)]
}

cidade_inicial = 'A'
arvore, custo_total = algoritmo_prim(grafo, cidade_inicial)

print("Árvore Geradora Mínima (conexões mais econômicas):")
for conexao in arvore:
    print(f"{conexao[0]} - {conexao[1]} (custo: {conexao[2]})")

print(f"Custo Total da Rede Elétrica: {custo_total}")
