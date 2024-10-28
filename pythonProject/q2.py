#q2
cartas_embaralhadas = [12, 3, 7, 1, 9, 5, 11, 2, 8, 4, 10, 6, 13]

cartas_ordenadas = []

#inserir na posição
def inserir_ordenado(cartas, carta):
    if not cartas:
        cartas.append(carta)
    else:
        for i in range(len(cartas)):
            if carta < cartas[i]:
                cartas.insert(i, carta)
                return
        cartas.append(carta)

#ordenação
while cartas_embaralhadas:
    carta = cartas_embaralhadas.pop(0)
    inserir_ordenado(cartas_ordenadas, carta)

print(cartas_ordenadas)