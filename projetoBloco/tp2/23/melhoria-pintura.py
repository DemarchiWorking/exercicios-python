import time
import numpy as np
from functools import lru_cache


def contar_modos_otimizado(N, K):

    if N == 0 or K == 0:
        return 0
    if N == 1:
        return K

    anterior = np.ones(K, dtype=np.int64)
    atual = np.zeros(K, dtype=np.int64)

    for _ in range(1, N):
        total_anterior = np.sum(anterior)
        for j in range(K):
            atual[j] = total_anterior - anterior[j]
        anterior, atual = atual, anterior 

    return np.sum(anterior)


@lru_cache(maxsize=None)
def contar_modos_memoization(N, K):
    if N == 0 or K == 0:
        return 0
    if N == 1:
        return K
    if K == 1:
        return 0 if N > 1 else 1
    return (K - 1) * contar_modos_memoization(N - 1, K)


def benchmark():
    numeros_cadeiras = [5, 10, 25, 50, 100, 200, 500, 1000]
    K = 3

    print("Benchmarking...\n")
    print(f"{'N':<10} | {'Tempo (ms)':<15} | {'Resultado':<30} | {'Método':<20}")
    print("-" * 80)

    for N in numeros_cadeiras:
        start = time.perf_counter()
        res_otimizado = contar_modos_otimizado(N, K)
        end = time.perf_counter()
        tempo_otimizado = (end - start) * 1000

        tempo_memoization = 0
        res_memoization = 0
        if N <= 5000:
            start = time.perf_counter()
            res_memoization = contar_modos_memoization(N, K)
            end = time.perf_counter()
            tempo_memoization = (end - start) * 1000

        print(f"{N:<10} | {tempo_otimizado:<15.6f} | {res_otimizado:<30} | {'Otimizado (DP)'}")
        if N <= 5000:
            print(f"{'':<10} | {tempo_memoization:<15.6f} | {res_memoization:<30} | {'Memoizacao'}")


if __name__ == "__main__":
    benchmark()