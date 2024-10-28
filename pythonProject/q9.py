def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Testando a função com diferentes listas
def testando_bubble_sort():
    lista = [
        [38, 27, 43, 3, 9, 82, 10],
        [64, 34, 25, 12, 22, 11, 90],
        [12, 25, 3 ,5, 11, 4, 2],
    ]

    for i, input in enumerate(lista):
        ordem = bubble_sort(input.copy())
        print(f"Item {i + 1} - Lista= [{input}]> Ordenada: [{ordem}]")

testando_bubble_sort()