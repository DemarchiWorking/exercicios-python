import time

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def testar_fatorial():
    numeros = [5, 10, 15, 20, 25, 30]
    for numero in numeros:
        start_time = time.time()
        resultado = fatorial(numero)
        end_time = time.time()
        tempo_execucao = (end_time - start_time) * 1000  # Convertendo para milissegundos
        print(f"Fatorial de {numero} é {resultado}. Tempo de execução: {tempo_execucao:.6f} ms")

if __name__ == "__main__":
    testar_fatorial()
