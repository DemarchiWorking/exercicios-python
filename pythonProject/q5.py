def maior_numero(array):
    contagem = {}
    for num in array:
        if num in contagem:
            contagem[num] += 1
        else:
            contagem[num] = 1

    maior_unico = 0
    for num, count in contagem.items():
        if count == 1:
            if maior_unico is None or num > maior_unico:
                maior_unico = num
    return maior_unico


print(maior_numero([2, 4, 6, 8, 10, 12, 13]))

