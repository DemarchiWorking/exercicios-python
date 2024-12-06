def mochila(valores, pesos, capacidade):
    n = len(valores)
    dp = [[0 for peso_atual in range(capacidade + 1)] for item_atual in range(n + 1)]

    for i in range(1, n + 1):
        for peso_atual in range(1, capacidade + 1):
            if pesos[i-1] <= peso_atual:
                dp[i][peso_atual] = max(dp[i-1][peso_atual], dp[i-1][peso_atual-pesos[i-1]] + valores[i-1])
            else:
                dp[i][peso_atual] = dp[i-1][peso_atual]

    return dp[n][capacidade]

valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidade = 50

maximo = mochila(valores, pesos, capacidade)
print("Máximo a ser carregado:", maximo)
