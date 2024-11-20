import os
import time
import tracemalloc

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None

    def esta_vazia(self):
        return self.topo is None

    def empilhar(self, item):
        novo_no = No(item)
        novo_no.proximo = self.topo
        self.topo = novo_no

    def desempilhar(self):
        if self.esta_vazia():
            raise IndexError("Desempilhar de uma pilha vazia")
        item_desempilhado = self.topo.dado
        self.topo = self.topo.proximo
        return item_desempilhado

    def acessar_posicao(self, pos):
        atual = self.topo
        contador = 0
        while atual is not None and contador < pos:
            atual = atual.proximo
            contador += 1
        return atual.dado if atual else None

class Fila:
    def __init__(self):
        self.frente = self.fim = None

    def esta_vazia(self):
        return self.frente is None

    def enfileirar(self, item):
        novo_no = No(item)
        if self.fim is None:
            self.frente = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError("Desenfileirar de uma fila vazia")
        item_desenfileirado = self.frente.dado
        self.frente = self.frente.proximo
        if self.frente is None:
            self.fim = None
        return item_desenfileirado

    def acessar_posicao(self, pos):
        atual = self.frente
        contador = 0
        while atual is not None and contador < pos:
            atual = atual.proximo
            contador += 1
        return atual.dado if atual else None

class TabelaHash:
    def __init__(self):
        self.tabela = {}

    def inserir(self, chave, valor):
        self.tabela[chave] = valor

    def obter(self, chave):
        return self.tabela.get(chave, None)

    def deletar(self, chave):
        if chave in self.tabela:
            del self.tabela[chave]


def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        return [linha.strip() for linha in arquivo]


def medir_tempo_memoria(funcao, *args):
    tempos = []
    memorias = []

    for _ in range(10):
        tracemalloc.start()
        inicio_tempo = time.perf_counter_ns()
        resultado = funcao(*args)
        fim_tempo = time.perf_counter_ns()
        memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        tempos.append(fim_tempo - inicio_tempo)
        memorias.append(memoria_pico)

    tempo_medio = sum(tempos) / len(tempos)
    memoria_media = sum(memorias) / len(memorias)

    return tempo_medio, memoria_media


def realizar_operacoes_pilha(pilha, arquivos, posicoes):
    tempos_adicao = []
    memorias_adicao = []
    tempos_remocao = []
    memorias_remocao = []
    itens_removidos = []

    # Adicionar itens à pilha
    for arquivo in arquivos:
        inicio_tempo = time.perf_counter_ns()
        tracemalloc.start()
        pilha.empilhar(arquivo)
        fim_tempo = time.perf_counter_ns()
        memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        tempos_adicao.append(fim_tempo - inicio_tempo)
        memorias_adicao.append(memoria_pico)

    # Pilha temporária para armazenar itens que não serão removidos
    pilha_temporaria = Pilha()

    # Remover itens das posições especificadas
    inicio_tempo = time.perf_counter_ns()
    tracemalloc.start()
    for _ in range(len(arquivos)):
        item = pilha.desempilhar()
        if _ in posicoes:
            itens_removidos.append(item)
        else:
            pilha_temporaria.empilhar(item)

    # Retornar os itens não removidos à pilha original
    while not pilha_temporaria.esta_vazia():
        pilha.empilhar(pilha_temporaria.desempilhar())

    fim_tempo = time.perf_counter_ns()
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tempos_remocao.append(fim_tempo - inicio_tempo)
    memorias_remocao.append(memoria_pico)

    tempo_adicao_medio = sum(tempos_adicao) / len(tempos_adicao)
    memoria_adicao_media = sum(memorias_adicao) / len(memorias_adicao)
    tempo_remocao_medio = sum(tempos_remocao) / len(tempos_remocao)
    memoria_remocao_media = sum(memorias_remocao) / len(memorias_remocao)

    tempo_adicao_medio = tempo_adicao_medio / 1e9
    tempo_remocao_medio = tempo_remocao_medio / 1e9

    return tempo_adicao_medio, memoria_adicao_media, tempo_remocao_medio, memoria_remocao_media, itens_removidos


def realizar_operacoes_fila(fila, arquivos, posicoes):
    tempos_adicao = []
    memorias_adicao = []
    tempos_remocao = []
    memorias_remocao = []
    itens_removidos = []

    # Adicionar itens à fila
    for arquivo in arquivos:
        inicio_tempo = time.perf_counter_ns()
        tracemalloc.start()
        fila.enfileirar(arquivo)
        fim_tempo =  time.perf_counter_ns()
        memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        tempos_adicao.append(fim_tempo - inicio_tempo)
        memorias_adicao.append(memoria_pico)

    # Fila temporária para armazenar itens que não serão removidos
    fila_temporaria = Fila()

    # Remover itens das posições especificadas
    inicio_tempo = time.perf_counter_ns()
    tracemalloc.start()
    for _ in range(len(arquivos)):
        item = fila.desenfileirar()
        if _ in posicoes:
            itens_removidos.append(item)
        else:
            fila_temporaria.enfileirar(item)

    # Retornar os itens não removidos à fila original
    while not fila_temporaria.esta_vazia():
        fila.enfileirar(fila_temporaria.desenfileirar())

    fim_tempo = time.perf_counter_ns()
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tempos_remocao.append(fim_tempo - inicio_tempo)
    memorias_remocao.append(memoria_pico)

    tempo_adicao_medio = sum(tempos_adicao) / len(tempos_adicao)
    memoria_adicao_media = sum(memorias_adicao) / len(memorias_adicao)
    tempo_remocao_medio = sum(tempos_remocao) / len(tempos_remocao)
    memoria_remocao_media = sum(memorias_remocao) / len(memorias_remocao)

    tempo_adicao_medio = tempo_adicao_medio / 1e9
    tempo_remocao_medio = tempo_remocao_medio / 1e9

    return tempo_adicao_medio, memoria_adicao_media, tempo_remocao_medio, memoria_remocao_media, itens_removidos


