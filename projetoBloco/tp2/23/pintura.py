import time


def contar_modos(N, K):
    if N == 0:
        return 0
    if K == 0:
        return 0

    dp = [[0 for _ in range(K)] for _ in range(N)]
    for j in range(K):
        dp[0][j] = 1

    for i in range(1, N):
        for j in range(K):
            dp[i][j] = sum(dp[i - 1][m] for m in range(K) if m != j)

    return sum(dp[N - 1])


# Lista dos diferentes valores de N
numeros_cadeiras = [5, 10, 25, 50, 100, 200, 500, 1000, 5000]
K = 3  # Número de cores

# Medir e imprimir o tempo de execução para cada valor de N
for N in numeros_cadeiras:
    inicio = time.perf_counter()
    resultado = contar_modos(N, K)
    fim = time.perf_counter()
    tempo = (fim - inicio) * 1000  # Converter para milissegundos
    print(f"Quantidade de cadeiras: {N}, Tempo de execução: {tempo:.10f} ms, Número de maneiras: {resultado}")
