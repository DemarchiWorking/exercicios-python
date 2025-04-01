import time
import random

def medir_tempo(funcao, *args):
    inicio = time.perf_counter()
    resultado = funcao(*args)
    fim = time.perf_counter()
    tempo = (fim - inicio) * 1000

    return resultado, tempo

def vizinho_mais_proximo(matriz_distancias):
    num_cidades = len(matriz_distancias)
    visitado = [False] * num_cidades
    caminho = [0]
    visitado[0] = True
    custo_total = 0

    for _ in range(num_cidades - 1):
        ultima_cidade = caminho[-1]
        menor_distancia = float('inf')
        proxima_cidade = None

        for cidade in range(num_cidades):
            if not visitado[cidade] and matriz_distancias[ultima_cidade][cidade] < menor_distancia:
                menor_distancia = matriz_distancias[ultima_cidade][cidade]
                proxima_cidade = cidade

        caminho.append(proxima_cidade)
        visitado[proxima_cidade] = True
        custo_total += menor_distancia

    custo_total += matriz_distancias[caminho[-1]][0]
    caminho.append(0)

    return caminho, custo_total

def algoritmo_genetico(matriz_distancias, tamanho_populacao=50, geracoes=100, taxa_mutacao=0.1):
    def calcular_custo(caminho):
        return sum(matriz_distancias[caminho[i-1]][caminho[i]] for i in range(len(caminho)))

    def gerar_populacao_inicial():
        populacao = []
        for _ in range(tamanho_populacao):
            individuo = list(range(len(matriz_distancias)))
            random.shuffle(individuo)
            populacao.append(individuo + [individuo[0]])
        return populacao

    def crossover(pai1, pai2):
        tamanho = len(pai1) - 1
        inicio, fim = sorted(random.sample(range(tamanho), 2))
        filho = [-1] * tamanho
        filho[inicio:fim + 1] = pai1[inicio:fim + 1]
        preenchidos = set(pai1[inicio:fim + 1])
        idx = 0
        for gene in pai2:
            if gene not in preenchidos:
                while idx < tamanho and filho[idx] != -1:
                    idx += 1
                if idx < tamanho:
                    filho[idx] = gene
        return filho + [filho[0]]

    def mutacao(individuo):
        i, j = sorted(random.sample(range(len(individuo) - 1), 2))
        individuo[i], individuo[j] = individuo[j], individuo[i]

    num_cidades = len(matriz_distancias)
    populacao = gerar_populacao_inicial()

    for _ in range(geracoes):
        populacao = sorted(populacao, key=lambda ind: calcular_custo(ind))
        nova_populacao = populacao[:tamanho_populacao // 2]
        while len(nova_populacao) < tamanho_populacao:
            pai1, pai2 = random.sample(nova_populacao[:tamanho_populacao // 4], 2)
            filho = crossover(pai1, pai2)
            if random.random() < taxa_mutacao:
                mutacao(filho)
            nova_populacao.append(filho)

        populacao = nova_populacao

    melhor_solucao = min(populacao, key=lambda ind: calcular_custo(ind))
    return melhor_solucao, calcular_custo(melhor_solucao)

distancias = [
    [0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140],
    [10, 0, 35, 25, 30, 40, 45, 50, 55, 20, 65, 30, 75, 80, 85, 90, 95, 50, 100, 55, 110, 115, 120, 65, 125, 130, 135, 70],
    [15, 35, 0, 30, 20, 50, 60, 15, 70, 55, 25, 80, 35, 90, 40, 95, 45, 100, 50, 105, 55, 110, 60, 115, 65, 120, 70, 125],
    [20, 25, 30, 0, 15, 10, 70, 65, 60, 55, 50, 20, 45, 30, 75, 25, 80, 70, 85, 35, 90, 75, 95, 40, 100, 80, 105, 45],
    [25, 30, 20, 15, 0, 35, 80, 75, 70, 65, 60, 55, 50, 45, 85, 40, 90, 80, 95, 45, 100, 85, 105, 50, 110, 90, 115, 55],
    [30, 40, 50, 10, 35, 0, 90, 85, 80, 75, 70, 65, 60, 55, 95, 50, 100, 90, 105, 55, 110, 95, 115, 60, 120, 100, 125, 65],
    [35, 45, 60, 70, 80, 90, 0, 10, 20, 30, 40, 50, 60, 70, 15, 80, 20, 85, 25, 90, 30, 95, 35, 100, 40, 105, 45, 110],
    [40, 50, 15, 65, 75, 85, 10, 0, 35, 45, 55, 20, 65, 30, 80, 90, 85, 95, 90, 100, 95, 105, 100, 110, 105, 115, 110, 120],
    [45, 55, 70, 60, 70, 80, 20, 35, 0, 25, 15, 30, 40, 50, 85, 60, 90, 95, 95, 105, 100, 110, 115, 120, 125, 130, 135, 140],
]

resultado_vizinho_mp, tempo_vmp = medir_tempo(vizinho_mais_proximo, distancias)
print("vizinho mais proximo=")
print("caminho=", resultado_vizinho_mp[0])
print("custo=", resultado_vizinho_mp[1])
print(f"tempo de execucao= {tempo_vmp:.5f} ms")

resultado_genetico, tempo_genetico = medir_tempo(algoritmo_genetico, distancias)
print("algoritmo genetico=")
print("caminho=", resultado_genetico[0])
print("custo=", resultado_genetico[1])
print(f"tempo de execucao= {tempo_genetico:.5f} ms")
