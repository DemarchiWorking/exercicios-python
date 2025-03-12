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

    def executar(self, arestas):
        inicio = time.perf_counter_ns()
        self.adicionar_arestas(arestas)
        self.exibir_grafo()
        fim = time.perf_counter_ns()
        tempo_execucao = (fim - inicio) / 1_000_000
        return tempo_execucao


if __name__ == "__main__":
    arestas_exemplo = [
        ("C", "A"), ("B", "D"), ("A", "E"), ("E", "F"),
        ("F", "C"), ("D", "G"), ("G", "H"), ("H", "I"),
        ("J", "B"), ("K", "L"), ("L", "M"), ("M", "N"),
        ("O", "P"), ("P", "Q"), ("R", "S"), ("S", "T"),
        ("T", "U"), ("U", "A"), ("B", "C"), ("E", "D")
    ]

    print("Grafo NaoOrientado")
    grafo_nao_orientado = Grafo(orientado=False)
    tempo_nao_orientado = grafo_nao_orientado.executar(arestas_exemplo)
    print(f"Tempo para criar e mostrar o grafo nao orientado: {tempo_nao_orientado:.6f} ms\n")

    print("Grafo Orientado:")
    grafo_orientado = Grafo(orientado=True)
    tempo_orientado = grafo_orientado.executar(arestas_exemplo)
    print(f"Tempo para criar e mostrar grafo orientado: {tempo_orientado:.6f} ms\n")

    print(" === Tempos==")
    print(f"Grafo Não-Orientado: {tempo_nao_orientado:.6f} ms")
    print(f"Grafo Orientado: {tempo_orientado:.6f} ms")
