def quickselect(array, low, high, k):
    if low == high:
        return array[low]

    pivot_index = partition(array, low, high)

    if k == pivot_index:
        return array[k]
    elif k < pivot_index:
        return quickselect(array, low, pivot_index - 1, k)
    else:
        return quickselect(array, pivot_index + 1, high, k)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

# Exemplo de uso
array = [3, 2, 1, 5, 4]
k = 2
print(f"O {k + 1}-ésimo menor elemento é {quickselect(array, 0, len(array) - 1, k)}")
