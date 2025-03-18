import heapq

def algoritmo_prim(grafo, torre_inicial):
    arvore_geradora_minima = []
    visitados = set()
    fila_prioridade = [(0, torre_inicial, None)]
    custo_total = 0

    while fila_prioridade:

        custo, torre_atual, torre_anterior = heapq.heappop(fila_prioridade)

        if torre_atual in visitados:
            continue

        visitados.add(torre_atual)
        custo_total += custo

        if torre_anterior is not None:
            arvore_geradora_minima.append((torre_anterior, torre_atual, custo))

        for vizinho, custo_conexao in grafo[torre_atual]:
            if vizinho not in visitados:
                heapq.heappush(fila_prioridade, (custo_conexao, vizinho, torre_atual))

    return arvore_geradora_minima, custo_total

grafo = {
    'Torre1': [('Torre2', 5), ('Torre3', 10)],
    'Torre2': [('Torre1', 5), ('Torre3', 4), ('Torre4', 8)],
    'Torre3': [('Torre1', 10), ('Torre2', 4), ('Torre4', 3)],
    'Torre4': [('Torre2', 8), ('Torre3', 3)]
}

torre_inicial = 'Torre1'
arvore, custo_total = algoritmo_prim(grafo, torre_inicial)

print("Melhor plano de expansão da infraestrutura (Árvore Geradora Mínima):")
for conexao in arvore:
    print(f"{conexao[0]} - {conexao[1]} (custo: {conexao[2]})")
print(f"Custo total do projeto: {custo_total}")
