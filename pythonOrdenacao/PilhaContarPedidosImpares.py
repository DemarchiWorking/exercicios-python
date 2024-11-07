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


def contar_impares(pilha_de_pedidos):
    contador_impares = 0
    for pedido in pilha_de_pedidos.itens:
        if pedido % 2 != 0:
            contador_impares += 1
    return contador_impares

def contar_pares(pilha_de_pedidos):
    contador_pares = 0
    for pedido in pilha_de_pedidos.itens:
        if pedido % 2 == 0:
            contador_pares += 1
    return contador_pares

pilha_de_pedidos = Pilha()
pilha_de_pedidos.empilhar(101)
pilha_de_pedidos.empilhar(102)
pilha_de_pedidos.empilhar(103)
pilha_de_pedidos.empilhar(104)
pilha_de_pedidos.empilhar(105)
quantidade_impares = contar_impares(pilha_de_pedidos)
quantidade_pares= contar_pares(pilha_de_pedidos)
print("identificação ímpar:", quantidade_impares)
print("identificação pares:", quantidade_pares)
