# benchmark.py
import numpy as np
import time
import soma_paralela
import matplotlib.pyplot as plt


def executar_testes():
    tamanhos = [1_000_000, 5_000_000, 10_000_000]
    threads = [1, 2, 4, 8]

    resultados = []

    for tamanho in tamanhos:
        print(f"\nTeste com lista de tamanho: {tamanho}")
        print("--------------------------------------------------")

        arr = np.arange(1, tamanho + 1, dtype=np.int64)

        # Teste sequencial
        start = time.perf_counter()
        resultado_seq = soma_paralela.soma_sequencial(arr)
        tempo_seq = (time.perf_counter() - start) * 1000

        print(f"Sequencial - Resultado: {resultado_seq}, Tempo: {tempo_seq:.2f} ms")

        # Testes paralelos
        for t in threads:
            start = time.perf_counter()
            resultado_par = soma_paralela.soma_paralela(arr, t)
            tempo_par = (time.perf_counter() - start) * 1000

            speedup = tempo_seq / tempo_par
            print(
                f"Paralelo ({t} threads) - Resultado: {resultado_par}, Tempo: {tempo_par:.2f} ms, Speedup: {speedup:.2f}x")

            resultados.append({
                'tamanho': tamanho,
                'threads': t,
                'sequencial_ms': tempo_seq,
                'paralelo_ms': tempo_par,
                'speedup': speedup
            })

    return resultados


def plotar_resultados(resultados):
    tamanhos = sorted({r['tamanho'] for r in resultados})

    for tamanho in tamanhos:
        dados = [r for r in resultados if r['tamanho'] == tamanho]
        threads = [d['threads'] for d in dados]
        tempos = [d['paralelo_ms'] for d in dados]

        plt.figure()
        plt.bar([str(t) for t in threads], tempos)
        plt.xlabel('Número de Threads')
        plt.ylabel('Tempo (ms)')
        plt.title(f'Desempenho Paralelo - Tamanho {tamanho:,}')
        plt.savefig(f'cython_desempenho_{tamanho}.png')
        plt.close()


if __name__ == '__main__':
    # Compila os módulos Cython
    print("Compilando módulos Cython...")
    from subprocess import run

    run(["python", "setup.py", "build_ext", "--inplace"], check=True)

    resultados = executar_testes()
    plotar_resultados(resultados)

    # Verificação final
    print("\nVerificação de consistência:")
    arr_pequeno = np.arange(1, 1001, dtype=np.int64)
    soma_seq = soma_paralela.soma_sequencial(arr_pequeno)
    soma_par = soma_paralela.soma_paralela(arr_pequeno, 2)
    print(f"Soma Sequencial: {soma_seq}")
    print(f"Soma Paralela: {soma_par}")
    print(f"Resultados iguais: {soma_seq == soma_par}")