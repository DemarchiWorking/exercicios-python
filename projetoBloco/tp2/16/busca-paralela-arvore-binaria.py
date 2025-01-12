from multiprocessing import Process, Value
import time
import matplotlib.pyplot as plt
from flask import Flask, jsonify, send_file, redirect
import io

app = Flask(__name__)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def parallel_search(root, target):
    def search_subtree(node, target, found):
        if node is None or found.value:
            return
        if node.value == target:
            found.value = True
            return
        search_subtree(node.left, target, found)
        search_subtree(node.right, target, found)

    found = Value('b', False)
    left_proc = Process(target=search_subtree, args=(root.left, target, found))
    right_proc = Process(target=search_subtree, args=(root.right, target, found))

    left_proc.start()
    right_proc.start()
    left_proc.join()
    right_proc.join()

    return found.value


def build_tree(values):
    nodes = [TreeNode(v) for v in values]
    for i in range(len(nodes) // 2):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0] if nodes else None


def sequential_search(root, target):
    def search_subtree(node, target):
        if node is None:
            return False
        if node.value == target:
            return True
        return search_subtree(node.left, target) or search_subtree(node.right, target)

    return search_subtree(root, target)


@app.route('/')
def home():
    return redirect('/compare')


@app.route('/compare')
def compare_search():
    sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    parallel_times = []
    sequential_times = []

    for size in sizes:
        values = list(range(size))
        root = build_tree(values)
        target = size - 1

        # Busca paralela
        start_time = time.perf_counter()
        parallel_search(root, target)
        end_time = time.perf_counter()
        parallel_time = (end_time - start_time) * 1000  # Convertendo para ms
        parallel_times.append(parallel_time)

        # Busca sequencial
        start_time = time.perf_counter()
        sequential_search(root, target)
        end_time = time.perf_counter()
        sequential_time = (end_time - start_time) * 1000  # Convertendo para ms
        sequential_times.append(sequential_time)

    # Criando o gráfico de barras
    fig, ax = plt.subplots()
    ax.bar([str(size) for size in sizes], parallel_times, color='blue', label='Paralela')
    ax.bar([str(size) for size in sizes], sequential_times, color='green', label='Sequencial', alpha=0.5)
    ax.set_xlabel('Tamanho da Árvore (nós)')
    ax.set_ylabel('Tempo de Execução (ms)')
    ax.set_title('Comparação de Tempo de Execução: Busca Paralela vs. Sequencial')
    ax.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return send_file(img, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
