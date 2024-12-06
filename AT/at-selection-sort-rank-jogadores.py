def selection_sort_jogadores(jogadores):
    n = len(jogadores)
    # Loop externo para cada posição na lista de jogadores
    for j in range(n-1):
        max_index = j
        # Loop interno para encontrar o jogador com a maior pontuação na parte não ordenada da lista
        for i in range(j+1, n):
            if jogadores[i]['pontuacao'] > jogadores[max_index]['pontuacao']:
                max_index = i
        # Se o jogador com a maior pontuação encontrado for maior que o jogador na posição j, troca os jogadores
        if jogadores[j]['pontuacao'] < jogadores[max_index]['pontuacao']:
            aux = jogadores[j]
            jogadores[j] = jogadores[max_index]
            jogadores[max_index] = aux
    return jogadores


# Lista de jogadores
jogadores = [
    {"id": 1, "nome": "Antonio Demarchi", "pontuacao": 9000},
    {"id": 2, "nome": "Debora Amaral", "pontuacao": 9200},
    {"id": 3, "nome": "Rogerio Ribas", "pontuacao": 8800},
    {"id": 4, "nome": "Daniel Zuckerman", "pontuacao": 8900}
]
# Ordenar jogadores por pontuação ranking
jogadores_ordenados = selection_sort_jogadores(jogadores)

# Imprimir jogadores ordenados

for index, jogador in enumerate(jogadores_ordenados, start=1):
    print(f"Ranking: {index}, ID: {jogador['id']}, Nome: {jogador['nome']}, Pontuação: {jogador['pontuacao']}")

