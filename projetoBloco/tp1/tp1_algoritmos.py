import time


def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        return [linha.strip() for linha in arquivo]


def escrever_arquivo(caminho_arquivo, lista):
    with open(caminho_arquivo, 'w') as arquivo:
        for item in lista:
            arquivo.write(f"{item}\n")


# Algoritmos de Ordenação 1
def bubble_sort(lista):
    n = len(lista)
    for j in range(n - 1):
        for i in range(n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

#2
def selection_sort(lista):
    n = len(lista)
    for j in range(n - 1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux

#3
def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = chave


# Função para medir o tempo de execução
def medir_tempo(ordenacao_funcao, lista):
    inicio_tempo = time.time()
    ordenacao_funcao(lista)
    fim_tempo = time.time()
    return fim_tempo - inicio_tempo


def calcular_media_tempo(ordenacao_funcao, lista, repeticoes=10):
    tempos = []
    for _ in range(repeticoes):
        lista_copia = lista.copy()
        tempo_execucao = medir_tempo(ordenacao_funcao, lista_copia)
        tempos.append(tempo_execucao)
    media_tempo = sum(tempos) / repeticoes
    return media_tempo


def main():
    caminho_listagem = 'listagem_arquivos_ordena.txt'
    lista_arquivos = ler_arquivo(caminho_listagem)

    # Medir e registrar o tempo de execução para cada algoritmo
    tempos_execucao = {
        'Bubble Sort': calcular_media_tempo(bubble_sort, lista_arquivos),
        'Selection Sort': calcular_media_tempo(selection_sort, lista_arquivos),
        'Insertion Sort': calcular_media_tempo(insertion_sort, lista_arquivos)
    }

    # Escrever listagem ordenada em arquivos separados usando os algoritmos
    lista_ordenada_bubble = lista_arquivos.copy()
    bubble_sort(lista_ordenada_bubble)
    escrever_arquivo('bubble_sorted.txt', lista_ordenada_bubble)

    lista_ordenada_selection = lista_arquivos.copy()
    selection_sort(lista_ordenada_selection)
    escrever_arquivo('selection_sorted.txt', lista_ordenada_selection)

    lista_ordenada_insertion = lista_arquivos.copy()
    insertion_sort(lista_ordenada_insertion)
    escrever_arquivo('insertion_sorted.txt', lista_ordenada_insertion)

    for metodo, tempo in tempos_execucao.items():
        print(f"{metodo}: {tempo:.6f} segundos")


if __name__ == "__main__":
    main()
