class Grafo:
    def __init__(self, vertices):
        self.bairros = vertices
        self.num_vertices = len(vertices)
        self.INF = float('inf')
        self.matriz = [[self.INF for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
        for i in range(self.num_vertices):
            self.matriz[i][i] = 0

    def adicionar_rua(self, bairro1, bairro2, tempo):
        try:
            i = self.bairros.index(bairro1)
            j = self.bairros.index(bairro2)
            self.matriz[i][j] = tempo
        except ValueError:
            print(f"Erro: Um dos bairros ({bairro1}, {bairro2}) não existe no grafo.")

    def floyd_warshall(self):
        dist = [[self.INF for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]

        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.matriz[i][j] != self.INF:
                    dist[i][j] = self.matriz[i][j]
                else:
                    dist[i][j] = self.INF
            dist[i][i] = 0

        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if dist[i][k] != self.INF and dist[k][j] != self.INF:
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]

        return dist

bairros = ['A', 'B', 'C', 'D', 'E', 'F']
grafo_cidade = Grafo(bairros)

ruas = [
    ('A', 'B', 5),
    ('A', 'C', 10),
    ('B', 'C', 3),
    ('B', 'D', 8),
    ('C', 'D', 2),
    ('C', 'E', 7),
    ('D', 'E', 4),
    ('D', 'F', 6),
    ('E', 'F', 5)
]

for bairro1, bairro2, tempo in ruas:
    grafo_cidade.adicionar_rua(bairro1, bairro2, tempo)

print("Matriz de adjacência (grafo ponderado):")
print("   ", end="")
for bairro in bairros:
    print(f"{bairro:>4}", end="")

for i in range(len(bairros)):
    print(f"{bairros[i]}: ", end="")
    for j in range(len(bairros)):
        if grafo_cidade.matriz[i][j] == grafo_cidade.INF:
            print(" INF", end="")
        else:
            print(f"{grafo_cidade.matriz[i][j]:>4}", end="")
    print()

distancias = grafo_cidade.floyd_warshall()

print("matriz de menores tempos de viagem entre todos os pares de bairros:")
print("   ", end="")
for bairro in bairros:
    print(f"{bairro:>4}", end="")
print()
for i in range(len(bairros)):
    print(f"{bairros[i]}: ", end="")
    for j in range(len(bairros)):
        if distancias[i][j] == grafo_cidade.INF:
            print(" INF", end="")
        else:
            print(f"{distancias[i][j]:>4}", end="")
    print()

print("=================================================")
bairro_origem = 'A'
bairro_destino = 'F'
i = bairros.index(bairro_origem)
j = bairros.index(bairro_destino)

if distancias[i][j] == grafo_cidade.INF:
    print(f"Não há rota disponível para viajar do Bairro {bairro_origem} até o Bairro {bairro_destino}.")
else:
    print(f"O tempo mínimo para viajar do Bairro {bairro_origem} até o Bairro {bairro_destino} é: {distancias[i][j]} minutos.")
