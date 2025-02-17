#Exercício 3.2 – Busca em Profundidade (DFS) Paralela com Retorno de Caminho
#Descrição: Utilize paralelismo para implementar uma busca em profundidade que retorne o caminho (lista de nós) desde a raiz até o elemento buscado.
#Exemplo: Para uma árvore simples com raiz 1, retorne o caminho até o nó 5.

import concurrent.futures
import time

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def busca_sequencial(nodo, valor_busca):
    """Busca sequencial de um valor na árvore."""
    if nodo is None:
        return False
    if nodo.valor == valor_busca:
        return True
    return busca_sequencial(nodo.esquerda, valor_busca) or busca_sequencial(nodo.direita, valor_busca)

def busca_dfs_paralela(nodo, valor_busca, caminho):
    """Busca em profundidade paralela que retorna o caminho até o valor procurado.
    Parâmetros:nodo (Nodo): O nodo atual da árvore.
    valor_busca (int): O valor a ser procurado.
    caminho (list): A lista que guarda o caminho percorrido até o valor.
    Retorna:list ou bool: O caminho se o valor for encontrado, False caso contrário."""
    if nodo is None:
        return False

    # Adiciona o nodo atual ao caminho
    caminho.append(nodo.valor)

    if nodo.valor == valor_busca:
        return caminho

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futuros = []
        if nodo.esquerda is not None:
            futuros.append(executor.submit(busca_dfs_paralela, nodo.esquerda, valor_busca, caminho.copy()))
        if nodo.direita is not None:
            futuros.append(executor.submit(busca_dfs_paralela, nodo.direita, valor_busca, caminho.copy()))

        for futuro in concurrent.futures.as_completed(futuros):
            resultado = futuro.result()
            if resultado:
                return resultado

    caminho.pop()  # Remove o nodo atual se não for o caminho correto
    return False

if __name__ == "__main__":
    # Construindo a árvore binária
    raiz = Nodo(1)
    raiz.esquerda = Nodo(2)
    raiz.direita = Nodo(3)
    raiz.esquerda.esquerda = Nodo(4)
    raiz.esquerda.direita = Nodo(5)
    raiz.direita.esquerda = Nodo(6)
    raiz.direita.direita = Nodo(7)

    valor_busca = 5

    # Medir o tempo de execução da busca sequencial
    inicio_tempo_seq = time.perf_counter()
    encontrado_seq = busca_sequencial(raiz, valor_busca)
    fim_tempo_seq = time.perf_counter()
    tempo_execucao_seq = fim_tempo_seq - inicio_tempo_seq

    if encontrado_seq:
        print(f"B Sequencial: Valor {valor_busca} encontrado na árvore.")
    else:
        print(f"B Sequencial: Valor {valor_busca} não encontrado na árvore.")
    print(f"Tempo de execução (sequencial): {tempo_execucao_seq:.8f} segundos")

    # Medir o tempo de execução da busca em profundidade paralela
    caminho = []
    inicio_tempo_par = time.perf_counter()
    caminho_encontrado = busca_dfs_paralela(raiz, valor_busca, caminho)
    fim_tempo_par = time.perf_counter()
    tempo_execucao_par = fim_tempo_par - inicio_tempo_par

    if caminho_encontrado:
        print(f"B Paralela: Valor {valor_busca} encontrado na árvore. Caminho: {caminho_encontrado}")
    else:
        print(f"B Paralela: Valor {valor_busca} não encontrado na árvore.")
    print(f"Tempo de execução (paralela): {tempo_execucao_par:.8f} segundos")
