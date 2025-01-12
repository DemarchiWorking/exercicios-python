from multiprocessing import Pool
import time
import matplotlib.pyplot as plt
from flask import Flask, jsonify, send_file
import io

app = Flask(__name__)

def sum_parallel(lst):
    chunk_size = len(lst) // 4  # Dividindo a lista em 4 partes
    chunks = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
    with Pool(4) as pool:
        results = pool.map(sum, chunks)
    return sum(results)

def sum_sequential(lst):
    return sum(lst)

@app.route('/compare')
def compare_sums():
    large_list = list(range(1, 10001))

    # Medindo o tempo da soma paralela
    start_time = time.perf_counter()
    parallel_sum = sum_parallel(large_list)
    end_time = time.perf_counter()
    parallel_time = (end_time - start_time) * 1000  # Convertendo para ms

    # Medindo o tempo da soma sequencial
    start_time = time.perf_counter()
    sequential_sum = sum_sequential(large_list)
    end_time = time.perf_counter()
    sequential_time = (end_time - start_time) * 1000  # Convertendo para ms

    # Criando o gráfico de barras
    labels = ['Paralela', 'Sequencial']
    times = [parallel_time, sequential_time]

    fig, ax = plt.subplots()
    ax.bar(labels, times, color=['blue', 'green'])
    ax.set_xlabel('Método')
    ax.set_ylabel('Tempo de Execução (ms)')
    ax.set_title('Comparação de Tempo de Execução: Soma Paralela vs. Sequencial')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    large_list = list(range(1, 10001))

    # Medindo o tempo da soma paralela
    start_time = time.perf_counter()
    parallel_sum = sum_parallel(large_list)
    end_time = time.perf_counter()
    parallel_time = (end_time - start_time) * 1000  # Convertendo para ms
    print(f"Soma paralela: {parallel_sum}, Tempo: {parallel_time:.10f} ms")

    # Medindo o tempo da soma sequencial
    start_time = time.perf_counter()
    sequential_sum = sum_sequential(large_list)
    end_time = time.perf_counter()
    sequential_time = (end_time - start_time) * 1000  # Convertendo para ms
    print(f"Soma sequencial: {sequential_sum}, Tempo: {sequential_time:.10f} ms")

    app.run(debug=True)
