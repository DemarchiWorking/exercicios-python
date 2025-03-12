#Exercício 1.1 – Implementar uma Árvore Binária de Busca com Inserção e Percursos

import time

#no da arvore
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

#arvore Binária de Busca
class ArvoreBusca:
    def __init__(self):
        self.raiz = None

    #inserir elementos na arvore
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.inserir_rec(self.raiz, valor)

    # auxiliar para insercao recursiva
    def inserir_rec(self, no, valor):
        if valor < no.valor:
            if no.esq is None:
                no.esq = No(valor)
            else:
                self.inserir_rec(no.esq, valor)
        else:
            if no.dir is None:
                no.dir = No(valor)
            else:
                self.inserir_rec(no.dir, valor)

    #percurso em-ordem de forma recursiva
    def em_ordem(self):
        res = []
        self.em_ordem_rec(self.raiz, res)
        return res

    def em_ordem_rec(self, no, res):
        if no:
            self.em_ordem_rec(no.esq, res)
            res.append(no.valor)
            self.em_ordem_rec(no.dir, res)

    # percurso pre ordem recursiva
    def pre_ordem(self):
        res = []
        self.pre_ordem_rec(self.raiz, res)
        return res

    def pre_ordem_rec(self, no, res):
        if no:
            res.append(no.valor)
            self.pre_ordem_rec(no.esq, res)
            self.pre_ordem_rec(no.dir, res)

    # Percurso pós-ordem de forma recursiva
    def pos_ordem(self):
        res = []
        self.pos_ordem_rec(self.raiz, res)
        return res

    def pos_ordem_rec(self, no, res):
        if no:
            self.pos_ordem_rec(no.esq, res)
            self.pos_ordem_rec(no.dir, res)
            res.append(no.valor)

    # medir o tempo de execução de cada percurso
    def medir_tempo(self, metodo_percurso):
        inicio = time.perf_counter()
        res, decorrido = metodo_percurso(), (time.perf_counter() - inicio) * 1000  # Converte para milissegundos
        return res, decorrido


arvore = ArvoreBusca()
elementos = [50, 30, 70, 20, 40, 60, 80]
for elem in elementos:
    arvore.inserir(elem)

em_ordem_res, em_ordem_tempo = arvore.medir_tempo(arvore.em_ordem)
pre_ordem_res, pre_ordem_tempo = arvore.medir_tempo(arvore.pre_ordem)
pos_ordem_res, pos_ordem_tempo = arvore.medir_tempo(arvore.pos_ordem)

print("Em-ordem:", em_ordem_res, f"Tempo: {em_ordem_tempo:.5f} ms")
print("Pre-ordem:", pre_ordem_res, f"Tempo: {pre_ordem_tempo:.5f} ms")
print("Pos-ordem:", pos_ordem_res, f"Tempo: {pos_ordem_tempo:.5f} ms")
