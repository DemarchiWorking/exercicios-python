def soma_lista(numeros):
    if not numeros:
        return 0
    return numeros[0] + soma_lista(numeros[1:])

lista = [1, 2, 3, 4]
print(soma_lista(lista))