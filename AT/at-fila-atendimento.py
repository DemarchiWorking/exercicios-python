class Fila:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if self.esta_vazia():
            return None
        return self.itens.pop(0)

    def tamanho(self):
        return len(self.itens)

    def ver_primeiro(self):
        if self.esta_vazia():
            return None
        return self.itens[0]

fila_chamados = Fila()
fila_chamados.enfileirar("1- Chamado Reset Senha")
fila_chamados.enfileirar("2- Chamado Troca Telefone")
fila_chamados.enfileirar("3- Chamado Configuração VPN")
print("Chamados após inserções:", fila_chamados.itens)
atendido = fila_chamados.desenfileirar()
print("Atendendo:", atendido)
print("Fila após remoção:", fila_chamados.itens)

atendido = fila_chamados.desenfileirar()
print("Atendendo:", atendido)
print("Fila de chamados após remoção:", fila_chamados.itens)
