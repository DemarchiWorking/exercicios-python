#Exercício 2: Implementação da estrutura de dados MinHeap
#Enunciado: Implemente uma MinHeap em Python sem utilizar bibliotecas auxiliares, garantindo que os elementos sempre sejam organizados corretamente após inserções e remoções.


class MinHeap:
    def __init__(self):
        self.heap = []

    def pai(self, indice):
        return (indice - 1) // 2

    def filho_esquerdo(self, indice):
        return 2 * indice + 1

    def filho_direito(self, indice):
        return 2 * indice + 2

    def inserir(self, chave):
        self.heap.append(chave)
        self._heapify_up(len(self.heap) - 1)

    def remover_min(self):
        if len(self.heap) == 0:
            raise IndexError("Não é possível remover o menor elemento, a heap está vazia.")

        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return raiz

    def obter_min(self):
        if len(self.heap) == 0:
            raise IndexError("Não é possível obter o menor elemento, a heap está vazia.")

        return self.heap[0]

    def _heapify_up(self, indice):
        while indice > 0 and self.heap[indice] < self.heap[self.pai(indice)]:
            self.heap[indice], self.heap[self.pai(indice)] = self.heap[self.pai(indice)], self.heap[indice]
            indice = self.pai(indice)

    def _heapify_down(self, indice):
        menor = indice
        esquerdo = self.filho_esquerdo(indice)
        direito = self.filho_direito(indice)

        if esquerdo < len(self.heap) and self.heap[esquerdo] < self.heap[menor]:
            menor = esquerdo

        if direito < len(self.heap) and self.heap[direito] < self.heap[menor]:
            menor = direito

        if menor != indice:
            self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice]
            self._heapify_down(menor)

    def tamanho(self):
        return len(self.heap)


min_heap = MinHeap()
min_heap.inserir(10)
min_heap.inserir(5)
min_heap.inserir(3)
min_heap.inserir(8)
min_heap.inserir(2)
print("Heap atual:", min_heap.heap)
print("Menor elemento removido:", min_heap.remover_min())
