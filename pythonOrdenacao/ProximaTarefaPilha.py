class Pilha:
    def __init__(self):
        self.itens = []
    def esta_vazia(self):
        return len(self.itens) == 0
    def empilhar(self, item):
        if isinstance(item, list):
            for i in item:
                self.itens.append(i)
        else:
            self.itens.append(item)
    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        return None
    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        return None
def tarefa_no_topo(pilha_de_tarefas):
    return pilha_de_tarefas.topo()
pilha_de_tarefas = Pilha()
pilha_de_tarefas.empilhar("Tarefa 1")
pilha_de_tarefas.empilhar("Tarefa 2")
pilha_de_tarefas.empilhar("Tarefa 3")
topo = tarefa_no_topo(pilha_de_tarefas)
print("Tarefa no topo:", topo)  