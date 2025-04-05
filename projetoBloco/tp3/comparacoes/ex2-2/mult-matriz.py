import multiprocessing
import time
import random


def gerar_matriz(tamanho, valor_max=10):
    """Gera uma matriz quadrada aleatória."""
    return [[random.randint(0, valor_max) for _ in range(tamanho)] for _ in range(tamanho)]


# Matrizes de exemplo pré-geradas
MATRIZES_A = {
    3: [[4, 3, 0], [2, 5, 2], [4, -2, 3]],
    9: gerar_matriz(9),
    12: gerar_matriz(12),
    24: gerar_matriz(24)
}

MATRIZES_B = {
    3: [[-5, -5, 0], [-2, 5, 0], [-5, 2, -3]],
    9: gerar_matriz(9),
    12: gerar_matriz(12),
    24: gerar_matriz(24)
}


def multiplicar_fila(parametros):
    """Função para multiplicação paralela de uma linha da matriz."""
    fila_a, matriz_b, fila_idx = parametros
    num_colunas_b = len(matriz_b[0])
    fila_resultado = [0] * num_colunas_b
    for j in range(num_colunas_b):
        fila_resultado[j] = sum(fila_a[k] * matriz_b[k][j] for k in range(len(fila_a)))
    return fila_idx, fila_resultado


def multiplicar_matrizes_paralelo(matriz_a, matriz_b):
    """Multiplicação de matrizes usando multiprocessing."""
    num_filas_a = len(matriz_a)
    num_filas_b = len(matriz_b)
    num_colunas_b = len(matriz_b[0])

    if len(matriz_a[0]) != num_filas_b:
        raise ValueError("O número de colunas da A deve ser igual ao número de filas de B.")

    with multiprocessing.Pool() as pool:
        parametros = [(matriz_a[i], matriz_b, i) for i in range(num_filas_a)]
        resultados = pool.map(multiplicar_fila, parametros)

    matriz_resultante = [None] * num_filas_a
    for fila_idx, fila_resultado in resultados:
        matriz_resultante[fila_idx] = fila_resultado

    return matriz_resultante


def multiplicar_matrizes_sequencial(matriz_a, matriz_b):
    """Multiplicação de matrizes usando abordagem sequencial."""
    num_filas_a = len(matriz_a)
    num_filas_b = len(matriz_b)
    num_colunas_b = len(matriz_b[0])

    if len(matriz_a[0]) != num_filas_b:
        raise ValueError("O número de colunas da A deve ser igual ao número de filas de B.")

    matriz_resultante = [[0 for _ in range(num_colunas_b)] for _ in range(num_filas_a)]

    for i in range(num_filas_a):
        for j in range(num_colunas_b):
            for k in range(num_filas_b):
                matriz_resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return matriz_resultante


def testar_desempenho(tamanho, n_execucoes=5):
    """Testa o desempenho para um tamanho específico de matriz."""
    matriz_a = MATRIZES_A[tamanho]
    matriz_b = MATRIZES_B[tamanho]

    print(f"\n{'=' * 50}")
    print(f"Testando matrizes {tamanho}x{tamanho}")
    print(f"{'=' * 50}")

    # Aquecimento (warm-up)
    multiplicar_matrizes_sequencial(MATRIZES_A[3], MATRIZES_B[3])
    multiplicar_matrizes_paralelo(MATRIZES_A[3], MATRIZES_B[3])

    # Teste sequencial
    inicio_seq = time.perf_counter()
    resultado_seq = multiplicar_matrizes_sequencial(matriz_a, matriz_b)
    tempo_seq = time.perf_counter() - inicio_seq

    # Teste paralelo
    inicio_par = time.perf_counter()
    resultado_par = multiplicar_matrizes_paralelo(matriz_a, matriz_b)
    tempo_par = time.perf_counter() - inicio_par

    # Verificar resultados
    assert resultado_seq == resultado_par, "Resultados diferentes entre as implementações!"

    # Exibir resultados
    print(f"\nTempo sequencial: {tempo_seq:.6f} segundos")
    print(f"Tempo paralelo:   {tempo_par:.6f} segundos")

    if tempo_seq > 0:
        diferenca = ((tempo_seq - tempo_par) / tempo_seq) * 100
        print(f"Diferença: {diferenca:.2f}% mais {'rápido' if tempo_par < tempo_seq else 'lento'}")
    else:
        print("Diferença: Tempo sequencial muito rápido para calcular porcentagem")


if __name__ == "__main__":
    print("Comparação de desempenho: Multiplicação de Matrizes")
    print("Sequencial vs Paralelo\n")

    # Testar para todos os tamanhos de matriz
    for tamanho in [3, 9, 12, 24]:
        testar_desempenho(tamanho)

    print("\nTestes concluídos!")