def bubble_sort_alfabetico(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def exec_bubble_sort_alfabetico():
    test_cases = [
        ["antonio", "felipe", "rodrigo", "bianca"],
        ["lorena", "andre", "tati", "dalvo"],
        ["carlos", "elias", "isis", "joao"],
    ]

    for i, input in enumerate(test_cases):
        sorted_list = bubble_sort_alfabetico(input.copy())
        print(f"Item {i + 1} - Lista: [{input}] > Ordenado: [{sorted_list}]")


exec_bubble_sort_alfabetico()
