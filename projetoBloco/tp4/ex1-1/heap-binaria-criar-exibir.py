import heapq


class HeapBinaria:
    def __init__(self):
        self.heap = []

    def criar_heap(self, lista):
        if not all(isinstance(x, int) for x in lista):
            raise ValueError("Elementos da lista tem q ser numeros inteiros.")

        self.heap = [-elem for elem in lista]  # Negar os valores para usar como max-heap
        heapq.heapify(self.heap)

    def exibir_heap(self):
        return [-elem for elem in self.heap]  # Reverter os valores negados

    #def peneirar(self, indice):
    #    pai = (indice - 1) // 2
    #    while indice > 0 and self.heap[pai] < self.heap[indice]:
    #        self.heap[pai], self.heap[indice] = self.heap[indice], self.heap[pai]
    #        indice = pai
    #        pai = (indice - 1) // 2

def main():
    entrada = [20, 33, 17, 25, 15]
    heap = HeapBinaria()

    print("Original:", entrada)
    try:
        heap.criar_heap(entrada)
        print("Heap Lista:", heap.exibir_heap())
    except ValueError as e:
        print("Falha:", e)


if __name__ == "__main__":
    main()
