import random
from time import perf_counter


class Nodo:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.chave = chave


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        """Insere um elemento na árvore (versão iterativa para evitar recursion error)"""
        if self.raiz is None:
            self.raiz = Nodo(chave)
        else:
            self._inserir_iterativo(self.raiz, chave)

    def _inserir_iterativo(self, nodo_inicial, chave):
        """Método auxiliar iterativo para inserção"""
        nodo_atual = nodo_inicial
        while True:
            if chave < nodo_atual.chave:
                if nodo_atual.esquerda is None:
                    nodo_atual.esquerda = Nodo(chave)
                    return
                nodo_atual = nodo_atual.esquerda
            else:
                if nodo_atual.direita is None:
                    nodo_atual.direita = Nodo(chave)
                    return
                nodo_atual = nodo_atual.direita

    def verificar_se_eh_bst(self):
        """Verifica se a árvore é uma BST válida"""
        return self._verificar_se_eh_bst(self.raiz, float('-inf'), float('inf'))

    def _verificar_se_eh_bst(self, nodo, minimo, maximo):
        """Método recursivo de verificação"""
        if nodo is None:
            return True
        if nodo.chave <= minimo or nodo.chave >= maximo:
            return False
        return (self._verificar_se_eh_bst(nodo.esquerda, minimo, nodo.chave) and
                self._verificar_se_eh_bst(nodo.direita, nodo.chave, maximo))


def gerar_listas_aleatorias(tamanho_inicial=100, multiplicador=2, num_listas=10):
    """Gera listas aleatórias de tamanhos crescentes"""
    listas = []
    tamanho = tamanho_inicial
    for _ in range(num_listas):
        lista = random.sample(range(tamanho * 10), tamanho)
        listas.append(lista)
        tamanho *= multiplicador
    return listas


def teste_performance():
    """Testa o tempo de execução para diferentes tamanhos de árvore"""
    listas = gerar_listas_aleatorias(tamanho_inicial=100, num_listas=10)
    resultados = []

    for lista in listas:
        arvore = ArvoreBinariaBusca()

        for elem in lista:
            arvore.inserir(elem)

        for _ in range(3):
            arvore.verificar_se_eh_bst()

        inicio = perf_counter()
        for _ in range(10):
            arvore.verificar_se_eh_bst()
        fim = perf_counter()

        tempo_medio_ms = ((fim - inicio) / 10) * 1000
        resultados.append((len(lista), tempo_medio_ms))

    return resultados


def exemplo_manual():
    """Exemplo manual de verificação de BST"""
    print("\nExemplo Manual:")
    arvore = ArvoreBinariaBusca()
    elementos = [50, 30, 70, 20, 40, 60, 80]

    for elem in elementos:
        arvore.inserir(elem)

    print("Árvore válida?", arvore.verificar_se_eh_bst())

    arvore.raiz.esquerda.direita.chave = 55
    print("Árvore após modificação:", arvore.verificar_se_eh_bst())


if __name__ == "__main__":
    print("Teste de Performance:")
    print("Tamanho (n) | Tempo (ms) | Tempo/n (µs/n)")
    print("------------|------------|---------------")
    resultados = teste_performance()
    for tamanho, tempo in resultados:
        tempo_por_n = (tempo / tamanho) * 1000
        print(f"{tamanho:11} | {tempo:9.4f} | {tempo_por_n:12.6f}")

    exemplo_manual()