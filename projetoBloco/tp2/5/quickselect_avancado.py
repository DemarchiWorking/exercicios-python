import random
import time


def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))


def encontrar_mediana(arr):
    n = len(arr)
    if n % 2 == 1:
        return quickselect(arr, n // 2)
    else:
        return (quickselect(arr, n // 2 - 1) + quickselect(arr, n // 2)) / 2


def encontrar_k_menores(arr, k):
    menores = []
    for i in range(k):
        menores.append(quickselect(arr, i))
    return sorted(menores)


def gerar_lista():
    return [random.randint(1, 1000) for _ in range(1000)]


def testar_quickselect():
    listas = [gerar_lista() for _ in range(10)]
    k_values = [10, 50, 100, 500, 999]

    for i, lista in enumerate(listas):
        print(f"Teste {i + 1}:")

        start_time = time.time()
        mediana = encontrar_mediana(lista)
        end_time = time.time()
        print(f"  Mediana: {mediana}, Tempo: {end_time - start_time} segundos")

        for k in k_values:
            start_time = time.time()
            menores = encontrar_k_menores(lista, k)
            end_time = time.time()
            print(f"  k={k} menores elementos: {menores[:10]}..., Tempo: {end_time - start_time} segundos")


if __name__ == "__main__":
    testar_quickselect()
