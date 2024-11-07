def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivô = lista[0]
        menores = [x for x in lista[1:] if x <= pivô]
        maiores = [x for x in lista[1:] if x > pivô]
        return quick_sort(menores) + [pivô] + quick_sort(maiores)


lista_numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", lista_numeros)
lista_ordenada = bubble_sort(lista_numeros)
print("Lista ordenada:", lista_ordenada)
