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

def testar_linkedlist():
    lista = LinkedList()

    # Inserindo 1000 elementos no início
    start_time = time.time()
    for i in range(1000):
        lista.inserir_inicio(i)
    end_time = time.time()
    print(f"Tempo de inserção no início (1000 elementos): {(end_time - start_time) * 1000:.6f} ms")

    # Inserindo 1000 elementos no final
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

    # Excluindo 500 elementos
    start_time = time.time()
    for i in range(500):
        lista.excluir_valor(i)
    end_time = time.time()
    print(f"Tempo para excluir 500 valores: {(end_time - start_time) * 1000:.6f} ms")
    print("Lista após exclusões:", lista.exibir_lista()[:10], "...")  # Mostrando os primeiros 10 elementos

if __name__ == "__main__":
    testar_linkedlist()
