import timeit
import random

def gerar_pacotes(n):
    return [Pacote(f"pacote_{i}", random.randint(1, 100), random.randint(1, 500)) for i in range(n)]

def teste_massa(heap, lista_ordenada, lista_nao_ordenada, n_pacotes, n_operacoes):
    pacotes = gerar_pacotes(n_pacotes)

    # Inserção de pacotes
    print("\nInserindo massa de pacotes...")
    tempo_heap_inserir = medir_tempo(lambda: [heap.inserir(p) for p in pacotes])
    tempo_lista_ordenada_inserir = medir_tempo(lambda: [lista_ordenada.inserir(p) for p in pacotes])
    tempo_lista_nao_ordenada_inserir = medir_tempo(lambda: [lista_nao_ordenada.inserir(p) for p in pacotes])
    print(f"Tempo para inserir {n_pacotes} pacotes:")
    print(f"Heap: {tempo_heap_inserir:.6f} ms")
    print(f"Lista Ordenada: {tempo_lista_ordenada_inserir:.6f} ms")
    print(f"Lista Não Ordenada: {tempo_lista_nao_ordenada_inserir:.6f} ms")

    # Atualização de prioridades aleatórias
    ids_pacotes = [p.id_pacote for p in pacotes]
    print("\nAtualizando prioridades aleatórias...")
    tempo_heap_atualizar = medir_tempo(
        lambda: [heap.atualizar_prioridade(random.choice(ids_pacotes), random.randint(1, 100)) for _ in
                 range(n_operacoes)])
    tempo_lista_ordenada_atualizar = medir_tempo(
        lambda: [lista_ordenada.atualizar_prioridade(random.choice(ids_pacotes), random.randint(1, 100)) for _ in
                 range(n_operacoes)])
    tempo_lista_nao_ordenada_atualizar = medir_tempo(
        lambda: [lista_nao_ordenada.atualizar_prioridade(random.choice(ids_pacotes), random.randint(1, 100)) for _
                 in range(n_operacoes)])
    print(f"Tempo para atualizar {n_operacoes} prioridades:")
    print(f"Heap: {tempo_heap_atualizar:.6f} ms")
    print(f"Lista Ordenada: {tempo_lista_ordenada_atualizar:.6f} ms")
    print(f"Lista Não Ordenada: {tempo_lista_nao_ordenada_atualizar:.6f} ms")

    # Remoção de pacotes prioritários
    print("\nRemovendo pacotes de maior prioridade...")
    tempo_heap_remover = medir_tempo(lambda: [heap.remover_minimo() for _ in range(min(n_pacotes, n_operacoes))])
    tempo_lista_ordenada_remover = medir_tempo(
        lambda: [lista_ordenada.remover_minimo() for _ in range(min(n_pacotes, n_operacoes))])
    tempo_lista_nao_ordenada_remover = medir_tempo(
        lambda: [lista_nao_ordenada.remover_minimo() for _ in range(min(n_pacotes, n_operacoes))])
    print(f"Tempo para remover {min(n_pacotes, n_operacoes)} pacotes:")
    print(f"Heap: {tempo_heap_remover:.6f} ms")
    print(f"Lista Ordenada: {tempo_lista_ordenada_remover:.6f} ms")
    print(f"Lista Não Ordenada: {tempo_lista_nao_ordenada_remover:.6f} ms")

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



class ListaOrdenada:
    def __init__(self):
        self.lista = []

    def inserir(self, pacote):
        self.lista.append(pacote)
        self.lista.sort(key=lambda x: (x.prioridade, x.tempo_transmissao))

    def remover_minimo(self):
        return self.lista.pop(0) if self.lista else None

    def atualizar_prioridade(self, id_pacote, nova_prioridade):
        for pacote in self.lista:
            if pacote.id_pacote == id_pacote:
                pacote.prioridade = nova_prioridade
                self.lista.sort(key=lambda x: (x.prioridade, x.tempo_transmissao))
                break

    def obter_minimo(self):
        return self.lista[0] if self.lista else None


