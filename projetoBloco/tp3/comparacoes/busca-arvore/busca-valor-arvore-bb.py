import time
import matplotlib.pyplot as plt
import numpy as np

# Árvore Binária de Busca com busca

class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        inicio = time.perf_counter_ns()
        self.raiz = self._inserir(self.raiz, chave)
        fim = time.perf_counter_ns()
        tempo_ms = (fim - inicio) / 1_000_000
        print(f"Tempo para inserir {chave}: {tempo_ms:.4f} ms")
        self.exibir_arvore()

    def _inserir(self, no, chave):
        if no is None:
            return No(chave)
        if chave < no.chave:
            no.esquerda = self._inserir(no.esquerda, chave)
        else:
            no.direita = self._inserir(no.direita, chave)
        return no

    def remover(self, chave):
        inicio = time.perf_counter_ns()
        self.raiz = self._remover(self.raiz, chave)
        fim = time.perf_counter_ns()
        tempo_ms = (fim - inicio) / 1_000_000
        print(f"Tempo para remover {chave}: {tempo_ms:.4f} ms")
        self.exibir_arvore()

    def _remover(self, no, chave):
        if no is None:
            return no
        if chave < no.chave:
            no.esquerda = self._remover(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover(no.direita, chave)
        else:
            if no.esquerda is None and no.direita is None:
                return None
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            sucessor = self._menor_valor(no.direita)
            no.chave = sucessor.chave
            no.direita = self._remover(no.direita, sucessor.chave)
        return no

    def buscar(self, chave):
        inicio = time.perf_counter_ns()
        resultado = self._buscar(self.raiz, chave)
        fim = time.perf_counter_ns()
        tempo_ms = (fim - inicio) / 1_000_000
        if resultado:
            print(f"Valor {chave} encontrado na árvore. Tempo de busca: {tempo_ms:.4f} ms")
        else:
            print(f"Valor {chave} não encontrado na árvore. Tempo de busca: {tempo_ms:.4f} ms")

    def _buscar(self, no, chave):
        if no is None or no.chave == chave:
            return no
        if chave < no.chave:
            return self._buscar(no.esquerda, chave)
        else:
            return self._buscar(no.direita, chave)

    def exibir_arvore(self):
        print("Árvore (in-order):", self.percurso_inorder())

    def _menor_valor(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def percurso_inorder(self):
        return self._percurso_inorder(self.raiz)

    def _percurso_inorder(self, no):
        if no is None:
            return []
        return self._percurso_inorder(no.esquerda) + [no.chave] + self._percurso_inorder(no.direita)

arvore = ArvoreBinariaBusca()
for chave in [50, 30, 70, 20, 40, 60, 80]:
    arvore.inserir(chave)

arvore.buscar(40)
arvore.buscar(25)

arvore.remover(20)
arvore.remover(30)
arvore.remover(50)
