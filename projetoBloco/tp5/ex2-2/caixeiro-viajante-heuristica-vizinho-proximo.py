import timeit

def calcular_distancia(cidade1, cidade2):
    x1, y1 = cidade1
    x2, y2 = cidade2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def encontrar_vizinho_mais_proximo(cidade_atual, cidades_nao_visitadas):
    menor_distancia = float('inf')
    cidade_mais_proxima = None
    for cidade, coordenadas in cidades_nao_visitadas.items():
        distancia = calcular_distancia(cidade_atual, coordenadas)
        if distancia < menor_distancia:
            menor_distancia = distancia
            cidade_mais_proxima = cidade
    return cidade_mais_proxima, menor_distancia

def tsp_vizinho_mais_proximo(cidades):
    cidade_inicial = list(cidades.keys())[0]
    caminho = [cidade_inicial]
    cidades_nao_visitadas = dict(cidades)
    cidade_atual = cidades_nao_visitadas.pop(cidade_inicial)
    distancia_total = 0

    while cidades_nao_visitadas:
        proxima_cidade, distancia = encontrar_vizinho_mais_proximo(cidade_atual, cidades_nao_visitadas)
        caminho.append(proxima_cidade)
        cidade_atual = cidades_nao_visitadas.pop(proxima_cidade)
        distancia_total += distancia

    distancia_total += calcular_distancia(cidade_atual, cidades[caminho[0]])
    caminho.append(caminho[0])

    return caminho, distancia_total

def exibir_resultados(caminho, distancia):
    print("Melhor caminho encontrado (na ordem de visita):")
    print(" -> ".join(caminho))
    print(f"Distância total percorrida: {distancia:.2f}")

cidades = {
    "A": (0, 0),
    "B": (1, 5),
    "C": (5, 2),
    "D": (6, 6),
    "E": (8, 3)
}

def medir_execucao():
    caminho, distancia = tsp_vizinho_mais_proximo(cidades)
    exibir_resultados(caminho, distancia)

tempo_execucao = timeit.timeit("medir_execucao()", globals=globals(), number=1)
print(f"Tempo de execução: {tempo_execucao * 1000:.2f} ms")
