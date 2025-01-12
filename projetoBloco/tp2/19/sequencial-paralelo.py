import concurrent.futures
import time
import random
import matplotlib.pyplot as plt
from flask import Flask
import io
import base64

app = Flask(__name__)


def max_sequential(arr):
    return max(arr)


def max_parallel(arr, num_threads=4):
    def find_max_sublist(sublist):
        return max(sublist)

    chunk_size = len(arr) // num_threads
    sublists = [arr[i * chunk_size: (i + 1) * chunk_size] for i in range(num_threads)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(find_max_sublist, sublists))

    return max(results)


def measure_time(func, arr):
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    return result, (end_time - start_time) * 1000  # Convertendo para milissegundos


@app.route('/')
def plot():
    sizes = [2 ** i for i in range(10, 15)]
    parallel_max_times = []
    sequential_max_times = []

    for size in sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        _, seq_time = measure_time(max_sequential, arr)
        _, par_time = measure_time(lambda arr: max_parallel(arr, num_threads=4), arr)
        sequential_max_times.append(seq_time)
        parallel_max_times.append(par_time)

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, parallel_max_times, label='Paralelo', marker='o')
    plt.plot(sizes, sequential_max_times, label='Sequencial', marker='o')
    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo de Execução (ms)')
    plt.title('Comparação de Performance: Máximo Paralelo vs Sequencial')
    plt.legend()
    plt.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return f'<img src="data:image/png;base64,{plot_url}"/>'


if __name__ == '__main__':
    app.run(debug=True)
