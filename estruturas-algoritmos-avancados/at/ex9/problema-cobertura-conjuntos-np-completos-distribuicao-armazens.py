from time import perf_counter

lojas = {'L1', 'L2', 'L3', 'L4'}
armazens = {
    'A1': {'custo': 50, 'cobre': {'L1', 'L2'}},
    'A2': {'custo': 60, 'cobre': {'L2', 'L3'}},
    'A3': {'custo': 80, 'cobre': {'L3', 'L4'}}
}

def greedy_set_cover(lojas, armazens):
    lojas_nao_cobertas = lojas.copy()
    armazens_escolhidos = []
    custo_total = 0

    start_time = perf_counter()

    while lojas_nao_cobertas:
        melhor_armazem = None
        melhor_custo_por_loja = float('inf')

        for nome, info in armazens.items():
            if nome not in armazens_escolhidos:
                lojas_cobertas = info['cobre'] & lojas_nao_cobertas
                if lojas_cobertas:
                    custo = info['custo']
                    custo_por_loja = custo / len(lojas_cobertas)
                    if custo_por_loja < melhor_custo_por_loja:
                        melhor_custo_por_loja = custo_por_loja
                        melhor_armazem = nome

        if melhor_armazem:
            armazens_escolhidos.append(melhor_armazem)
            custo_total += armazens[melhor_armazem]['custo']
            lojas_nao_cobertas -= armazens[melhor_armazem]['cobre']
        else:
            print("nao foi possivel cobrir todas as lojas!")
            break

    end_time = perf_counter()

    tempo_execucao_ms = (end_time - start_time) * 1000
    print(f"tempo total de execucao: {tempo_execucao_ms:.6f} ms")

    return armazens_escolhidos, custo_total, lojas_nao_cobertas

escolhidos, custo, nao_cobertas = greedy_set_cover(lojas, armazens)

print(f"armazens escolhidos: {escolhidos}")
print(f"custo total: {custo}")
print(f"lojas nao cobertas: {nao_cobertas}")
if not nao_cobertas:
    print("solucao encontrada: todas as lojas foram cobertas!")
else:
    print("solucao incompleta: algumas lojas n foram cobertas.")
