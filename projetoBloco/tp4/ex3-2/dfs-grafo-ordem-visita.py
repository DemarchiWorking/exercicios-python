import time

class Grafo:
    def __init__(self, orientado=False):
        self.orientado = orientado
        self.lista_adjacencia = {}

    def adicionar_arestas(self, arestas):
        for origem, destino in arestas:
            if origem not in self.lista_adjacencia:
                self.lista_adjacencia[origem] = []
            if destino not in self.lista_adjacencia[origem]:
                self.lista_adjacencia[origem].append(destino)
            if not self.orientado:
                if destino not in self.lista_adjacencia:
                    self.lista_adjacencia[destino] = []
                if origem not in self.lista_adjacencia[destino]:
                    self.lista_adjacencia[destino].append(origem)

    def exibir_grafo(self):
        print("Lista de Adjacência:")
        for vertice, vizinhos in sorted(self.lista_adjacencia.items()):
            print(f"{vertice} -> {', '.join(sorted(vizinhos))}")

    def dfs_nao_ordenado(self, inicio):
        visitados = set()
        resultado = []

        def dfs_recursivo(v):
            if v not in visitados:
                visitados.add(v)
                resultado.append(v)
                for vizinho in self.lista_adjacencia.get(v, []):
                    dfs_recursivo(vizinho)

        inicio_tempo = time.perf_counter_ns()
        dfs_recursivo(inicio)
        fim_tempo = time.perf_counter_ns()
        tempo_execucao = (fim_tempo - inicio_tempo) / 1_000_000

        print(f"DFS Não Ordenado: {resultado}")
        print(f"Tempo DFS Não Ordenado: {tempo_execucao:.6f} ms\n")
        return resultado, tempo_execucao

    def dfs_ordenado(self, inicio):
        visitados = set()
        resultado = []

        def dfs_recursivo(v):
            if v not in visitados:
                visitados.add(v)
                resultado.append(v)
                for vizinho in sorted(self.lista_adjacencia.get(v, [])):
                    dfs_recursivo(vizinho)

        inicio_tempo = time.perf_counter_ns()
        dfs_recursivo(inicio)
        fim_tempo = time.perf_counter_ns()
        tempo_execucao = (fim_tempo - inicio_tempo) / 1_000_000

        print(f"DFS Ordenado: {resultado}")
        print(f"Tempo DFS Ordenado: {tempo_execucao:.6f} ms\n")
        return resultado, tempo_execucao

    def executar(self, arestas):
        inicio_tempo = time.perf_counter_ns()
        self.adicionar_arestas(arestas)
        self.exibir_grafo()
        fim_tempo = time.perf_counter_ns()
        tempo_execucao = (fim_tempo - inicio_tempo) / 1_000_000
        print(f"Tempo para criar e exibir o grafo: {tempo_execucao:.6f} ms\n")
        return tempo_execucao


if __name__ == "__main__":
    arestas = [
        ("C", "A"), ("B", "D"), ("A", "E"), ("E", "F"), ("F", "C"),
        ("D", "G"), ("G", "H"), ("H", "I"), ("J", "B"), ("K", "L"),
        ("L", "M"), ("M", "N"), ("O", "P"), ("P", "Q"), ("R", "S"),
        ("S", "T"), ("T", "U"), ("U", "A"), ("B", "C"), ("E", "D")
    ]

    print("Grafo Não Orientado:")
    grafo_nao_orientado = Grafo(orientado=False)
    tempo_nao_orientado = grafo_nao_orientado.executar(arestas)
    print(f"Tempo para criar e mostrar o grafo não orientado: {tempo_nao_orientado:.6f} ms\n")

    tempo_dfs_nao_ordenado = grafo_nao_orientado.dfs_nao_ordenado("A")
    tempo_dfs_ordenado = grafo_nao_orientado.dfs_ordenado("A")

    print("Grafo Orientado:")
    grafo_orientado = Grafo(orientado=True)
    tempo_orientado = grafo_orientado.executar(arestas)
    print(f"Tempo para criar e mostrar o grafo orientado: {tempo_orientado:.6f} ms\n")

    tempo_dfs_nao_ordenado_orientado = grafo_orientado.dfs_nao_ordenado("A")
    tempo_dfs_ordenado_orientado = grafo_orientado.dfs_ordenado("A")

    print(" === Tempos DFS ===")
    print(f"DFS Não Ordenado (Não Orientado): {tempo_dfs_nao_ordenado[1]:.6f} ms")
    print(f"DFS Ordenado (Não Orientado): {tempo_dfs_ordenado[1]:.6f} ms")
    print(f"DFS Não Ordenado (Orientado): {tempo_dfs_nao_ordenado_orientado[1]:.6f} ms")
    print(f"DFS Ordenado (Orientado): {tempo_dfs_ordenado_orientado[1]:.6f} ms")