def realizar_operacoes_tabela(tabela, arquivos, posicoes):
    tempos_adicao = []
    memorias_adicao = []
    tempos_remocao = []
    memorias_remocao = []
    itens_removidos = []

    for i, arquivo in enumerate(arquivos):
        inicio_tempo = time.perf_counter_ns()
        tracemalloc.start()
        chave = str(i)
        tabela.inserir(chave, arquivo)
        fim_tempo = time.perf_counter_ns()
        memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        tempos_adicao.append(fim_tempo - inicio_tempo)
        memorias_adicao.append(memoria_pico)

    inicio_tempo = time.perf_counter_ns()
    tracemalloc.start()
    for pos in posicoes:
        chave = str(pos)
        itens_removidos.append(tabela.obter(chave))
        tabela.deletar(chave)
    fim_tempo = time.perf_counter_ns()
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tempos_remocao.append(fim_tempo - inicio_tempo)
    memorias_remocao.append(memoria_pico)

    tempo_adicao_medio = sum(tempos_adicao) / len(tempos_adicao)
    memoria_adicao_media = sum(memorias_adicao) / len(memorias_adicao)
    tempo_remocao_medio = sum(tempos_remocao) / len(tempos_remocao)
    memoria_remocao_media = sum(memorias_remocao) / len(memorias_remocao)

    tempo_adicao_medio = tempo_adicao_medio / 1e9
    tempo_remocao_medio = tempo_remocao_medio / 1e9

    return tempo_adicao_medio, memoria_adicao_media, tempo_remocao_medio, memoria_remocao_media, itens_removidos



def main():
    caminho_diretorio = 'tp1'
    arquivos = [os.path.basename(f) for f in os.listdir(caminho_diretorio) if os.path.isfile(os.path.join(caminho_diretorio, f))]

    print("Arquivos encontrados:", arquivos)
    posicoes = [0, 99, 999, 4999, len(arquivos) - 1]

    # Pilha
    pilha = Pilha()
    tempo_pilha, memoria_pilha = medir_tempo_memoria(lambda: [pilha.empilhar(arq) for arq in arquivos])
    tempo_pilha = tempo_pilha / 1e9
    tempo_adicao_pilha, memoria_adicao_pilha, tempo_remocao_pilha, memoria_remocao_pilha, itens_removidos_pilha = realizar_operacoes_pilha(pilha, arquivos, posicoes)

    # Fila
    fila = Fila()
    tempo_fila, memoria_fila = medir_tempo_memoria(lambda: [fila.enfileirar(arq) for arq in arquivos])
    tempo_fila = tempo_fila / 1e9
    tempo_adicao_fila, memoria_adicao_fila, tempo_remocao_fila, memoria_remocao_fila, itens_removidos_fila = realizar_operacoes_fila(fila, arquivos, posicoes)

    # TabelaHash
    tabela = TabelaHash()
    tempo_tabela, memoria_tabela = medir_tempo_memoria(lambda: [tabela.inserir(str(i), arq) for i, arq in enumerate(arquivos)])
    tempo_tabela = tempo_tabela / 1e9
    tempo_adicao_tabela, memoria_adicao_tabela, tempo_remocao_tabela, memoria_remocao_tabela, itens_removidos_tabela = realizar_operacoes_tabela(tabela, arquivos, posicoes)
    print("Pilha")
    for p in itens_removidos_pilha:
        print(p)
    print("Fila")
    for f in itens_removidos_fila:
        print(f)
    print("Tabela Hash")
    for h in itens_removidos_tabela:
        print(h)
    # Resultados
    print("Medições de Tempo e Memória:")
    print(f"Pilha (Adicionar Itens)- Tempo: {tempo_pilha:.10f} segundos, Memória: {memoria_pilha / 1024:.4f}KB")
    print(f"Pilha (Remover Itens) - Tempo: {tempo_remocao_pilha:.10f} segundos, Memória: {memoria_remocao_pilha / 1024:.4f}KB")
    print(f"Pilha (Unidade) - Tempo: {tempo_adicao_pilha:.10f} segundos, Memória: {memoria_adicao_pilha / 1024:.4f}KB")
    print("-------------------------------------------------------------------------------------------------------------------")
    print(f"Fila (Adicionar Itens)- Tempo: {tempo_fila:.10f} segundos, Memória: {memoria_fila / 1024:.4f}KB")
    print(f"Fila (Remover Itens) - Tempo: {tempo_remocao_fila:.10f} segundos, Memória: {memoria_remocao_fila / 1024:.4f}KB")

    print(f"Fila (Unidade) - Tempo: {tempo_adicao_fila:.10f} segundos, Memória: {memoria_adicao_fila / 1024:.4f}KB")
    print("-------------------------------------------------------------------------------------------------------------------")
    print(f"TabelaHash (Adicionar Itens)- Tempo: {tempo_tabela:.10f} segundos, Memória: {memoria_tabela / 1024:.4f}KB")
    print(f"TabelaHash (Remover Itens) - Tempo: {tempo_remocao_tabela:.10f} segundos, Memória: {memoria_remocao_tabela / 1024:.4f}KB")
    print(f"TabelaHash (Unidade) - Tempo: {tempo_adicao_tabela:.10f} segundos, Memória: {memoria_adicao_tabela / 1024:.4f}KB")

if __name__ == "__main__":
    main()