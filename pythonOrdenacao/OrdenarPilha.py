def ordenar_pilha(pilha):
    pilha_auxiliar = []
    while pilha:
        temp = pilha.pop()

        while pilha_auxiliar and pilha_auxiliar[-1] < temp:
            pilha.append(pilha_auxiliar.pop())

        pilha_auxiliar.append(temp)

    while pilha_auxiliar:
        pilha.append(pilha_auxiliar.pop())

pilha_notas = [70, 85, 92, 88, 78, 99, 65]
print("Pilha original:", pilha_notas)
ordenar_pilha(pilha_notas)
print("Ordem crescente:", pilha_notas)
