import time

def ajustar_descendo_para_maior(matriz, tamanho, indice):
    maior_indice = indice
    filho_esquerdo = 2 * indice + 1
    filho_direito = 2 * indice + 2

    if filho_esquerdo < tamanho and matriz[filho_esquerdo] > matriz[maior_indice]:
        maior_indice = filho_esquerdo

    if filho_direito < tamanho and matriz[filho_direito] > matriz[maior_indice]:
        maior_indice = filho_direito

    if maior_indice != indice:
        matriz[indice], matriz[maior_indice] = matriz[maior_indice], matriz[indice]
        ajustar_descendo_para_maior(matriz, tamanho, maior_indice)

def criar_heap_maior(matriz):
    for i in range((len(matriz) - 2) // 2, -1, -1):
        ajustar_descendo_para_maior(matriz, len(matriz), i)

def remover_maior_elemento_temporizado(matriz):
    if len(matriz) == 0:
        return None
    inicio = time.perf_counter_ns()
    raiz = matriz[0]
    matriz[0] = matriz[-1]
    matriz.pop()
    ajustar_descendo_para_maior(matriz, len(matriz), 0)
    fim = time.perf_counter_ns()
    print(f"Tempo para remover e reeordenar a Max-Heap: {(fim - inicio) / 1_000_000:.6f} ms")
    return raiz

lista_maiores = [5, 2, 3, 7, 1]
print("Lista Original (Max-Heap):", lista_maiores)

criar_heap_maior(lista_maiores)
print("Max-Heap criada:")
print(lista_maiores)

print("Removendo o maior elemento [raiz]  Max-Heap:")
elemento_removido = remover_maior_elemento_temporizado(lista_maiores)
print(f"Elemento removido: {elemento_removido}")
print("Max-Heap após exclusao:")
print(lista_maiores)
