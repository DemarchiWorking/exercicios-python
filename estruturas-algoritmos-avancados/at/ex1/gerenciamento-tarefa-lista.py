import timeit

class ProcessoLista:
    def __init__(self, id, tempo_execucao, prioridade):
        self.id = id
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade

class ListaPrioridade:
    def __init__(self):
        self.lista = []

    def inserir(self, processo):
        self.lista.append(processo)
        self.lista.sort(key=lambda x: (x.prioridade, x.tempo_execucao))  # O(n log n)

    def remover_min(self):
        if not self.lista:
            raise IndexError("A lista esta vazia.")
        return self.lista.pop(0)

    def modificar_prioridade(self, id, nova_prioridade):
        for processo in self.lista:
            if processo.id == id:
                processo.prioridade = nova_prioridade
                self.lista.sort(key=lambda x: (x.prioridade, x.tempo_execucao))
                return
        raise ValueError(f"processo com ID {id} nao encontrado.")

    def tamanho(self):
        return len(self.lista)

def menu_lista():
    fila_prioridade = ListaPrioridade()
    while True:
        print("Escolha a opção:")
        print("1 - adicionar um processo na lista de prioridade")
        print("2 - executar o proximo processo de maior prioridade (rmv)")
        print("3 - modificar a prioridade de um processo existente")
        print("4 - sair")

        opcao = input("digite a opcao: ")

        if opcao == "1":
            id = int(input("qual ID do processo: "))
            tempo_execucao = int(input("entre com o tempo de execucao: "))
            prioridade = int(input("entre com a prioridade: "))

            def acao():
                processo = ProcessoLista(id, tempo_execucao, prioridade)
                fila_prioridade.inserir(processo)
                print(f"processo ID {id} adicionado com prioridade {prioridade}.")

            tempo = timeit.timeit(acao, number=1)
            print(f"tempo de execucao: {tempo * 1000:.6f} ms")

        elif opcao == "2":
            def acao():
                try:
                    processo_executado = fila_prioridade.remover_min()
                    print(f"processo ID {processo_executado.id} com prioridade {processo_executado.prioridade} foi executado.")
                except IndexError:
                    print("lista vazia.")

            tempo = timeit.timeit(acao, number=1)
            print(f"tempo de execucao: {tempo * 1000:.6f} ms")

        elif opcao == "3":
            def acao():
                try:
                    id = int(input("digite o ID que deseja modificar: "))
                    nova_prioridade = int(input("Digite a nova prioridade: "))
                    fila_prioridade.modificar_prioridade(id, nova_prioridade)
                    print(f"prioridade do ID {id} alterada para {nova_prioridade}.")
                except ValueError as e:
                    print(e)

            tempo = timeit.timeit(acao, number=1)
            print(f"tempo de execucao: {tempo * 1000:.6f} ms")

        elif opcao == "4":
            print("encerrando.")
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
                    processo = ProcessoLista(i, tempo_execucao, prioridade)

                    inicio = timeit.default_timer()
                    fila_prioridade.inserir(processo)
                    fim = timeit.default_timer()

                    if (i + 1) % 1000 == 0:
                        print(
                            f"Tempo para adicionar ate o processo ID {i + 1}: {(fim - inicio) * 1000:.6f} ms")

            tempo_total = timeit.timeit(acao, number=1)
            print(f"tempo total de execucao: {tempo_total * 1000:.6f} ms")

        else:
            print("erro. opcao invalida.")

menu_lista()
