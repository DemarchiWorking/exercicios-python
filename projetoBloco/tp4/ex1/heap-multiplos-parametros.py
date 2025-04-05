import heapq
import time
import random
import gc


class MinHeap:
    def __init__(self):
        self.heap = []

    def criar_heap(self, lista):
        """Transforma uma lista em heap usando heapify"""
        self.heap = lista.copy()
        heapq.heapify(self.heap)

    def inserir_elementos(self, elementos):
        """Insere elementos um por um na heap"""
        for elem in elementos:
            heapq.heappush(self.heap, elem)

    def buscar(self, valor):
        """Busca linear na heap"""
        return valor in self.heap

    def remover_menor(self):
        """Remove e retorna o menor elemento"""
        return heapq.heappop(self.heap)

    def exibir(self):
        """Retorna a heap como lista"""
        return self.heap.copy()


def medir_tempo(operacao, *args):
    """Mede o tempo de uma operação em milissegundos"""
    gc.disable()
    inicio = time.perf_counter_ns()
    resultado = operacao(*args)
    fim = time.perf_counter_ns()
    gc.enable()
    return resultado, (fim - inicio) / 1_000_000


def testar_desempenho(tamanhos, repeticoes=3):
    """Testa o desempenho para diferentes tamanhos de heap"""
    print(f"{'Tamanho':<10} | {'Criação (ms)':<12} | {'Inserção (ms)':<12} | {'Busca (ms)':<10} | {'Remoção (ms)':<10}")
    print("-" * 70)

    for tamanho in tamanhos:
        tempos = {'criacao': [], 'insercao': [], 'busca': [], 'remocao': []}

        for _ in range(repeticoes):
            dados = [random.randint(1, 10_000_000) for _ in range(tamanho)]
            elemento_busca = random.choice(dados)

            heap = MinHeap()
            _, tempo = medir_tempo(heap.criar_heap, dados)
            tempos['criacao'].append(tempo)

            heap_vazia = MinHeap()
            _, tempo = medir_tempo(heap_vazia.inserir_elementos, dados)
            tempos['insercao'].append(tempo)

            _, tempo = medir_tempo(heap.buscar, elemento_busca)
            tempos['busca'].append(tempo)

            _, tempo = medir_tempo(heap.remover_menor)
            tempos['remocao'].append(tempo)

        media = lambda x: sum(x) / len(x)
        print(f"{tamanho:<10} | {media(tempos['criacao']):12.6f} | {media(tempos['insercao']):12.6f} | "
              f"{media(tempos['busca']):10.6f} | {media(tempos['remocao']):10.6f}")


if __name__ == "__main__":
    tamanhos = [100, 1_000, 5_000, 10_000, 50_000, 100_000]
    repeticoes = 5

    print(f"Testando com {repeticoes} repetições para cada tamanho...")
    testar_desempenho(tamanhos, repeticoes)