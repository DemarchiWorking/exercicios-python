import time


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

class ArvoreBusca:
    def __init__(self):
        self.raiz = None


    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_rec(self.raiz, valor)


    def _inserir_rec(self, no, valor):
        if valor < no.valor:
            if no.esq is None:
                no.esq = No(valor)
            else:
                self._inserir_rec(no.esq, valor)
        else:
            if no.dir is None:
                no.dir = No(valor)
            else:
                self._inserir_rec(no.dir, valor)



    def em_ordem_iter(self):
        res, stack, curr = [], [], self.raiz
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.esq
            curr = stack.pop()
            res.append(curr.valor)
            curr = curr.dir
        return res

    def pre_ordem_iter(self):
        res, stack = [], [self.raiz]
        while stack:
            curr = stack.pop()
            if curr:
                res.append(curr.valor)
                stack.append(curr.dir)
                stack.append(curr.esq)
        return res

    def pos_ordem_iter(self):
        res, stack1, stack2 = [], [self.raiz], []
        while stack1:
            curr = stack1.pop()
            if curr:
                stack2.append(curr)
                stack1.append(curr.esq)
                stack1.append(curr.dir)
        while stack2:
            curr = stack2.pop()
            res.append(curr.valor)
        return res

    def medir_tempo(self, metodo_percurso):
        inicio = time.perf_counter()
        res, decorrido = metodo_percurso(), (time.perf_counter() - inicio) * 1000
        return res, decorrido


arvore = ArvoreBusca()
elementos = [50, 30, 70, 20, 40, 60, 80]
for elem in elementos:
    arvore.inserir(elem)


em_ordem_res_iter, em_ordem_tempo_iter = arvore.medir_tempo(arvore.em_ordem_iter)
pre_ordem_res_iter, pre_ordem_tempo_iter = arvore.medir_tempo(arvore.pre_ordem_iter)
pos_ordem_res_iter, pos_ordem_tempo_iter = arvore.medir_tempo(arvore.pos_ordem_iter)

print("Em-ordem:", em_ordem_res_iter, f"tempo: {em_ordem_tempo_iter:.5f} ms")
print("Pre-ordem:", pre_ordem_res_iter, f"tempo: {pre_ordem_tempo_iter:.5f} ms")
print("Pos-ordem:", pos_ordem_res_iter, f"tempo: {pos_ordem_tempo_iter:.5f} ms")
