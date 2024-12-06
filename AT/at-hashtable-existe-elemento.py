def tem_duplicatas(lista):
    hashtable = {}
    for item in lista:
        if item in hashtable:
            return True
        hashtable[item] = True
    return False

lista_exemplo = [10, 12, 13, 14, 15, 16, 12]
print(tem_duplicatas(lista_exemplo))

lista_exemplo = [1, 2, 3, 4, 5, 6]
print(tem_duplicatas(lista_exemplo))
