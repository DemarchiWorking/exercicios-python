import time

movimentos = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]
def dentro_tabuleiro(x, y, N):
    return 0 <= x < N and 0 <= y < N

def resolver_cavalo(tabuleiro, x, y, passo, N):
    if passo == N * N:
        return True

    for dx, dy in movimentos:
        nx, ny = x + dx, y + dy
        if dentro_tabuleiro(nx, ny, N) and tabuleiro[nx][ny] == -1:
            tabuleiro[nx][ny] = passo
            if resolver_cavalo(tabuleiro, nx, ny, passo + 1, N):
                return True
            tabuleiro[nx][ny] = -1

    return False

def iniciar_passeio(N, inicio_x=0, inicio_y=0):
    start_time = time.perf_counter()
    tabuleiro = [[-1 for _ in range(N)] for _ in range(N)]
    tabuleiro[inicio_x][inicio_y] = 0

    if resolver_cavalo(tabuleiro, inicio_x, inicio_y, 1, N):
        end_time = time.perf_counter()
        tempo_execucao = (end_time - start_time) * 1000
        return tabuleiro, tempo_execucao
    else:
        end_time = time.perf_counter()
        tempo_execucao = (end_time - start_time) * 1000
        print("nao ha solucao para o problema do cavalo.")
        print(f"tempo de execucao: {tempo_execucao:.5f} ms")
        return None, tempo_execucao

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(f"{num:2}" for num in linha))

N = 8
solucao, tempo_execucao = iniciar_passeio(N)

if solucao:
    print("passeio do cavalo encontrado:")
    imprimir_tabuleiro(solucao)
    print(f"tempo de execucao: {tempo_execucao:.5f} ms")
else:
    print("(erro) falha.")

