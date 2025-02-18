#Exercício 1.2 – Implementar Deleção de um Nó na Árvore Binária de Busca
#Descrição:
#Implemente a remoção de um nó na BST, considerando os três casos: nó sem filhos, com um filho e com dois filhos (usando o sucessor in-order).
#Exemplo:
#Após inserir [50, 30, 70, 20, 40, 60, 80], remova os nós 20, 30 e 50, observando a mudança do percurso in-order.

class No:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.valor = chave

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
        else:
            self._inserir(self.raiz, chave)

    def _inserir(self, raiz, chave):
        if chave < raiz.valor:
            if raiz.esquerda is None:
                raiz.esquerda = No(chave)
            else:
                self._inserir(raiz.esquerda, chave)
        else:
            if raiz.direita is None:
                raiz.direita = No(chave)
            else:
                self._inserir(raiz.direita, chave)

    def deletar(self, chave):
        self.raiz = self._deletar(self.raiz, chave)

    def _deletar(self, raiz, chave):
        if raiz is None:
            return raiz
        if chave < raiz.valor:
            raiz.esquerda = self._deletar(raiz.esquerda, chave)
        elif chave > raiz.valor:
            raiz.direita = self._deletar(raiz.direita, chave)
        else:
            if raiz.esquerda is None:
                return raiz.direita
            elif raiz.direita is None:
                return raiz.esquerda
            temp = self._minValorNo(raiz.direita)
            raiz.valor = temp.valor
            raiz.direita = self._deletar(raiz.direita, temp.valor)
        return raiz

    def _minValorNo(self, no):
        atual = no
        while(atual.esquerda is not None):
            atual = atual.esquerda
        return atual

    def percurso_em_ordem(self, raiz):
        resultado = []
        if raiz:
            resultado = self.percurso_em_ordem(raiz.esquerda)
            resultado.append(raiz.valor)
            resultado = resultado + self.percurso_em_ordem(raiz.direita)
        return resultado


arvore_binaria = ArvoreBinariaBusca()
lista = [50, 30, 70, 20, 40, 60, 80]

for item in lista:
    arvore_binaria.inserir(item)

print("Percurso em ordem:", arvore_binaria.percurso_em_ordem(arvore_binaria.raiz))

arvore_binaria.deletar(20)
print("Percurso em ordem dps deletar 20:", arvore_binaria.percurso_em_ordem(arvore_binaria.raiz))

arvore_binaria.deletar(30)
print("Percurso em ordem dps deletar 30:", arvore_binaria.percurso_em_ordem(arvore_binaria.raiz))

arvore_binaria.deletar(50)
print("Percurso em ordem dps deletar 50:", arvore_binaria.percurso_em_ordem(arvore_binaria.raiz))

#1.2-delecao-no-arvore-binaria-busca.py