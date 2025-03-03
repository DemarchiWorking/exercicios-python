from collections import deque

# ======= Mapa das Conexões
conexoes = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}


#=====Função para Explorar as Conexões (BFS)
def explorar(conexoes, inicio):
    ja_vistos = set()  # Conjunto para marcar os pontos visitados
    fila_de_visita = deque([inicio])  # Fila para armazenar os pontos temporários
    ordem_dos_pontos = []  # Lista para registrar a ordem dos pontos visitados

    while fila_de_visita:
        ponto = fila_de_visita.popleft()  # Remove o primeiro ponto da fila
        if ponto not in ja_vistos:
            ja_vistos.add(ponto)  # Marca como visitado
            ordem_dos_pontos.append(ponto)

            # Adiciona pontos não visitados à fila
            for vizinho in conexoes[ponto]:
                if vizinho not in ja_vistos:
                    fila_de_visita.append(vizinho)

    return ordem_dos_pontos


# ===== Iniciando a exploração das conexões a partir do 'A'====
ordem_visita = explorar(conexoes, 'A')

# Resultado
print("Ordem pontos visitados a partir de 'A':")
print(" -> ".join(ordem_visita))
