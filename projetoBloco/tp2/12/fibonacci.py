import time

# Função recursiva para calcular o n-ésimo número de Fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Função recursiva com memorização
def fibonacci_mem(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci_mem(n - 1, memo) + fibonacci_mem(n - 2, memo)
        return memo[n]

def testar_fibonacci():
    numeros = [10, 20, 30, 35]  # Exemplos de valores para testar

    # Comparando execução sem memorização
    print("Tempo de execução sem memorização:")
    for numero in numeros:
        start_time = time.time()
        resultado = fibonacci(numero)
        end_time = time.time()
        tempo_execucao = (end_time - start_time) * 1000  # Convertendo para milissegundos
        print(f"Fibonacci de {numero} é {resultado}. Tempo de execução: {tempo_execucao:.6f} ms")

    # Comparando execução com memorização
    print("\nTempo de execução com memorização:")
    for numero in numeros:
        start_time = time.time()
        resultado = fibonacci_mem(numero)
        end_time = time.time()
        tempo_execucao = (end_time - start_time) * 1000  # Convertendo para milissegundos
        print(f"Fibonacci de {numero} é {resultado}. Tempo de execução: {tempo_execucao:.6f} ms")

if __name__ == "__main__":
    testar_fibonacci()
