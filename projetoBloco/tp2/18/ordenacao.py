import concurrent.futures
import time
import random
import matplotlib.pyplot as plt
from flask import Flask
import io
import base64


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result


def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_left = executor.submit(parallel_merge_sort, left)
        future_right = executor.submit(parallel_merge_sort, right)
        left = future_left.result()
        right = future_right.result()

    return merge(left, right)


def sequential_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = sequential_merge_sort(arr[:middle])
    right = sequential_merge_sort(arr[middle:])

    return merge(left, right)


def measure_sort_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time


# Lista de exemplo
arr = [random.randint(0, 1000) for _ in range(1000)]
parallel_time = measure_sort_time(parallel_merge_sort, arr.copy())
sequential_time = measure_sort_time(sequential_merge_sort, arr.copy())

print(f"Tempo de execução paralelo: {parallel_time:.4f} segundos")
print(f"Tempo de execução sequencial: {sequential_time:.4f} segundos")

app = Flask(__name__)


@app.route('/')
def plot():
    sizes = [2 ** i for i in range(10, 15)]
    parallel_times = []
    sequential_times = []

    for size in sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        parallel_times.append(measure_sort_time(parallel_merge_sort, arr.copy()))
        sequential_times.append(measure_sort_time(sequential_merge_sort, arr.copy()))

    plt.figure()
    plt.plot(sizes, parallel_times, label='Paralelo', marker='o')
    plt.plot(sizes, sequential_times, label='Sequencial', marker='o')
    plt.xlabel('Tamanho da Lista')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Comparação de Performance: MergeSort Paralelo vs Sequencial')
    plt.legend()
    plt.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return f'<img src="data:image/png;base64,{plot_url}"/>'


if __name__ == '__main__':
    app.run(debug=True)
