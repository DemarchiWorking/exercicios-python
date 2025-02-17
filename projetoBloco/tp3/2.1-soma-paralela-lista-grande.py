import multiprocessing

def soma(parametro):
    """Calcula a soma de uma parte da lista.
    Parâmetros:(list): Uma lista de números a serem somados.
    Retorna:int: A soma dos números na lista."""
    return sum(parametro)

if __name__ == "__main__":
    # Definindo o tamanho da lista em 10 milhões de itens
    tamanho_lista = 10000000
    # Gerando a lista de números de 1 até 10 milhões
    lista_numeros = list(range(1, tamanho_lista + 1))

    # Obtendo o número de núcleos disponíveis na CPU
    num_processos = multiprocessing.cpu_count()
    # Calculando o tamanho de cada pedaço para dividir a lista
    tamanho_pedaco = tamanho_lista // num_processos
    # Dividindo a lista em pedaços para cada processo
    pedacos = [lista_numeros[i * tamanho_pedaco:(i + 1) * tamanho_pedaco] for i in range(num_processos)]

    # Adicionando os elementos restantes ao último pedaço
    pedacos[-1].extend(lista_numeros[num_processos * tamanho_pedaco:])

    # Usando um pool de processos para calcular a soma de cada pedaço
    with multiprocessing.Pool(processes=num_processos) as pool:
        resultados = pool.map(soma, pedacos)

    # Somando os resultados para obter total
    total = sum(resultados)
    print(f"Resposta: {total}")
