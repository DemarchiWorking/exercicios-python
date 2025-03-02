# Implementação Completa do Grafo
class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_cidade(self, cidade):
        if cidade not in self.adjacencia:
            self.adjacencia[cidade] = []

    def adicionar_estrada(self, cidade1, cidade2):
        if cidade1 not in self.adjacencia:
            self.adicionar_cidade(cidade1)
        if cidade2 not in self.adjacencia:
            self.adicionar_cidade(cidade2)

        # Estrada bidirecional
        self.adjacencia[cidade1].append(cidade2)
        self.adjacencia[cidade2].append(cidade1)

    def exibir_grafo(self):
        for cidade, estradas in self.adjacencia.items():
            print(f"{cidade}: {', '.join(estradas)}")

    def verificar_conexao(self, cidade1, cidade2):
        if cidade2 in self.adjacencia.get(cidade1, []):
            return f"Há uma estrada direta entre {cidade1} e {cidade2}."
        else:
            return f"Não há estrada direta entre {cidade1} e {cidade2}."


# Criando o grafo e adicionando cidades e estradas
meu_grafo = Grafo()
cidades = ['A', 'B', 'C', 'D', 'E', 'F']
estradas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')]

for cidade in cidades:
    meu_grafo.adicionar_cidade(cidade)

for cidade1, cidade2 in estradas:
    meu_grafo.adicionar_estrada(cidade1, cidade2)

# Exibindo o grafo
print("Lista de Adjacência do Grafo:")
meu_grafo.exibir_grafo()

# Testando conexões
print("\n" + meu_grafo.verificar_conexao('A', 'B'))
print(meu_grafo.verificar_conexao('A', 'E'))
