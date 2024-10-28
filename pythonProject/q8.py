def cocktail_shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Mover o maior elemento para a direita
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Se nada foi trocado, então o array está ordenado
        if not swapped:
            break

        swapped = False

        # Reduzir o final pois o maior elemento já está na posição correta
        end -= 1

        # Mover o menor elemento para a esquerda
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        # Aumentar o início porque o menor elemento já está na posição correta
        start += 1

    return arr

# Testando a função com diferentes listas
def test_cocktail_shaker_sort():
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [38, 27, 43, 3, 9, 82, 10],
        [],
        [1],
        [2, 1]
    ]

    for i, test in enumerate(test_cases):
        sorted_list = cocktail_shaker_sort(test.copy())
        print(f"Teste {i + 1}: Original: {test} -> Ordenado: {sorted_list}")

test_cocktail_shaker_sort()