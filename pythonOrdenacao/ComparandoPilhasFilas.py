class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        return None


class FilaAtendimento:
    def __init__(self):
        self.pilha1 = Pilha()
        self.pilha2 = Pilha()

    def adicionar_cliente(self, nome):
        self.pilha1.empilhar(nome)
        print(f"Cliente {nome} adicionado à fila.")

    def atender_cliente(self):
        if self.pilha1.esta_vazia() and self.pilha2.esta_vazia():
            print("Nenhum cliente na fila para atender.")
            return None

        if self.pilha2.esta_vazia():
            while not self.pilha1.esta_vazia():
                self.pilha2.empilhar(self.pilha1.desempilhar())

        cliente_atendido = self.pilha2.desempilhar()
        print(f"Atendendo cliente {cliente_atendido}.")
        return cliente_atendido

    def tamanho_fila(self):
        tamanho = len(self.pilha1.itens) + len(self.pilha2.itens)
        print(f"Número de clientes na fila: {tamanho}.")
        return tamanho


# Exemplo de uso
fila = FilaAtendimento()
fila.adicionar_cliente("Rhuan")
fila.adicionar_cliente("Joana")
fila.adicionar_cliente("Marcelo")
fila.tamanho_fila()
fila.atender_cliente()
fila.tamanho_fila()
fila.atender_cliente()
fila.atender_cliente()
fila.atender_cliente()
fila.tamanho_fila()
