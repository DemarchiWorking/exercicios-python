import multiprocessing
import time


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


def testar_desempenho(matriz_a, matriz_b, n_execucoes=10):
    """Testa o desempenho das implementações sequencial e paralela."""
    print("Testando desempenho...\n")

    # Teste sequencial
    tempos_seq = []
    for _ in range(n_execucoes):
        inicio = time.perf_counter()
        resultado_seq = multiplicar_matrizes_sequencial(matriz_a, matriz_b)
        fim = time.perf_counter()
        tempos_seq.append(fim - inicio)

    # Teste paralelo
    tempos_par = []
    for _ in range(n_execucoes):
        inicio = time.perf_counter()
        resultado_par = multiplicar_matrizes_paralelo(matriz_a, matriz_b)
        fim = time.perf_counter()
        tempos_par.append(fim - inicio)

    # Verificar se os resultados são iguais
    assert resultado_seq == resultado_par, "Resultados diferentes entre as implementações!"

    # Calcular estatísticas
    media_seq = sum(tempos_seq) / n_execucoes
    media_par = sum(tempos_par) / n_execucoes

    print(f"Tempo médio sequencial: {media_seq:.6f} segundos")
    print(f"Tempo médio paralelo:   {media_par:.6f} segundos")
    print(
        f"Diferença: {((media_seq - media_par) / media_seq) * 100:.2f}% mais {'rápido' if media_par < media_seq else 'lento'}")
    print(f"\nMelhor tempo sequencial: {min(tempos_seq):.6f} segundos")
    print(f"Melhor tempo paralelo:   {min(tempos_par):.6f} segundos")


if __name__ == "__main__":
    # Matrizes de exemplo
    matriz_a = [
        [4, 3, 0],
        [2, 5, 2],
        [4, -2, 3]
    ]

    matriz_b = [
        [-5, -5, 0],
        [-2, 5, 0],
        [-5, 2, -3]
    ]

    # Executar uma única vez para mostrar o resultado
    print("Resultado da multiplicação:")
    resultado = multiplicar_matrizes_sequencial(matriz_a, matriz_b)
    for linha in resultado:
        print(linha)

    # Testar desempenho com múltiplas execuções
    print("\n" + "=" * 50 + "\n")
    testar_desempenho(matriz_a, matriz_b)