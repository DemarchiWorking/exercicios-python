#Grupo 1 – Algoritmos de Busca e Manipulação em Estruturas de Árvore
#Exercício 1.1 – Implementar uma Árvore Binária de Busca com Inserção e Percursos
#Descrição: Crie uma classe de árvore binária de busca (BST) que permita inserir elementos e realizar percursos em pré-ordem, in-ordem e pós-ordem.
#Exemplo:
#Inserindo os elementos [50, 30, 70, 20, 40, 60, 80], os percursos gerados serão:
# • In-order: 20 30 40 50 60 70 80
# • Pre-order: 50 30 20 40 70 60 80
# • Post-order: 20 40 30 60 80 70 50

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

    def percurso_em_ordem(self, raiz):
        resultado = []
        if raiz:
            resultado = self.percurso_em_ordem(raiz.esquerda)
            resultado.append(raiz.valor)
            resultado = resultado + self.percurso_em_ordem(raiz.direita)
        return resultado

    def percurso_pre_ordem(self, raiz):
        resultado = []
        if raiz:
            resultado.append(raiz.valor)
            resultado = resultado + self.percurso_pre_ordem(raiz.esquerda)
            resultado = resultado + self.percurso_pre_ordem(raiz.direita)
        return resultado

    def percurso_pos_ordem(self, raiz):
        resultado = []
        if raiz:
            resultado = self.percurso_pos_ordem(raiz.esquerda)
            resultado = resultado + self.percurso_pos_ordem(raiz.direita)
            resultado.append(raiz.valor)
        return resultado

arvore = ArvoreBinariaBusca()
lista = [50, 30, 70, 20, 40, 60, 80]

for item in lista:
    arvore.inserir(item)

print("Em ordem:", arvore.percurso_em_ordem(arvore.raiz))
print("Pré-ordem:", arvore.percurso_pre_ordem(arvore.raiz))
print("Pós-ordem:", arvore.percurso_pos_ordem(arvore.raiz))
