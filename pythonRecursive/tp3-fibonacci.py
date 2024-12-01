def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

valor = 10
resultado = fibonacci(valor)
print(f"O número {valor} da sequencia fibonacci é {resultado}")