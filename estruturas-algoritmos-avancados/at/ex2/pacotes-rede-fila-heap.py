import timeit

class Pacote:
    def __init__(self, id_pacote, prioridade, tempo_transmissao):
        self.id_pacote = id_pacote
        self.prioridade = prioridade
        self.tempo_transmissao = tempo_transmissao

    def __lt__(self, outro):
        # menor prioridade tem precedencia; em empate, menor tempo de transmissao eh priorizado
        if self.prioridade == outro.prioridade:
            return self.tempo_transmissao < outro.tempo_transmissao
        return self.prioridade < outro.prioridade


class HeapMinima:
    def __init__(self):
        self.heap = []
        self.indice_map = {}

    def inserir(self, pacote):
        self.heap.append(pacote)
        self.indice_map[pacote.id_pacote] = len(self.heap) - 1
        self._organizar_para_cima(len(self.heap) - 1)

    def remover_minimo(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            pacote = self.heap.pop()
            del self.indice_map[pacote.id_pacote]
            return pacote
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        del self.indice_map[raiz.id_pacote]
        if self.heap:
            self.indice_map[self.heap[0].id_pacote] = 0
            self._organizar_para_baixo(0)
        return raiz

    def atualizar_prioridade(self, id_pacote, nova_prioridade):
        if id_pacote not in self.indice_map:
            raise ValueError(f"Pacote com ID {id_pacote} não encontrado.")
        indice = self.indice_map[id_pacote]
        pacote = self.heap[indice]
        pacote.prioridade = nova_prioridade
        self._organizar_para_cima(indice)
        self._organizar_para_baixo(indice)

    def obter_minimo(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def _organizar_para_cima(self, indice):
        while indice > 0 and self.heap[indice] < self.heap[(indice - 1) // 2]:
            pai = (indice - 1) // 2
            self._trocar(indice, pai)
            indice = pai

    def _organizar_para_baixo(self, indice):
        menor = indice
        esquerdo = 2 * indice + 1
        direito = 2 * indice + 2

        if esquerdo < len(self.heap) and self.heap[esquerdo] < self.heap[menor]:
            menor = esquerdo
        if direito < len(self.heap) and self.heap[direito] < self.heap[menor]:
            menor = direito
        if menor != indice:
            self._trocar(indice, menor)
            self._organizar_para_baixo(menor)

    def _trocar(self, i, j):
        self.indice_map[self.heap[i].id_pacote] = j
        self.indice_map[self.heap[j].id_pacote] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def main():
    heap = HeapMinima()

    while True:
        print("Menu:")
        print("1. inserir um novo pacote")
        print("2. remover o pacote de maior prioridade")
        print("3. atualizar a prioridade de um pacote existente")
        print("4. consultar o pacote de maior prioridade")
        print("5. sair")

        escolha = input("escolha uma opcao: ")

        if escolha == "1":
            id_pacote = input("id do pacote: ")
            prioridade = int(input("prioridade : "))
            tempo_transmissao = int(input("tempo estimado de transmissao: "))

            def inserir_pacote():
                heap.inserir(Pacote(id_pacote, prioridade, tempo_transmissao))
                print("pacote inserido.")

            tempo = timeit.timeit(inserir_pacote, number=1)
            print(f"tempo de execucao: {tempo * 1000:.6f} ms")

        elif escolha == "2":
            def remover_pacote():
                pacote_removido = heap.remover_minimo()
                if pacote_removido:
                    print(f"pcote removido: id: {pacote_removido.id_pacote}, prioridade: {pacote_removido.prioridade}")
                else:
                    print("fila vazia.")

            tempo = timeit.timeit(remover_pacote, number=1)
            print(f"tempo de execucao: {tempo * 1000:.6f} ms")

        elif escolha == "3":
            id_pacote = input("id do pacote para atualizar: ")
            nova_prioridade = int(input("nova prioridade: "))

            def atualizar_prioridade():
                try:
                    heap.atualizar_prioridade(id_pacote, nova_prioridade)
                    print("prioridade do pacote atualizada com sucesso.")
                except ValueError as e:
                    print(e)

            tempo = timeit.timeit(atualizar_prioridade, number=1)
            print(f"tempo de execucao: {tempo * 1000:.6f} ms")

        elif escolha == "4":
            def consultar_minimo():
                pacote_minimo = heap.obter_minimo()
                if pacote_minimo:
                    print(f"pacote com maior prioridade: id: {pacote_minimo.id_pacote}, "
                          f"prioridade: {pacote_minimo.prioridade}, tempo: {pacote_minimo.tempo_transmissao}")
                else:
                    print("a fila esta vazia.")

            tempo = timeit.timeit(consultar_minimo, number=1)
            print(f"tempo de execucao: {tempo * 1000:.6f} ms")

        elif escolha == "5":
            print("encerrando o programa.")
            break
        else:
            print("opcao invalida. tente novamente.")
        print("estado atual da fila:")
        for pacote in heap.heap:
            print(f"id: {pacote.id_pacote}, prioridade: {pacote.prioridade}, tempo: {pacote.tempo_transmissao}")

if __name__ == "__main__":
    main()
