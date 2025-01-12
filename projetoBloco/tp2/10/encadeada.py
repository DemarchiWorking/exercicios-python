import time


class DNode:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None


class DoublyLinkedList:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserir_inicio(self, valor):
        novo_no = DNode(valor)
        if not self.cabeca:
            self.cabeca = self.cauda = novo_no
        else:
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no

    def inserir_final(self, valor):
        novo_no = DNode(valor)
        if not self.cauda:
            self.cabeca = self.cauda = novo_no
        else:
            novo_no.anterior = self.cauda
            self.cauda.proximo = novo_no
            self.cauda = novo_no

    def excluir_posicao(self, posicao):
        if not self.cabeca:
            return
        no_atual = self.cabeca
        for _ in range(posicao):
            no_atual = no_atual.proximo
            if not no_atual:
                return
        if no_atual.anterior:
            no_atual.anterior.proximo = no_atual.proximo
        if no_atual.proximo:
            no_atual.proximo.anterior = no_atual.anterior
        if no_atual == self.cabeca:
            self.cabeca = no_atual.proximo
        if no_atual == self.cauda:
            self.cauda = no_atual.anterior

    def exibir_lista_direta(self):
        elementos = []
        no_atual = self.cabeca
        while no_atual:
            elementos.append(no_atual.valor)
            no_atual = no_atual.proximo
        return elementos

    def exibir_lista_reversa(self):
        elementos = []
        no_atual = self.cauda
        while no_atual:
            elementos.append(no_atual.valor)
            no_atual = no_atual.anterior
        return elementos

    def insertion_sort(self):
        if not self.cabeca:
            return
        no_atual = self.cabeca.proximo
        while no_atual:
            chave = no_atual
            no_prox = no_atual.proximo
            while chave.anterior and chave.anterior.valor > chave.valor:
                chave.valor, chave.anterior.valor = chave.anterior.valor, chave.valor
                chave = chave.anterior
            no_atual = no_prox

    def mesclar(self, outra_lista):
        resultado = DoublyLinkedList()
        no1 = self.cabeca
        no2 = outra_lista.cabeca

        while no1 and no2:
            if no1.valor < no2.valor:
                resultado.inserir_final(no1.valor)
                no1 = no1.proximo
            else:
                resultado.inserir_final(no2.valor)
                no2 = no2.proximo

        while no1:
            resultado.inserir_final(no1.valor)
            no1 = no1.proximo

        while no2:
            resultado.inserir_final(no2.valor)
            no2 = no2.proximo

        return resultado


def testar_doublylinkedlist():
    lista = DoublyLinkedList()

    # Inserindo elementos na lista
    for i in range(20, 0, -1):  # Inserir elementos em ordem decrescente para testar a ordenação
        lista.inserir_final(i)
    print("Lista antes da ordenação (direta):", lista.exibir_lista_direta())

    # Medindo tempo de ordenação
    start_time = time.time()
    lista.insertion_sort()
    end_time = time.time()
    print(f"Tempo para ordenação (Insertion Sort): {(end_time - start_time) * 1000:.6f} ms")
    print("Lista após ordenação (direta):", lista.exibir_lista_direta())

    # Criando outra lista para mesclagem
    outra_lista = DoublyLinkedList()
    for i in range(21, 41):  # Inserindo elementos em ordem crescente
        outra_lista.inserir_final(i)
    print("Outra lista antes da mesclagem (direta):", outra_lista.exibir_lista_direta())

    # Mesclando listas
    start_time = time.time()
    lista_mesclada = lista.mesclar(outra_lista)
    end_time = time.time()
    print(f"Tempo para mesclagem: {(end_time - start_time) * 1000:.6f} ms")
    print("Lista mesclada (direta):", lista_mesclada.exibir_lista_direta())


if __name__ == "__main__":
    testar_doublylinkedlist()
