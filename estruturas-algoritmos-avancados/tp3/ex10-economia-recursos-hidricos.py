import heapq

def algoritmo_prim(grafo, bairro_inicial):
    arvore_geradora_minima = []
    visitados = set()
    fila_prioridade = [(0, bairro_inicial, None)]
    custo_total = 0

    while fila_prioridade:
        custo, bairro_atual, bairro_anterior = heapq.heappop(fila_prioridade)

        if bairro_atual in visitados:
            continue

        visitados.add(bairro_atual)
        custo_total += custo

        if bairro_anterior is not None:
            arvore_geradora_minima.append((bairro_anterior, bairro_atual, custo))

        for vizinho, custo_conexao in grafo[bairro_atual]:
            if vizinho not in visitados:
                heapq.heappush(fila_prioridade, (custo_conexao, vizinho, bairro_atual))

    return arvore_geradora_minima, custo_total

grafo = {
    'Pinheiros': [('Vila Madalena', 3), ('Morumbi', 7)],
    'Vila Madalena': [('Pinheiros', 3), ('Butantã', 2), ('Morumbi', 6)],
    'Butantã': [('Vila Madalena', 2), ('Morumbi', 5)],
    'Morumbi': [('Pinheiros', 7), ('Vila Madalena', 6), ('Butantã', 5)]
}

bairro_inicial = 'Pinheiros'
arvore, custo_total = algoritmo_prim(grafo, bairro_inicial)

print("Melhor plano de instalação (Árvore Geradora Mínima):")
for conexao in arvore:
    print(f"{conexao[0]} - {conexao[1]} (custo: {conexao[2]})")
print(f"Custo total do sistema: {custo_total}")
