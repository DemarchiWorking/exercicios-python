import heapq


class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_bairro(self, bairro):
        if bairro not in self.vertices:
            self.vertices[bairro] = {}

    def adicionar_rua(self, bairro1, bairro2, distancia):
        self.vertices[bairro1][bairro2] = distancia
        self.vertices[bairro2][bairro1] = distancia

    def dijkstra(self, origem, destino):
        distancias = {bairro: float('inf') for bairro in self.vertices}
        distancias[origem] = 0
        fila_prioridade = [(0, origem)]
        predecessores = {}

        while fila_prioridade:
            distancia_atual, bairro_atual = heapq.heappop(fila_prioridade)

            if bairro_atual == destino:
                break

            for vizinho, peso in self.vertices[bairro_atual].items():
                nova_distancia = distancia_atual + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = bairro_atual
                    heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

        caminho = []
        bairro_atual = destino
        while bairro_atual in predecessores:
            caminho.append(bairro_atual)
            bairro_atual = predecessores[bairro_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, distancias[destino]

grafo_cidade = Grafo()
bairros = ["CD", "A", "B", "C", "D", "E", "F"]

for bairro in bairros:
    grafo_cidade.adicionar_bairro(bairro)

ruas = [
    ("CD", "A", 4),
    ("CD", "B", 2),
    ("A", "C", 5),
    ("A", "D", 10),
    ("B", "A", 3),
    ("B", "D", 8),
    ("C", "D", 2),
    ("C", "E", 4),
    ("D", "E", 6),
    ("D", "F", 5),
    ("E", "F", 3)
]

for bairro1, bairro2, distancia in ruas:
    grafo_cidade.adicionar_rua(bairro1, bairro2, distancia)

origem = "CD"
destino = "F"
rota_otima, custo_total = grafo_cidade.dijkstra(origem, destino)

print(f"Rota ótima: {' -> '.join(rota_otima)}")
print(f"Custo total: {custo_total} km")