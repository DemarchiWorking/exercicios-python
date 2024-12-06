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

    def buscar_minimo(self):
        if self.raiz is None:
            return None
        return self._buscar_minimo(self.raiz)

    def _buscar_minimo(self, no_atual):
        while no_atual.esquerda is not None:
            no_atual = no_atual.esquerda
        return no_atual.valor

    def buscar_maximo(self):
        if self.raiz is None:
            return None
        return self._buscar_maximo(self.raiz)

    def _buscar_maximo(self, no_atual):
        while no_atual.direita is not None:
            no_atual = no_atual.direita
        return no_atual.valor

notas = [85, 70, 95, 60, 75, 90, 100]

arvore_notas = ArvoreBinariaBusca()
for nota in notas:
    arvore_notas.inserir(nota)

nota_minima = arvore_notas.buscar_minimo()
nota_maxima = arvore_notas.buscar_maximo()

print(f"Nota mínima: {nota_minima}")
print(f"Nota máxima: {nota_maxima}")
