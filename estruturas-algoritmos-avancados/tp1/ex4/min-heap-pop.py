#Exercício 4: Remoção em Heap
#Enunciado: Explique o processo de remoção do elemento raiz em uma MinHeap e implemente uma função pop() que execute essa operação corretamente.

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
        self._heapify_cima(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("A heap está vazia, não é possível remover o elemento.")

        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]

        self.heap[0] = self.heap.pop()

        self._heapify_baixo(0)

        return raiz

    def _heapify_cima(self, indice):
        while indice > 0 and self.heap[indice] < self.heap[self.pai(indice)]:
            self.heap[indice], self.heap[self.pai(indice)] = self.heap[self.pai(indice)], self.heap[indice]
            indice = self.pai(indice)

    def _heapify_baixo(self, indice):
        menor = indice
        esquerdo = self.filho_esquerdo(indice)
        direito = self.filho_direito(indice)

        if esquerdo < len(self.heap) and self.heap[esquerdo] < self.heap[menor]:
            menor = esquerdo

        if direito < len(self.heap) and self.heap[direito] < self.heap[menor]:
            menor = direito

        if menor != indice:
            self.heap[indice], self.heap[menor] = self.heap[menor], self.heap[indice]
            self._heapify_baixo(menor)

    def obter_min(self):
        return self.heap[0] if self.heap else None

    def tamanho(self):
        return len(self.heap)


min_heap = MinHeap()
min_heap.inserir(11)
min_heap.inserir(6)
min_heap.inserir(3)
min_heap.inserir(2)
min_heap.inserir(9)

print("Atual:", min_heap.heap)
print("Removido:", min_heap.pop())
print("Heap Após Remoção:", min_heap.heap)
