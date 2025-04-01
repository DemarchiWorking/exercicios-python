import itertools
import time

def held_karp(distances):
    n = len(distances)
    C = {}
    num_operations = 0
    start_time = time.perf_counter()

    for k in range(1, n):
        C[(1 << k, k)] = (distances[0][k], 0)
        num_operations += 1

    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
                num_operations += 1
            for k in subset:
                prev_bits = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == k:
                        continue
                    if (prev_bits, m) in C:
                        res.append((C[(prev_bits, m)][0] + distances[m][k], m))
                        num_operations += 1
                if res:
                    C[(bits, k)] = min(res)
                else:
                    C[(bits, k)] = (float('inf'), None)
                num_operations += 1

    bits = (2 ** n - 1) - 1
    res = []
    for k in range(1, n):
        if (bits, k) in C:
            res.append((C[(bits, k)][0] + distances[k][0], k))
            num_operations += 1
    if not res:
        raise ValueError("nao consegui calcular o caminho.")
    opt, parent = min(res)

    path = []
    visited = 1
    curr_bits = bits
    curr_parent = parent

    for _ in range(n - 1):
        path.append(curr_parent)
        visited |= 1 << curr_parent
        next_bits = curr_bits & ~(1 << curr_parent)
        if next_bits == 0:
            break
        possible_next = []
        for m in range(1, n):
            if (next_bits, m) in C and (visited & (1 << m)) == 0:
                possible_next.append((C[(next_bits, m)][0] + distances[m][curr_parent], m))
                num_operations += 1
        if not possible_next:
            raise ValueError(f"(erro) reconstruir o caminho. bits: {next_bits}, parent: {curr_parent}")
        _, curr_parent = min(possible_next)
        curr_bits = next_bits
        num_operations += 1

    path.append(0)
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000

    return opt, list(reversed(path)), execution_time_ms, num_operations

def comparar_solucoes(matriz_distancias):
    print("xxx Held-Karp xxx")
    custo_exato, caminho_exato, tempo_ms, num_operacoes = held_karp(matriz_distancias)
    print("custo otimo =", custo_exato)
    print("Caminho otimo =", caminho_exato)
    print(f"tempo de execucao: {tempo_ms:.5f} ms")
    print("numero total de operacoes =", num_operacoes)

distancias = [
    [0, 10, 15, 20], #1
    [10, 0, 35, 25], #2
    [15, 35, 0, 30], #3
    [20, 25, 30, 0]  #4
]
#distancias = [
#    [0, 10, 15, 20, 25, 30, 35],
#    [10, 0, 35, 25, 30, 40, 45],
#    [15, 35, 0, 30, 20, 50, 60],
#    [20, 25, 30, 0, 15, 10, 70],
#    [25, 30, 20, 15, 0, 35, 80],
#    [30, 40, 50, 10, 35, 0, 90],
#    [35, 45, 60, 70, 80, 90, 0]
#]

comparar_solucoes(distancias)
