import time

def soma_sequencial(lista):
    """Calcula a soma de toda a lista sequencialmente."""
    return sum(lista)

if __name__ == "__main__":
    # Medir tempo total de execução
    inicio = time.time()

    # Definindo o tamanho da lista em 10 milhões de itens
    tamanho_lista = 10_000_000
    lista_numeros = list(range(1, tamanho_lista + 1))

    # Calcular a soma sequencialmente
    total = soma_sequencial(lista_numeros)

    # Medir tempo final
    fim = time.time()
    tempo_total = fim - inicio

    # Exibir resultados
    print(f"Resposta: {total}")
    print(f"Tempo total de execução: {tempo_total:.6f} segundos")
