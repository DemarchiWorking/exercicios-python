import time
from multiprocessing import Pool
import numpy as np
from functools import reduce


def generate_list(size):
    return np.random.randint(1, 1000, size).tolist()


def sequential_sum(numbers):
    start_time = time.perf_counter()
    result = sum(numbers)
    end_time = time.perf_counter()
    return result, (end_time - start_time) * 1000  # Convertendo para ms


def partial_sum(chunk):
    return sum(chunk)


def parallel_sum(numbers, num_threads=4):
    start_time = time.perf_counter()

    chunk_size = len(numbers) // num_threads
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

    with Pool(processes=num_threads) as pool:
        partial_results = pool.map(partial_sum, chunks)

    total = sum(partial_results)
    end_time = time.perf_counter()

    return total, (end_time - start_time) * 1000  # Convertendo para ms


def perf_test(list_size, thread_configs=[1, 2, 4, 8]):
    numbers = generate_list(list_size)
    print(f"\nTeste com lista de tamanho: {list_size}")
    print("-" * 50)

    seq_result, seq_time = sequential_sum(numbers)
    print(f"Sequencial - Resultado: {seq_result}, Tempo: {seq_time:.2f} ms")

    for threads in thread_configs:
        par_result, par_time = parallel_sum(numbers, threads)
        speedup = seq_time / par_time if par_time > 0 else 0
        print(f"Paralelo ({threads} threads) - Resultado: {par_result}, "
              f"Tempo: {par_time:.2f} ms, Speedup: {speedup:.2f}x")


def main():
    test_sizes = [1000000, 5000000, 10000000]  # 1M, 5M, 10M elementos

    for size in test_sizes:
        perf_test(size)

    sample_list = generate_list(100)
    seq_sum, _ = sequential_sum(sample_list)
    par_sum, _ = parallel_sum(sample_list, 4)
    print(f"\nVerificação de consistência:")
    print(f"Soma Sequencial: {seq_sum}")
    print(f"Soma Paralela: {par_sum}")
    print(f"Resultados iguais: {seq_sum == par_sum}")


if __name__ == '__main__':
    main()