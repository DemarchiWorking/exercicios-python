import random


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


def gerar_lista():
    return [random.randint(1, 1000) for _ in range(10000)]


def testar_quickselect():
    k_values = [10, 100, 1000, 5000, 9999]
    for i in range(10):
        lista = gerar_lista()
        print(f"Teste {i + 1}:")
        for k in k_values:
            result = quickselect(lista, k)
            print(f"  k={k}: {result}")


if __name__ == "__main__":
    testar_quickselect()
