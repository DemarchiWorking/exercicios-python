import time

# Árvore Binária de Busca com remoção de nós

class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, no, chave):
        if no is None:
            return No(chave)
        if chave < no.chave:
            no.esquerda = self._inserir(no.esquerda, chave)
        else:
            no.direita = self._inserir(no.direita, chave)
        return no

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, no, chave):
        if no is None:
            return no
        if chave < no.chave:
            no.esquerda = self._remover(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover(no.direita, chave)
        else:
            # Caso 1: Nó sem filhos
            if no.esquerda is None and no.direita is None:
                return None
            # Caso 2: Nó com um filho
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            # Caso 3: Nó com dois filhos
            sucessor = self._menor_valor(no.direita)
            no.chave = sucessor.chave
            no.direita = self._remover(no.direita, sucessor.chave)
        return no

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

# Teste
arvore = ArvoreBinariaBusca()
for chave in [50, 30, 70, 20, 40, 60, 80]:
    arvore.inserir(chave)

print("In-order antes da remoção:", arvore.percurso_inorder())

tempos = {}
casos = {20: "Nó sem filhos", 30: "Nó com um filho", 50: "Nó com dois filhos"}

for chave in [20, 30, 50]:
    inicio = time.perf_counter_ns()
    arvore.remover(chave)
    fim = time.perf_counter_ns()
    tempo_ms = (fim - inicio) / 1_000_000
    tempos[casos[chave]] = tempo_ms
    print(f"In-order após remover {chave} ({casos[chave]}):", arvore.percurso_inorder())

print(f"\nTempos de remoção por caso (ms): {tempos}")
