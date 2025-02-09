#Exercício 6: Aplicação de Heap em um cenário real
#Enunciado: Explique como uma Heap pode ser utilizada para implementar uma Fila de Prioridade. Em seguida, implemente um sistema de agendamento de tarefas onde cada tarefa possui uma prioridade, utilizando uma MinHeap.

class Tarefa:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade

    def __lt__(self, outra_tarefa):
        return self.prioridade < outra_tarefa.prioridade

    def __repr__(self):
        return f"Tarefa({self.nome}, {self.prioridade})"


class MinHeap:
    def __init__(self):
        self.heap = []

    def pai(self, indice):
        return (indice - 1) // 2

    def filho_esquerdo(self, indice):
        return 2 * indice + 1

    def filho_direito(self, indice):
        return 2 * indice + 2

    def inserir(self, tarefa):
        self.heap.append(tarefa)
        self._heapify_cima(len(self.heap) - 1)

    def _heapify_cima(self, indice):
        while indice > 0 and self.heap[indice] < self.heap[self.pai(indice)]:
            self.heap[indice], self.heap[self.pai(indice)] = self.heap[self.pai(indice)], self.heap[indice]
            indice = self.pai(indice)

    def remover_min(self):
        if len(self.heap) == 0:
            raise IndexError("A heap está vazia, não é possível remover o elemento.")
        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_baixo(0)
        return raiz

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


class Agendador:
    def __init__(self):
        self.min_heap = MinHeap()

    def agendar(self, tarefa):
        self.min_heap.inserir(tarefa)

    def executar(self):
        return self.min_heap.remover_min()

    def visualizar_proxima_tarefa(self):
        return self.min_heap.obter_min()

    def tamanho(self):
        return self.min_heap.tamanho()


agendador = Agendador()

tarefa1 = Tarefa("Analisar dados", 2)
tarefa2 = Tarefa("Construir Interface", 7)
tarefa3 = Tarefa("Criar Documentação", 4)
tarefa4 = Tarefa("Desenvolver Lógica Backend", 8)
tarefa5 = Tarefa("Hospedar na Núvem", 10)


agendador.agendar(tarefa1)
agendador.agendar(tarefa2)
agendador.agendar(tarefa3)
agendador.agendar(tarefa4)
agendador.agendar(tarefa5)


print("\nPróxima sem remover:", agendador.visualizar_proxima_tarefa())

while agendador.tamanho() > 0:
    print("\nExecutando:", agendador.executar())
