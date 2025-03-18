import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_cidade(self, cidade):
        if cidade not in self.vertices:
            self.vertices[cidade] = {}

    def adicionar_rua(self, cidade1, cidade2, tempo):
        self.vertices[cidade1][cidade2] = tempo
        self.vertices[cidade2][cidade1] = tempo

    def dijkstra(self, origem, destino):
        distancias = {cidade: float('inf') for cidade in self.vertices}
        distancias[origem] = 0
        fila_prioridade = [(0, origem)]
        predecessores = {}

        while fila_prioridade:
            tempo_atual, cidade_atual = heapq.heappop(fila_prioridade)

            if cidade_atual == destino:
                break

            for vizinho, tempo in self.vertices[cidade_atual].items():
                nova_distancia = tempo_atual + tempo
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = cidade_atual
                    heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

        caminho = []
        cidade_atual = destino
        while cidade_atual in predecessores:
            caminho.append(cidade_atual)
            cidade_atual = predecessores[cidade_atual]
        caminho.append(origem)
        caminho.reverse()

        return caminho, distancias[destino]

cidade = Grafo()
cidades = ["São Paulo", "Campinas", "Sorocaba", "Santos", "Ribeirão Preto"]

for cidade_nome in cidades:
    cidade.adicionar_cidade(cidade_nome)

ruas = [
    ("São Paulo", "Campinas", 80),
    ("São Paulo", "Sorocaba", 100),
    ("Campinas", "Santos", 120),
    ("Sorocaba", "Santos", 150),
    ("Santos", "Ribeirão Preto", 200),
    ("Campinas", "Ribeirão Preto", 220)
]

for cidade1, cidade2, tempo in ruas:
    cidade.adicionar_rua(cidade1, cidade2, tempo)

origem = "São Paulo"
destino = "Ribeirão Preto"
rota, tempo_total = cidade.dijkstra(origem, destino)

print(f"Menor rota entre {origem} e {destino}: {' => '.join(rota)}")
print(f"Tempo total: {tempo_total} minutos")
