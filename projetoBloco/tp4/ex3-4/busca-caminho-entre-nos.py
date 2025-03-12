from collections import defaultdict, deque
import time


class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def adicionar_aresta(self, origem, destino):
        self.grafo[origem].append(destino)
        self.grafo[destino].append(origem)

    def buscar_caminho_bfs(self, inicio, fim):
        fila = deque([[inicio]])
        visitados = {inicio}

        if inicio == fim:
            return [inicio]

        while fila:
            caminho_atual = fila.popleft()
            ultimo_no = caminho_atual[-1]

            for vizinho in self.grafo[ultimo_no]:
                if vizinho not in visitados:
                    novo_caminho = caminho_atual + [vizinho]
                    if vizinho == fim:
                        return novo_caminho
                    visitados.add(vizinho)
                    fila.append(novo_caminho)

        return None

    def buscar_caminho_dfs(self, inicio, fim):
        visitados = set()

        def dfs_recursiva(no_atual, destino, caminho_atual):
            visitados.add(no_atual)
            caminho_atual.append(no_atual)

            if no_atual == destino:
                return caminho_atual

            for vizinho in self.grafo[no_atual]:
                if vizinho not in visitados:
                    resultado = dfs_recursiva(vizinho, destino, caminho_atual.copy())
                    if resultado:
                        return resultado

            return None

        return dfs_recursiva(inicio, fim, [])


def medir_tempo(grafo, inicio, fim, metodo, repeticoes=1000):
    tempo_total = 0

    for _ in range(repeticoes):
        inicio_tempo = time.perf_counter()
        if metodo == "BFS":
            grafo.buscar_caminho_bfs(inicio, fim)
        else:
            grafo.buscar_caminho_dfs(inicio, fim)
        fim_tempo = time.perf_counter()
        tempo_total += (fim_tempo - inicio_tempo) * 1000

    tempo_medio = tempo_total / repeticoes
    return tempo_medio


grafo = Grafo()
arestas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]

for origem, destino in arestas:
    grafo.adicionar_aresta(origem, destino)

testes = [
    ('A', 'E'),
]

print("Busca de caminhos no grafo:")


for inicio, fim in testes:
    caminho_bfs = grafo.buscar_caminho_bfs(inicio, fim)
    tempo_bfs = medir_tempo(grafo, inicio, fim, "BFS")

    caminho_dfs = grafo.buscar_caminho_dfs(inicio, fim)
    tempo_dfs = medir_tempo(grafo, inicio, fim, "DFS")

    print(f"De {inicio} até {fim}:")

    if caminho_bfs:
        print(f"BFS encontrou: {' -> '.join(caminho_bfs)}")
        print(f"Tempo médio BFS: {tempo_bfs:.4f} ms")
    else:
        print("BFS: Nenhum caminho encontrado")
        print(f"Tempo médio BFS: {tempo_bfs:.4f} ms")

    if caminho_dfs:
        print(f"DFS encontrou: {' -> '.join(caminho_dfs)}")
        print(f"Tempo médio DFS: {tempo_dfs:.4f} ms")
    else:
        print("DFS: Nenhum caminho encontrado")
        print(f"Tempo médio DFS: {tempo_dfs:.4f} ms")
