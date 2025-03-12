import time

def exibir_heap(arr):
    inicio = time.perf_counter_ns()
    print("Heap como lista:", arr)
    fim = time.perf_counter_ns()
    print(f"Tempo para exibir a Heap: {(fim - inicio) / 1_000_000:.6f} ms")

def heapify_down(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify_down(arr, n, maior)

def heapify_up(arr, i):
    pai = (i - 1) // 2
    if i > 0 and arr[i] > arr[pai]:
        arr[i], arr[pai] = arr[pai], arr[i]
        heapify_up(arr, pai)

def criar_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        heapify_down(arr, n, i)
    return arr

def inserir_na_heap(arr, elemento):
    arr.append(elemento)
    heapify_up(arr, len(arr) - 1)

def criar_min_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        heapify_down_min(arr, n, i)
    return arr

def heapify_down_min(arr, n, i):
    menor = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[esquerda] < arr[menor]:
        menor = esquerda

    if direita < n and arr[direita] < arr[menor]:
        menor = direita

    if menor != i:
        arr[i], arr[menor] = arr[menor], arr[i]
        heapify_down_min(arr, n, menor)

lista = [20, 33, 17, 25, 15]
print("Original:", lista)

inicio = time.perf_counter_ns()
criar_heap(lista)
fim = time.perf_counter_ns()
print("MaxHeap:", lista)
print(f"Criando Max-Heap em  {(fim - inicio) / 1_000_000:.6f} ms")

inicio = time.perf_counter_ns()
inserir_na_heap(lista, 30)
fim = time.perf_counter_ns()
print("MaxHeap após inserção:", lista)
print(f"Inserir na Max-Heap em {(fim - inicio) / 1_000_000:.6f} ms")

exibir_heap(lista)

inicio = time.perf_counter_ns()
criar_min_heap(lista)
fim = time.perf_counter_ns()
print("MinHeap:", lista)
print(f"Criando a Min-Heap em {(fim - inicio) / 1_000_000:.6f} ms")
