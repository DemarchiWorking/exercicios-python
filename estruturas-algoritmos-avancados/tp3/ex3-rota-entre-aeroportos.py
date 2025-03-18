import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_aeroporto(self, aeroporto):
        if aeroporto not in self.vertices:
            self.vertices[aeroporto] = {}

    def adicionar_rota(self, origem, destino, distancia):
        self.vertices[origem][destino] = distancia
        self.vertices[destino][origem] = distancia

    def dijkstra(self, origem, destino):
        distancias = {aeroporto: float('inf') for aeroporto in self.vertices}
        distancias[origem] = 0
        fila_prioridade = [(0, origem)]
        predecessores = {}

        while fila_prioridade:
            distancia_atual, aeroporto_atual = heapq.heappop(fila_prioridade)

            if aeroporto_atual == destino:
                break

            for vizinho, distancia in self.vertices[aeroporto_atual].items():
                nova_distancia = distancia_atual + distancia
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = aeroporto_atual
                    heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

        caminho = []
        aeroporto_atual = destino
        while aeroporto_atual in predecessores:
            caminho.append(aeroporto_atual)
            aeroporto_atual = predecessores[aeroporto_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, distancias[destino]


rede_aerea = Grafo()

aeroportos = ["Rio de Janeiro", "São Paulo", "Belo Horizonte", "Brasília", "Salvador"]
for aeroporto in aeroportos:
    rede_aerea.adicionar_aeroporto(aeroporto)

rotas = [
    ("Rio de Janeiro", "São Paulo", 430),
    ("Rio de Janeiro", "Belo Horizonte", 440),
    ("São Paulo", "Brasília", 1015),
    ("Belo Horizonte", "Brasília", 625),
    ("Brasília", "Salvador", 1440),
    ("Salvador", "Rio de Janeiro", 1650)
]

for origem, destino, distancia in rotas:
    rede_aerea.adicionar_rota(origem, destino, distancia)

origem = "Rio de Janeiro"
destino = "Salvador"
rota, distancia_total = rede_aerea.dijkstra(origem, destino)

print(f"Menor rota entre {origem} e {destino}: {' => '.join(rota)}")
print(f"Distância total: {distancia_total} km")
