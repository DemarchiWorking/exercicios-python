import timeit


class Processo:
    def __init__(self, id, tempo_execucao, prioridade):
        self.id = id
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade

    def __lt__(self, outro):
        if self.prioridade == outro.prioridade:
            return self.tempo_execucao < outro.tempo_execucao
        return self.prioridade < outro.prioridade


class MinHeap:
    def __init__(self):
        self.heap = []
        self.indice_map = {}

    def pai(self, indice):
        return (indice - 1) // 2

    def filho_esquerdo(self, indice):
        return 2 * indice + 1

    def filho_direito(self, indice):
        return 2 * indice + 2

    def inserir(self, processo):
        self.heap.append(processo)
        self.indice_map[processo.id] = len(self.heap) - 1
        self._heapify_up(len(self.heap) - 1)

    def remover_min(self):
        if len(self.heap) == 0:
            raise IndexError("fila vazia.")
        if len(self.heap) == 1:
            processo = self.heap.pop()
            del self.indice_map[processo.id]
            return processo

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        del self.indice_map[raiz.id]
        if self.heap:
            self.indice_map[self.heap[0].id] = 0
            self._heapify_down(0)
        return raiz

    def modificar_prioridade(self, id, nova_prioridade):
        if id not in self.indice_map:
            raise ValueError(f"processo com id {id} nao encontrado.")
        indice = self.indice_map[id]
        processo = self.heap[indice]
        processo.prioridade = nova_prioridade
        self._heapify_up(indice)
        self._heapify_down(indice)

    def obter_min(self):
        if len(self.heap) == 0:
            raise IndexError("a fila esta vazia.")
        return self.heap[0]

    def _heapify_up(self, indice):
        while indice > 0 and self.heap[indice] < self.heap[self.pai(indice)]:
            self._trocar(indice, self.pai(indice))
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
            self._trocar(indice, menor)
            self._heapify_down(menor)

    def _trocar(self, indice1, indice2):
        self.indice_map[self.heap[indice1].id] = indice2
        self.indice_map[self.heap[indice2].id] = indice1
        self.heap[indice1], self.heap[indice2] = self.heap[indice2], self.heap[indice1]

    def tamanho(self):
        return len(self.heap)


# Menu interativo com medição de tempo
def menu():
    fila_prioridade = MinHeap()
    while True:
        print("escolha a opcao:")
        print("1 - adicionar um novo processo a fila de prioridade")
        print("2 - executar o proximo processo de maior prioridade (remov)")
        print("3 - modificar a prioridade de um processo existente")
        print("4 - sair")

        opcao = input("Digite a opcao: ")

        if opcao == "1":
            id = int(input("qual id do processo: "))
            tempo_execucao = int(input("entre com o tempo de execucao: "))
            prioridade = int(input("entre com prioridade : "))

            def acao():
                processo = Processo(id, tempo_execucao, prioridade)
                fila_prioridade.inserir(processo)
                print(f"processo ID {id} adicionado com prioridade {prioridade}.")

            tempo = timeit.timeit(acao, number=1)
            print(f"tempo de execucao: {tempo * 1000:.6f} ms")

        elif opcao == "2":
            def acao():
                try:
                    processo_executado = fila_prioridade.remover_min()
                    print(
                        f"processo ID {processo_executado.id} com prioridade {processo_executado.prioridade} foi executado.")
                except IndexError:
                    print("a fila de prioridade está vazia.")

            tempo = timeit.timeit(acao, number=1)
            print(f"tempo de execucao: {tempo * 1000:.6f} ms")

        elif opcao == "3":
            def acao():
                try:
                    id = int(input("digite o ID do processo que deseja modificar: "))
                    nova_prioridade = int(input("digite a nova prioridade: "))
                    fila_prioridade.modificar_prioridade(id, nova_prioridade)
                    print(f"prioridade do ID {id}  alterada = {nova_prioridade}.")
                except ValueError as e:
                    print(e)

            tempo = timeit.timeit(acao, number=1)
            print(f"tempo de execucao: {tempo * 1000:.6f} ms")

        elif opcao == "4":
            print("encerrando o programa.")
            break

        elif opcao == "5":
            def acao():
                if fila_prioridade.tamanho() == 0:
                    print("fila vazia.")
                else:
                    print("xxx executando todos os processos na ordem da fila:")
                    while fila_prioridade.tamanho() > 0:
                        processo_executado = fila_prioridade.remover_min()
                        print(f"processo ID {processo_executado.id} com prioridade {processo_executado.prioridade} e tempo de execucao {processo_executado.tempo_execucao} foi executado.")

            tempo = timeit.timeit(acao, number=1)
            print(f"tempo total de execucao: {tempo * 1000:.6f} ms")
        elif opcao == "6":
            print("adicionando 10000 processos...")
            def acao():
                for i in range(10000):
                    tempo_execucao = (i % 10) + 1
                    prioridade = (i % 5) + 1
                    processo = Processo(i, tempo_execucao, prioridade)

                    inicio = timeit.default_timer()
                    fila_prioridade.inserir(processo)
                    fim = timeit.default_timer()

                    if (i + 1) % 1000 == 0:
                        print(
                            f"Tempo para adicionar ate o processo ID {i + 1}: {(fim - inicio) * 1000:.6f} ms")

            tempo_total = timeit.timeit(acao, number=1)
            print(f"tempo total de execucao: {tempo_total * 1000:.6f} ms")

        else:
            print("erro. entre com opcao valida.")



menu()
