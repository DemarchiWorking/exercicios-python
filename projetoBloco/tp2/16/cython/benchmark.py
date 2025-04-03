# benchmark.py
import time
import numpy as np
import busca_arvore
import matplotlib.pyplot as plt
from statistics import median


def run_benchmark():
    sizes = [2 ** i for i in range(5, 22)]  # 32 a 2.097.152 nós
    results = []

    for size in sizes:
        print(f"\nTesting size: {size:,}")
        values = np.arange(size, dtype=np.int32)
        tree = busca_arvore.create_tree(values)
        target = size - 1  # Pior caso (último elemento)

        # Número de repetições baseado no tamanho
        repetitions = max(1000 // size, 10) if size < 10000 else max(100000 // size, 5)

        # Medição sequencial
        seq_times = []
        for _ in range(repetitions):
            start = time.perf_counter_ns()
            result = busca_arvore.sequential_search(tree, target)
            end = time.perf_counter_ns()
            seq_times.append((end - start) / 1e6)  # converter para ms
            assert result == 1  # Verifica que encontrou o alvo

        # Medição paralela
        par_times = []
        for _ in range(repetitions):
            start = time.perf_counter_ns()
            result = busca_arvore.parallel_search(tree, target)
            end = time.perf_counter_ns()
            par_times.append((end - start) / 1e6)  # converter para ms
            assert result == 1  # Verifica que encontrou o alvo

        # Calcula estatísticas
        seq_median = median(seq_times)
        par_median = median(par_times)
        speedup = seq_median / par_median if par_median > 0 else 0

        results.append((size, seq_median, par_median, speedup))
        print(f"Size: {size:10,} | Seq: {seq_median:9.6f} ms | Par: {par_median:9.6f} ms | Speedup: {speedup:6.3f}x")

    # Processamento dos resultados
    sizes, seq_times, par_times, speedups = zip(*results)

    # Plot
    plt.figure(figsize=(14, 7))
    plt.plot(sizes, seq_times, 'go-', label='Sequencial')
    plt.plot(sizes, par_times, 'bo-', label='Paralelo')
    plt.xscale('log', base=2)
    plt.yscale('log')
    plt.xlabel('Tamanho da Árvore (nós)', fontsize=12)
    plt.ylabel('Tempo Médio (ms)', fontsize=12)
    plt.title('Busca em Árvore Binária: Desempenho Sequencial vs. Paralelo', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)

    # Adiciona valores de speedup ao gráfico
    for i, size in enumerate(sizes):
        if i % 2 == 0:  # Mostra apenas alguns para não poluir
            plt.annotate(f'{speedups[i]:.2f}x',
                         (size, par_times[i]),
                         textcoords="offset points",
                         xytext=(0, 10),
                         ha='center',
                         fontsize=9)

    plt.tight_layout()
    plt.savefig('benchmark_results.png', dpi=300, bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    run_benchmark()