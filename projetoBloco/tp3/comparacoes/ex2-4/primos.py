import multiprocessing
import time
import math
import sys


def is_prime_optimized(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def contar_primos_sequencial(inicio, fim):
    return sum(1 for num in range(inicio, fim + 1) if is_prime_optimized(num))


def processar_bloco(args):
    inicio, fim = args
    return sum(1 for num in range(inicio, fim + 1) if is_prime_optimized(num))


def contar_primos_paralelo(inicio, fim, num_processos=None):
    try:
        if num_processos is None:
            num_processos = multiprocessing.cpu_count()

        tamanho_total = fim - inicio + 1
        tamanho_bloco = max(10000, tamanho_total // (num_processos * 4))

        blocos = []
        current = inicio
        while current <= fim:
            proximo = min(current + tamanho_bloco - 1, fim)
            blocos.append((current, proximo))
            current = proximo + 1

        with multiprocessing.Pool(processes=num_processos) as pool:
            pool.map(processar_bloco, [(1, 10)])

            start_time = time.perf_counter()
            resultados = pool.map(processar_bloco, blocos)
            tempo_par = time.perf_counter() - start_time

        return sum(resultados), tempo_par
    except Exception as e:
        print(f"Erro no paralelismo: {str(e)}", file=sys.stderr)
        return 0, float('inf')


def testar_desempenho(inicio, fim, repeticoes=3):
    print(f"\n{'=' * 60}")
    print(f"Teste para intervalo {inicio}-{fim}")
    print(f"{'=' * 60}")

    try:
        tempos_seq = []
        for _ in range(repeticoes):
            start = time.perf_counter()
            total_seq = contar_primos_sequencial(inicio, fim)
            tempos_seq.append(time.perf_counter() - start)
    except Exception as e:
        print(f"Erro sequencial: {str(e)}", file=sys.stderr)
        return

    tempos_par = []
    totais_par = []
    for _ in range(repeticoes):
        try:
            total_par, tempo_par = contar_primos_paralelo(inicio, fim)
            tempos_par.append(tempo_par)
            totais_par.append(total_par)
        except Exception as e:
            print(f"Erro na execução paralela: {str(e)}", file=sys.stderr)
            continue

    if not totais_par or not all(t == total_seq for t in totais_par):
        print("Aviso: Resultados inconsistentes!", file=sys.stderr)
        return

    melhor_seq = min(tempos_seq)
    media_seq = sum(tempos_seq) / len(tempos_seq)
    melhor_par = min(tempos_par) if tempos_par else float('inf')
    media_par = sum(tempos_par) / len(tempos_par) if tempos_par else float('inf')

    print(f"\nPrimos encontrados: {total_seq}")
    print(f"\n{'Método':<12}{'Melhor':<12}{'Média':<12}")
    print(f"{'-' * 36}")
    print(f"{'Sequencial':<12}{melhor_seq:.6f}s{media_seq:.6f}s")
    if melhor_par != float('inf'):
        print(f"{'Paralelo':<12}{melhor_par:.6f}s{media_par:.6f}s")
        speedup = melhor_seq / melhor_par
        print(f"\nSpeedup: {speedup:.2f}x")
        print(f"Eficiência: {speedup / multiprocessing.cpu_count() * 100:.1f}%")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    print("=== Comparação de Desempenho ===")

    intervalos = [
        (1, 1_000),
        (1, 5_000),
        (1, 10_000),
        (1, 50_000),
        (1, 100_000)
    ]

    for inicio, fim in intervalos:
        testar_desempenho(inicio, fim)

    print("\nTodos os testes concluídos com sucesso!")