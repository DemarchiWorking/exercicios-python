def busca_linear(arr, x):
    for i in range(len(arr)):
        print(f"Comparando {arr[i]} com {x}")
        if arr[i] == x:
            return i
    return -1

arr = [2, 4, 6, 8, 10, 12, 13]

x = 8

resultado = busca_linear(arr, x)