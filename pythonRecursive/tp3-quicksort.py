def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[-1]

    menores = [x for x in array[:-1] if x <= pivot]
    maiores = [x for x in array[:-1] if x > pivot]

    return quicksort(menores) + [pivot] + quicksort(maiores)

array = [10, 7, 8, 9, 1, 5]
ordenado = quicksort(array)
print("Array ordenado:", ordenado)