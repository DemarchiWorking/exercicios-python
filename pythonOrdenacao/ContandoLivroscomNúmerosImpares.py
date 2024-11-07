def contar_livros_impares(fila_de_livros):
    contador_impares = 0
    for identificacao in fila_de_livros:
        if identificacao % 2 != 0:
            contador_impares += 1
    return contador_impares

fila_de_livros = [1001, 2002, 3003, 4004, 5005, 6006]
quantidade_impares = contar_livros_impares(fila_de_livros)
print("Total de Livros com Identificação Impar:", quantidade_impares)
