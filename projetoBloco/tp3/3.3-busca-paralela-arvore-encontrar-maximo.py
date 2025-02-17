#Exercício 3.3 – Busca Paralela em Árvore para Encontrar o Valor Máximo
#Descrição: Implemente uma função que percorra a árvore de forma paralela para encontrar o maior valor armazenado.
#Exemplo: Em uma árvore com nós [15, 10, 20, 8, 12, 17, 25], o valor máximo deve ser 25.

import concurrent.futures
import time

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def encontrar_maximo_sequencial(nodo):
    """Busca sequencial para encontrar o valor máximo na árvore."""
    if nodo is None:
        return float('-inf')
    max_esquerda = encontrar_maximo_sequencial(nodo.esquerda)
    max_direita = encontrar_maximo_sequencial(nodo.direita)
    return max(nodo.valor, max_esquerda, max_direita)

def encontrar_maximo_paralelo(nodo):
    """Busca paralela para encontrar o valor máximo na árvore."""
    if nodo is None:
        return float('-inf')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futuros = []
        if nodo.esquerda is not None:
            futuros.append(executor.submit(encontrar_maximo_paralelo, nodo.esquerda))
        if nodo.direita is not None:
            futuros.append(executor.submit(encontrar_maximo_paralelo, nodo.direita))

        max_valores = [nodo.valor]
        for futuro in concurrent.futures.as_completed(futuros):
            max_valores.append(futuro.result())

    return max(max_valores)

if __name__ == "__main__":
    raiz = Nodo(15)
    raiz.esquerda = Nodo(10)
    raiz.direita = Nodo(20)
    raiz.esquerda.esquerda = Nodo(8)
    raiz.esquerda.direita = Nodo(12)
    raiz.direita.esquerda = Nodo(17)
    raiz.direita.direita = Nodo(25)

    # Medir sequencial
    inicio_tempo_seq = time.perf_counter()
    max_sequencial = encontrar_maximo_sequencial(raiz)
    fim_tempo_seq = time.perf_counter()
    tempo_execucao_seq = fim_tempo_seq - inicio_tempo_seq

    print(f"B Sequencial: Valor máximo encontrado na árvore é: {max_sequencial}")
    print(f"Tempo (sequencial): {tempo_execucao_seq:.8f} seg")

    # Medir paralela
    inicio_tempo_par = time.perf_counter()
    max_paralelo = encontrar_maximo_paralelo(raiz)
    fim_tempo_par = time.perf_counter()
    tempo_execucao_par = fim_tempo_par - inicio_tempo_par

    print(f"B Paralela: Valor máximo encontrado na árvore é: {max_paralelo}")
    print(f"Tempo (paralela): {tempo_execucao_par:.8f} seg")
