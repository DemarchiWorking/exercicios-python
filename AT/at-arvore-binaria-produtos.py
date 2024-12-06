class NoArvoreBinaria:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = NoArvoreBinaria(valor)
        else:
            self._inserir(valor, self.raiz)

    def _inserir(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoArvoreBinaria(valor)
            else:
                self._inserir(valor, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = NoArvoreBinaria(valor)
            else:
                self._inserir(valor, no_atual.direita)

    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)

    def _remover(self, no_atual, valor):
        if no_atual is None:
            return no_atual

        if valor < no_atual.valor:
            no_atual.esquerda = self._remover(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direita = self._remover(no_atual.direita, valor)
        else:
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda

            temp = self._minimo_valor_no(no_atual.direita)
            no_atual.valor = temp.valor
            no_atual.direita = self._remover(no_atual.direita, temp.valor)

        return no_atual

    def _minimo_valor_no(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def em_ordem(self):
        elementos = []
        self._em_ordem(self.raiz, elementos)
        return elementos

    def _em_ordem(self, no_atual, elementos):
        if no_atual:
            self._em_ordem(no_atual.esquerda, elementos)
            elementos.append(no_atual.valor)
            self._em_ordem(no_atual.direita, elementos)

codigos = [45, 25, 65, 20, 30, 60, 70]

arvore_codigos = ArvoreBinariaBusca()
for codigo in codigos:
    arvore_codigos.inserir(codigo)


def exibir_arvore_ordem(arvore):
    elementos = arvore.em_ordem()
    print("Árvore em ordem crescente:", elementos)

exibir_arvore_ordem(arvore_codigos)

arvore_codigos.remover(20)
print("Remover o codigo 20:")
exibir_arvore_ordem(arvore_codigos)

arvore_codigos.remover(25)
print("Remover o código 25:")
exibir_arvore_ordem(arvore_codigos)

arvore_codigos.remover(45)
print("Remover o código 45:")
exibir_arvore_ordem(arvore_codigos)
