import time
import random
from collections import defaultdict


class No:
    """Nó de uma Árvore Binária de Busca"""
    __slots__ = ['esquerda', 'direita', 'valor']  # Otimização de memória

    def __init__(self, valor):
        self.esquerda = None
        self.direita = None
        self.valor = valor


class ArvoreBinariaBusca:
    """Implementação otimizada de BST com medição de desempenho"""

    def __init__(self):
        self.raiz = None
        self.tamanho = 0

    def inserir(self, valor):
        """Insere um valor na árvore, retorna True se inserido"""
        if self.raiz is None:
            self.raiz = No(valor)
            self.tamanho += 1
            return True

        inserido = self._inserir_rec(self.raiz, valor)
        if inserido:
            self.tamanho += 1
        return inserido

    def _inserir_rec(self, no, valor):
        """Inserção recursiva auxiliar"""
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
                return True
            return self._inserir_rec(no.esquerda, valor)
        elif valor > no.valor:
            if no.direita is None:
                no.direita = No(valor)
                return True
            return self._inserir_rec(no.direita, valor)
        return False  # Valor duplicado

    def em_ordem(self):
        """Retorna lista em ordem (left, root, right)"""
        resultado = []
        self._em_ordem_rec(self.raiz, resultado)
        return resultado

    def _em_ordem_rec(self, no, resultado):
        if no:
            self._em_ordem_rec(no.esquerda, resultado)
            resultado.append(no.valor)
            self._em_ordem_rec(no.direita, resultado)

    def pre_ordem(self):
        """Retorna lista em pré-ordem (root, left, right)"""
        resultado = []
        self._pre_ordem_rec(self.raiz, resultado)
        return resultado

    def _pre_ordem_rec(self, no, resultado):
        if no:
            resultado.append(no.valor)
            self._pre_ordem_rec(no.esquerda, resultado)
            self._pre_ordem_rec(no.direita, resultado)

    def pos_ordem(self):
        """Retorna lista em pós-ordem (left, right, root)"""
        resultado = []
        self._pos_ordem_rec(self.raiz, resultado)
        return resultado

    def _pos_ordem_rec(self, no, resultado):
        if no:
            self._pos_ordem_rec(no.esquerda, resultado)
            self._pos_ordem_rec(no.direita, resultado)
            resultado.append(no.valor)


def gerar_lista_aleatoria(tamanho, min_val=0, max_val=1000):
    """Gera lista com valores únicos entre min_val e max_val"""
    return random.sample(range(min_val, max_val + 1), tamanho)


def testar_desempenho(tamanhos):
    """Testa o desempenho para diferentes tamanhos de lista"""
    resultados = []

    for tamanho in tamanhos:
        lista = gerar_lista_aleatoria(tamanho)
        arvore = ArvoreBinariaBusca()

        inicio_insercao = time.perf_counter_ns()
        for valor in lista:
            arvore.inserir(valor)
        tempo_insercao = (time.perf_counter_ns() - inicio_insercao) / 1e6  # ms

        tempos_percursos = {}
        for nome, metodo in [('em_ordem', arvore.em_ordem),
                             ('pre_ordem', arvore.pre_ordem),
                             ('pos_ordem', arvore.pos_ordem)]:
            inicio = time.perf_counter_ns()
            metodo()  # Executar percurso
            tempos_percursos[nome] = (time.perf_counter_ns() - inicio) / 1e6  # ms

        resultados.append({
            'tamanho': tamanho,
            'tempo_insercao_total': tempo_insercao,
            'tempo_por_insercao': tempo_insercao / tamanho,
            **tempos_percursos
        })

    return resultados


def exibir_resultados(resultados):
    """Exibe os resultados em formato tabular"""
    print("\n=== RESULTADOS DE DESEMPENHO ===")
    print(
        f"{'Tamanho':<8} | {'Inserção (ms)':<12} | {'Inserção/Item (μs)':<17} | {'Em Ordem (ms)':<13} | {'Pré-Ordem (ms)':<13} | {'Pós-Ordem (ms)':<13}")
    print("-" * 95)

    for res in resultados:
        print(
            f"{res['tamanho']:<8} | {res['tempo_insercao_total']:12.4f} | {res['tempo_por_insercao'] * 1000:17.4f} | {res['em_ordem']:13.4f} | {res['pre_ordem']:13.4f} | {res['pos_ordem']:13.4f}")


if __name__ == "__main__":
    print("=== TESTE BÁSICO CONFORME ENUNCIADO ===")
    arvore_teste = ArvoreBinariaBusca()
    lista_teste = [50, 30, 70, 20, 40, 60, 80]

    for valor in lista_teste:
        arvore_teste.inserir(valor)

    print("\nResultados esperados:")
    print("Em ordem:", arvore_teste.em_ordem())
    print("Pré-ordem:", arvore_teste.pre_ordem())
    print("Pós-ordem:", arvore_teste.pos_ordem())

    tamanhos_testes = [7, 14, 28, 56, 112, 224, 448, 896]
    resultados = testar_desempenho(tamanhos_testes)

    exibir_resultados(resultados)

    print("\n=== ANÁLISE DE COMPLEXIDADE ===")
    print("• Inserção: Esperado O(log n) para árvore balanceada")
    print("• Percursos: Esperado O(n) para todos os casos")
    print("• Tempos devem crescer aproximadamente linearmente para percursos")
    print("• Tempo por inserção deve permanecer relativamente constante para árvore balanceada")