from time import perf_counter
from itertools import combinations

lojas = {'L1', 'L2', 'L3', 'L4'}
armazens = {
    'A1': {'custo': 50, 'cobre': {'L1', 'L2'}},
    'A2': {'custo': 60, 'cobre': {'L2', 'L3'}},
    'A3': {'custo': 80, 'cobre': {'L3', 'L4'}}
}

def exact_set_cover(lojas, armazens):
    start_time = perf_counter()

    armazens_names = list(armazens.keys())
    melhor_custo = float('inf')
    melhor_combinacao = None

    for r in range(1, len(armazens_names) + 1):
        for combinacao in combinations(armazens_names, r):
            lojas_cobertas = set()
            custo_total = 0

            for armazem in combinacao:
                lojas_cobertas.update(armazens[armazem]['cobre'])
                custo_total += armazens[armazem]['custo']

            if lojas_cobertas >= lojas and custo_total < melhor_custo:
                melhor_custo = custo_total
                melhor_combinacao = combinacao

    end_time = perf_counter()

    tempo_execucao_ms = (end_time - start_time) * 1000
    print(f"tempo total de execucao: {tempo_execucao_ms:.6f} ms")

    return melhor_combinacao, melhor_custo

combinacao, custo = exact_set_cover(lojas, armazens)

if combinacao:
    print(f"armazens escolhidos: {combinacao}")
    print(f"custo total: {custo}")
    print("solucao encontrada: todas cobertas!")
else:
    print("nao foi possivel encontrar uma solução exata.")
