#Exercício 1.4 – Verificar se uma Árvore é uma BST Válida
#Descrição: Implemente uma função que verifica se uma árvore binária qualquer satisfaz a propriedade de BST, utilizando os limites mínimo e máximo permitidos para cada nó.
#Exemplo: Construa uma árvore e teste a função antes e depois de alterar manualmente algum nó para invalidar a propriedade BST.


class Nodo:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.chave = chave

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = Nodo(chave)
        else:
            self._inserir(self.raiz, chave)

    def _inserir(self, nodo_atual, chave):
        if chave < nodo_atual.chave:
            if nodo_atual.esquerda is None:
                nodo_atual.esquerda = Nodo(chave)
            else:
                self._inserir(nodo_atual.esquerda, chave)
        else:
            if nodo_atual.direita is None:
                nodo_atual.direita = Nodo(chave)
            else:
                self._inserir(nodo_atual.direita, chave)

    def verificar_se_eh_bst(self):
        return self._verificar_se_eh_bst(self.raiz, float('-inf'), float('inf'))

    def _verificar_se_eh_bst(self, nodo, limite_min, limite_max):
        if nodo is None:
            return True
        if nodo.chave <= limite_min or nodo.chave >= limite_max:
            return False
        return (self._verificar_se_eh_bst(nodo.esquerda, limite_min, nodo.chave) and
                self._verificar_se_eh_bst(nodo.direita, nodo.chave, limite_max))

    def percurso_em_ordem(self, nodo):
        resultado = []
        if nodo:
            resultado = self.percurso_em_ordem(nodo.esquerda)
            resultado.append(nodo.chave)
            resultado = resultado + self.percurso_em_ordem(nodo.direita)
        return resultado

# Exemplo de uso
arvore = ArvoreBinariaBusca()
elementos = [50, 30, 70, 20, 40, 60, 80]

for el in elementos:
    arvore.inserir(el)

print("Percurso em ordem inicial:", arvore.percurso_em_ordem(arvore.raiz))  # Deve imprimir: [20, 30, 40, 50, 60, 70, 80]

# Verificar se a árvore é uma BST válida
print("A árvore é uma BST válida?", arvore.verificar_se_eh_bst())  # Deve imprimir: True

# Alterar manualmente um nó para invalidar a propriedade BST
arvore.raiz.esquerda.direita.chave = 10

# Verificar novamente após a alteração
print("A árvore é uma BST válida após alteração?", arvore.verificar_se_eh_bst())  # Deve imprimir: False
