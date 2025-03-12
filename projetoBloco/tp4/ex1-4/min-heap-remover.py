import time

def ajustar_descendo_para_menor(matriz, tamanho, indice):
    menor_indice = indice
    filho_esquerdo = 2 * indice + 1
    filho_direito = 2 * indice + 2

    if filho_esquerdo < tamanho and matriz[filho_esquerdo] < matriz[menor_indice]:
        menor_indice = filho_esquerdo

    if filho_direito < tamanho and matriz[filho_direito] < matriz[menor_indice]:
        menor_indice = filho_direito

    if menor_indice != indice:
        matriz[indice], matriz[menor_indice] = matriz[menor_indice], matriz[indice]
        ajustar_descendo_para_menor(matriz, tamanho, menor_indice)

def criar_heap_menor(matriz):
    for i in range((len(matriz) - 2) // 2, -1, -1):
        ajustar_descendo_para_menor(matriz, len(matriz), i)

def remover_menor_elemento_temporizado(matriz):
    if len(matriz) == 0:
        return None
    inicio = time.perf_counter_ns()
    raiz = matriz[0]
    matriz[0] = matriz[-1]
    matriz.pop()
    ajustar_descendo_para_menor(matriz, len(matriz), 0)
    fim = time.perf_counter_ns()
    print(f"Tempo para remover e reposicionar na Min-Heap: {(fim - inicio) / 1_000_000:.6f} ms")
    return raiz


lista_menores = [5, 2, 3, 7, 1]
print("Lista Original (Min-Heap):", lista_menores)

criar_heap_menor(lista_menores)
print("Min-Heap criada:")
print(lista_menores)

print("Removendo o menor elemento [raiz] Min-Heap:")
elemento_removido = remover_menor_elemento_temporizado(lista_menores)
print(f"Elemento removido = {elemento_removido}")
print("Min-Heap após a exclusao")
print(lista_menores)
