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

def contar_pedidos_impares(pilha_de_pedidos):
    contador_impares = 0
    pilha_aux = Pilha()

    while not pilha_de_pedidos.esta_vazia():
        pedido = pilha_de_pedidos.desempilhar()
        if pedido % 2 != 0:
            contador_impares += 1
        pilha_aux.empilhar(pedido)

    while not pilha_aux.esta_vazia():
        pilha_de_pedidos.empilhar(pilha_aux.desempilhar())

    return contador_impares

pilha_de_pedidos = Pilha()
pilha_de_pedidos.empilhar(1001)
pilha_de_pedidos.empilhar(2002)
pilha_de_pedidos.empilhar(3003)
pilha_de_pedidos.empilhar(4004)
pilha_de_pedidos.empilhar(5005)
quantidade_impares = contar_pedidos_impares(pilha_de_pedidos)
print("quantidade com identificação ímpar:", quantidade_impares)
