#Exercício 2.3 – Paralelismo para Processamento de Tarefas Pesadas (Contagem de Primos)
#Descrição: Implemente uma função que verifica se um número é primo e, em seguida, divida um intervalo grande entre vários processos para contar quantos números primos existem.
#Exemplo: Conte os números primos entre 1 e 100000 utilizando todos os núcleos disponíveis.

import multiprocessing

def e_primo(numero):
    """Verifica se um número e primo.
    Parâmetros:numero (int): O número a ser verificado.
    Retorna:bool: True se o número for primo, False caso contrário.
    """
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True


def contar_primos_em_intervalo(intervalo):
    """Conta quantos números primos existem em um intervalo.
    Parâmetros:intervalo (tuple): Uma tupla com o início e o fim do intervalo.
    Retorna:int: A quantidade de números primos no intervalo."""
    inicio, fim = intervalo
    contador = 0
    for numero in range(inicio, fim):
        if e_primo(numero):
            contador += 1
    return contador

def contar_primos_parallel(inicio, fim):
    """Conta o total de números primos em um intervalo utilizando processamento paralelo.
    Parâmetros:inicio (int): O início do intervalo.
    fim (int): O fim do intervalo.
    Retorna:int: O total de números primos no intervalo. """
    num_processos = multiprocessing.cpu_count()
    tamanho_intervalo = (fim - inicio) // num_processos
    intervalos = [(inicio + i * tamanho_intervalo, inicio + (i + 1) * tamanho_intervalo) for i in range(num_processos)]
    # Corrigir o último intervalo para incluir o valor final
    intervalos[-1] = (intervalos[-1][0], fim)

    with multiprocessing.Pool(processes=num_processos) as pool:
        contagem_parcial = pool.map(contar_primos_em_intervalo, intervalos)

    total_primos = sum(contagem_parcial)
    return total_primos


if __name__ == "__main__":
    inicio = 1
    fim = 100000

    total_primos = contar_primos_parallel(inicio, fim)
    print(f"Quantidade de primos entre {inicio} e {fim} : {total_primos}")
