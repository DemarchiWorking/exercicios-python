def encontrar_duplicados_bruteforce(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados

def encontrar_duplicados_otimizado(lista):
    vistos = set()
    duplicados = set()
    for numero in lista:
        if numero in vistos:
            duplicados.add(numero)
        else:
            vistos.add(numero)
    return list(duplicados)


def main():
    import random
    # Criar uma lista com 5 milhões de números aleatórios entre 0 e 1000000
    lista = [random.randint(0, 1000000) for _ in range(5000000)]

    print("abordagem de força bruta")
    duplicados_bruteforce = encontrar_duplicados_bruteforce(lista)
    print(f"Duplicados (força bruta): {len(duplicados_bruteforce)} encontrados")

    print("abordagem otimizada...")
    duplicados_otimizado = encontrar_duplicados_otimizado(lista)
    print(f"Duplicados (otimizado): {len(duplicados_otimizado)} encontrados")


if __name__ == "__main__":
    main()
