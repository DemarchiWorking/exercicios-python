#Exercício 1.3 – Implementar Busca de um Valor na Árvore Binária de Busca
#Descrição: Implemente uma função que, dado um valor, procure o nó correspondente na BST.
#Exemplo: Após inserir os elementos, busque o valor 40 e informe se o elemento foi encontrado.

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

    def buscar(self, chave):
        return self._buscar(self.raiz, chave)

    def _buscar(self, raiz, chave):
        if raiz is None or raiz.valor == chave:
            return raiz is not None
        if chave < raiz.valor:
            return self._buscar(raiz.esquerda, chave)
        else:
            return self._buscar(raiz.direita, chave)

    def percurso_em_ordem(self, raiz):
        resultado = []
        if raiz:
            resultado = self.percurso_em_ordem(raiz.esquerda)
            resultado.append(raiz.valor)
            resultado = resultado + self.percurso_em_ordem(raiz.direita)
        return resultado

arvore = ArvoreBinariaBusca()
lista = [50, 30, 70, 20, 40, 60, 80]

for item in lista:
    arvore.inserir(item)
print("Em ordem:", arvore.percurso_em_ordem(arvore.raiz))

valor_procurado = 40
encontrado = arvore.buscar(valor_procurado)
print(f"{valor_procurado} encontrado:", encontrado)

