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


def buscar_na_heap(arr, valor, is_max_heap=True):
    inicio = time.perf_counter_ns()

    def buscar_recursivo(arr, indice, n, valor, is_max_heap):

        if indice >= n:
            return False


        atual = arr[indice]

        if atual == valor:
            return True

        if is_max_heap and atual < valor:
            return False

        if not is_max_heap and atual > valor:
            return False

        esquerda = 2 * indice + 1
        direita = 2 * indice + 2
        return (esquerda < n and buscar_recursivo(arr, esquerda, n, valor, is_max_heap)) or \
            (direita < n and buscar_recursivo(arr, direita, n, valor, is_max_heap))

    resultado = buscar_recursivo(arr, 0, len(arr), valor, is_max_heap)
    fim = time.perf_counter_ns()
    print(f"Tempo para buscar {valor} na Heap: {(fim - inicio) / 1_000_000:.6f} ms")
    return resultado



lista = [20, 33, 17, 25, 15]
print("Original:", lista)


inicio = time.perf_counter_ns()
criar_heap(lista)
fim = time.perf_counter_ns()
#print("MaxHeap:", lista)
#print(f"Criando Max-Heap em  {(fim - inicio) / 1_000_000:.6f} ms")


inicio = time.perf_counter_ns()
inserir_na_heap(lista, 30)
fim = time.perf_counter_ns()
#print("MaxHeap após inserção:", lista)
#print(f"Inserir na Max-Heap em {(fim - inicio) / 1_000_000:.6f} ms")

exibir_heap(lista)

print("\nBusca na Max-Heap:")
print("Buscando 25:", buscar_na_heap(lista, 25, is_max_heap=True))
print("Buscando 50:", buscar_na_heap(lista, 50, is_max_heap=True))


inicio = time.perf_counter_ns()
criar_min_heap(lista)
fim = time.perf_counter_ns()
print("\nMinHeap:", lista)
print(f"Criando a Min-Heap em {(fim - inicio) / 1_000_000:.6f} ms")


print("\nBusca na Min-Heap:")
print("Buscando 15:", buscar_na_heap(lista, 15, is_max_heap=False))
print("Buscando 10:", buscar_na_heap(lista, 10, is_max_heap=False))