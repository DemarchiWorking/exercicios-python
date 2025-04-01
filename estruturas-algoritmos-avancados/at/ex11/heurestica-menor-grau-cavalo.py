import time

movimentos = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]
def dentro_tabuleiro(x, y, N):
    return 0 <= x < N and 0 <= y < N

def grau_saida(tabuleiro, x, y, N):
    grau = 0
    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if dentro_tabuleiro(nx, ny, N) and tabuleiro[nx][ny] == -1:
            grau += 1
    return grau

def proximo_movimento(tabuleiro, x, y, N):
    melhor_movimento = None
    menor_grau = float('inf')

    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if dentro_tabuleiro(nx, ny, N) and tabuleiro[nx][ny] == -1:
            grau = grau_saida(tabuleiro, nx, ny, N)
            if grau < menor_grau:
                menor_grau = grau
                melhor_movimento = (nx, ny)

    return melhor_movimento


def resolver_cavalo(tabuleiro, x, y, passo, N):
    if passo == N * N:
        return True

    proximo = proximo_movimento(tabuleiro, x, y, N)
    while proximo:
        nx, ny = proximo
        tabuleiro[nx][ny] = passo
        if resolver_cavalo(tabuleiro, nx, ny, passo + 1, N):
            return True
        tabuleiro[nx][ny] = -1
        proximo = proximo_movimento(tabuleiro, x, y, N)

    return False


def iniciar_passeio(N, inicio_x=0, inicio_y=0):
    tabuleiro = [[-1 for _ in range(N)] for _ in range(N)]
    tabuleiro[inicio_x][inicio_y] = 0

    inicio_tempo = time.perf_counter()
    if resolver_cavalo(tabuleiro, inicio_x, inicio_y, 1, N):
        fim_tempo = time.perf_counter()
        tempo_execucao = fim_tempo - inicio_tempo
        print(f"tempo de execucao tabuleiro {N}x{N}: {tempo_execucao:.6f} segundos")
        return tabuleiro
    else:
        fim_tempo = time.perf_counter()
        tempo_execucao = fim_tempo - inicio_tempo
        print(f"nao tem solucao tabuleiro {N}x{N}. tempo: {tempo_execucao:.6f} segundos")
        return None


def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(f"{num:2}" for num in linha))


tamanhos = [5, 8, 10]
for N in tamanhos:
    print(f"tabuleiro {N}x{N}:")
    solucao = iniciar_passeio(N)
    if solucao:
        print(f"encontrado para {N}x{N}:")
        imprimir_tabuleiro(solucao)
    print("-" * 50)