class ListaNaoOrdenada:
    def __init__(self):
        self.lista = []

    def inserir(self, pacote):
        self.lista.append(pacote)

    def remover_minimo(self):
        if not self.lista:
            return None
        minimo = min(self.lista, key=lambda x: (x.prioridade, x.tempo_transmissao))
        self.lista.remove(minimo)
        return minimo

    def atualizar_prioridade(self, id_pacote, nova_prioridade):
        for pacote in self.lista:
            if pacote.id_pacote == id_pacote:
                pacote.prioridade = nova_prioridade
                break

    def obter_minimo(self):
        if not self.lista:
            return None
        return min(self.lista, key=lambda x: (x.prioridade, x.tempo_transmissao))


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

def medir_tempo(func, *args, **kwargs):
    tempo = timeit.timeit(lambda: func(*args, **kwargs), number=1)
    return tempo * 1000



def main():
    heap = HeapMinima()
    lista_ordenada = ListaOrdenada()
    lista_nao_ordenada = ListaNaoOrdenada()

    while True:
        print("\nMenu:")
        print("1. Inserir um novo pacote")
        print("2. Remover o pacote de maior prioridade")
        print("3. Atualizar a prioridade de um pacote existente")
        print("4. Consultar o pacote de maior prioridade")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            id_pacote = input("ID do pacote: ")
            prioridade = int(input("Prioridade: "))
            tempo_transmissao = int(input("Tempo estimado de transmissão: "))
            pacote = Pacote(id_pacote, prioridade, tempo_transmissao)

            print("\nMedindo tempos para 'Inserir':")
            print(f"Heap: {medir_tempo(heap.inserir, pacote):.6f} ms")
            print(f"Lista Ordenada: {medir_tempo(lista_ordenada.inserir, pacote):.6f} ms")
            print(f"Lista Não Ordenada: {medir_tempo(lista_nao_ordenada.inserir, pacote):.6f} ms")

        elif escolha == "2":
            print("\nMedindo tempos para 'Remover':")
            print(f"Heap: {medir_tempo(heap.remover_minimo):.6f} ms")
            print(f"Lista Ordenada: {medir_tempo(lista_ordenada.remover_minimo):.6f} ms")
            print(f"Lista Não Ordenada: {medir_tempo(lista_nao_ordenada.remover_minimo):.6f} ms")

        elif escolha == "3":
            id_pacote = input("ID do pacote para atualizar: ")
            nova_prioridade = int(input("Nova prioridade: "))

            print("\nMedindo tempos para 'Atualizar':")
            print(f"Heap: {medir_tempo(heap.atualizar_prioridade, id_pacote, nova_prioridade):.6f} ms")
            print(f"Lista Ordenada: {medir_tempo(lista_ordenada.atualizar_prioridade, id_pacote, nova_prioridade):.6f} ms")
            print(f"Lista Não Ordenada: {medir_tempo(lista_nao_ordenada.atualizar_prioridade, id_pacote, nova_prioridade):.6f} ms")

        elif escolha == "4":
            print("\nMedindo tempos para 'Consultar':")
            print(f"Heap: {medir_tempo(heap.obter_minimo):.6f} ms")
            print(f"Lista Ordenada: {medir_tempo(lista_ordenada.obter_minimo):.6f} ms")
            print(f"Lista Não Ordenada: {medir_tempo(lista_nao_ordenada.obter_minimo):.6f} ms")

        elif escolha == "5":
            print("Encerrando o programa.")
            break

        elif escolha == "9":
            print("6. Testar desempenho com massa de dados")
            n_pacotes = int(input("Número de pacotes para o teste: "))
            n_operacoes = int(input("Número de operações (atualizações e remoções): "))

            print("\nExecutando testes de desempenho com massa de dados...")
            teste_massa(heap, lista_ordenada, lista_nao_ordenada, n_pacotes, n_operacoes)


        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
