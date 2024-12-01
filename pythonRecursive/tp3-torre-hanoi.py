def torres_hanoi(n, origem, destino, aux):
    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
    else:
        torres_hanoi(n-1, origem, aux, destino)

        print(f"Mova o disco {n} de {origem} para {destino}")

        torres_hanoi(n - 1, aux, destino, origem)

torres_hanoi(3, 'A', 'C', 'B')