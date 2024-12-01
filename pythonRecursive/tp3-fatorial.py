def fatorial(num):
    if num == 1:
        return 1
    else:
        return num * fatorial(num-1)

numero = 15
resultado = fatorial(numero)

print(f"O Fatorial de {numero} é = {resultado}")