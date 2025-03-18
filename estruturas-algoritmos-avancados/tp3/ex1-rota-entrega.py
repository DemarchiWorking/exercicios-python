class GrafoPoderado:
    def __init__(self):
        self.vertices = {}

    def adicionar_cidade(self, cidade):
        if cidade not in self.vertices:
            self.vertices[cidade] = {}

    def adicionar_estrada(self, cidade1, cidade2, distancia):
        self.vertices[cidade1][cidade2] = distancia
        self.vertices[cidade2][cidade1] = distancia

    def dijkstra(self, origem):
        nao_visitados = list(self.vertices.keys())
        distancias = {cidade: float("inf") for cidade in self.vertices}
        distancias[origem] = 0
        predecessores = {}

        while nao_visitados:
            cidade_atual = min(nao_visitados, key=lambda cidade: distancias[cidade])

            if distancias[cidade_atual] == float("inf"):
                break

            for vizinho, distancia in self.vertices[cidade_atual].items():
                nova_distancia = distancias[cidade_atual] + distancia
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = cidade_atual

            nao_visitados.remove(cidade_atual)

        return distancias, predecessores

    def reconstruir_caminho(self, origem, destino, predecessores):
        caminho = []
        cidade_atual = destino
        while cidade_atual in predecessores:
            caminho.append(cidade_atual)
            cidade_atual = predecessores[cidade_atual]
        caminho.append(origem)
        caminho.reverse()
        return caminho

mapa_cidades = GrafoPoderado()
cidades = ["Sé", "Pinheiros", "Mooca", "Vila Mariana", "Butantã"]

for cidade in cidades:
    mapa_cidades.adicionar_cidade(cidade)

estradas = [
    ("Sé", "Pinheiros", 2),
    ("Sé", "Mooca", 4),
    ("Pinheiros", "Vila Mariana", 1),
    ("Mooca", "Vila Mariana", 3),
    ("Mooca", "Butantã", 2),
    ("Vila Mariana", "Butantã", 2)
]

for cidade1, cidade2, distancia in estradas:
    mapa_cidades.adicionar_estrada(cidade1, cidade2, distancia)

distancias, predecessores = mapa_cidades.dijkstra("Sé")


print("Menores distâncias da Sé:")
for bairro, distancia in distancias.items():
    print(f"{bairro}: {distancia} km")

print("\nCaminhos da Sé até cada bairro:")
for bairro in cidades:
    if bairro != "Sé":
        caminho = mapa_cidades.reconstruir_caminho("Sé", bairro, predecessores)
        print(f"Sé => {bairro}: {' => '.join(caminho)}")
