import math

def encontrar_quadrado(graos):
    # Calcula o n quadrado (log base 2)
    quadrado = math.log2(graos) + 1
    return int(quadrado)

graos = 16
print(encontrar_quadrado(graos))
#Q-2Use a Notação Big O para descrever a complexidade de tempo da função que você acabou de criar.
#R:A complexidade de tempo dessa função é (O(1)),constante/A operação de logaritmo base 2 é realizada em tempo constante, independentemente do valor de entrada.