#Exercício 2.2 – Multiplicação de Matrizes com Paralelismo
#Descrição: Utilize o módulo multiprocessing para paralelizar a multiplicação de duas matrizes pequenas, dividindo o cálculo por linhas.
#Exemplo: Multiplique duas matrizes 3×3 e exiba a matriz resultante.

import multiprocessing

def multiplicar_fila(parametros):
    """Multiplica uma fila da primeira matriz por todas as colunas da segunda matriz.
    parametros (tuple): Uma tupla contendo a fila da matriz A, a matriz B e o índice da fila.
    Retorna: list: Uma lista com o resultado da multiplicação da fila."""
    fila_a, matriz_b, fila_idx = parametros
    num_colunas_b = len(matriz_b[0])
    fila_resultado = [0] * num_colunas_b
    for j in range(num_colunas_b):
        fila_resultado[j] = sum(fila_a[k] * matriz_b[k][j] for k in range(len(fila_a)))
    return fila_idx, fila_resultado


def multiplicar_matrizes(matriz_a, matriz_b):
    """Multiplica duas matrizes utilizando processamento paralelo.
    Parâmetros:
    matriz_a (list): A primeira matriz.
    matriz_b (list): A segunda matriz.
    Retorna:
    list: A matriz resultante da multiplicação."""
    num_filas_a = len(matriz_a)
    num_filas_b = len(matriz_b)
    num_colunas_b = len(matriz_b[0])

    if len(matriz_a[0]) != num_filas_b:
        raise ValueError("O número de colunas da A deve ser igual ao número de filas de B.")

    with multiprocessing.Pool() as pool:
        parametros = [(matriz_a[i], matriz_b, i) for i in range(num_filas_a)]
        resultados = pool.map(multiplicar_fila, parametros)

    # Organizar os resultados pela ordem das filas
    matriz_resultante = [None] * num_filas_a
    for fila_idx, fila_resultado in resultados:
        matriz_resultante[fila_idx] = fila_resultado

    return matriz_resultante


if __name__ == "__main__":
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

    resultante = multiplicar_matrizes(matriz_a, matriz_b)
    print("Resposta - Matriz:")
    for res in resultante:
        print(res)
