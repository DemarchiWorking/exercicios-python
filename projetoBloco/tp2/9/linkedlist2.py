import time

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class LinkedList:
    def __init__(self):
        self.cabeca = None

    def inserir_inicio(self, valor):
        novo_no = Node(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def inserir_final(self, valor):
        novo_no = Node(valor)
        if not self.cabeca:
            self.cabeca = novo_no
            return
        ultimo = self.cabeca
        while ultimo.proximo:
            ultimo = ultimo.proximo
        ultimo.proximo = novo_no

    def excluir_valor(self, valor):
        no_atual = self.cabeca
        no_anterior = None

        while no_atual and no_atual.valor != valor:
            no_anterior = no_atual
            no_atual = no_atual.proximo

        if not no_atual:
            return

        if not no_anterior:
            self.cabeca = no_atual.proximo
        else:
            no_anterior.proximo = no_atual.proximo

    def exibir_lista(self):
        elementos = []
        no_atual = self.cabeca
        while no_atual:
            elementos.append(no_atual.valor)
            no_atual = no_atual.proximo
        return elementos

    def buscar_valor(self, valor):
        no_atual = self.cabeca
        posicao = 0
        while no_atual:
            if no_atual.valor == valor:
                return posicao
            no_atual = no_atual.proximo
            posicao += 1
        return -1

    def inverter_lista(self):
        no_anterior = None
        no_atual = self.cabeca
        while no_atual:
            no_proximo = no_atual.proximo
            no_atual.proximo = no_anterior
            no_anterior = no_atual
            no_atual = no_proximo
        self.cabeca = no_anterior

def testar_linkedlist():
    lista = LinkedList()

    # Medindo tempo de inserção no início
    start_time = time.time()
    for i in range(1000):
        lista.inserir_inicio(i)
    end_time = time.time()
    print(f"Tempo de inserção no início (1000 elementos): {(end_time - start_time) * 1000:.6f} ms")

    # Medindo tempo de inserção no final
    start_time = time.time()
    for i in range(1000, 2000):
        lista.inserir_final(i)
    end_time = time.time()
    print(f"Tempo de inserção no final (1000 elementos): {(end_time - start_time) * 1000:.6f} ms")

    # Exibindo lista
    start_time = time.time()
    elementos = lista.exibir_lista()
    end_time = time.time()
    print("Lista após inserções:", elementos[:10], "...")  # Mostrando os primeiros 10 elementos
    print(f"Tempo para exibir lista: {(end_time - start_time) * 1000:.6f} ms")

    # Buscando valor na lista
    valor_para_buscar = 1500
    start_time = time.time()
    posicao = lista.buscar_valor(valor_para_buscar)
    end_time = time.time()
    print(f"Tempo para buscar o valor {valor_para_buscar}: {(end_time - start_time) * 1000:.6f} ms")
    print(f"Posição do valor {valor_para_buscar}: {posicao}")

    # Invertendo a lista
    start_time = time.time()
    lista.inverter_lista()
    end_time = time.time()
    print(f"Tempo para inverter a lista: {(end_time - start_time) * 1000:.6f} ms")
    print("Lista após inversão:", lista.exibir_lista()[:10], "...")  # Mostrando os primeiros 10 elementos

if __name__ == "__main__":
    testar_linkedlist()
