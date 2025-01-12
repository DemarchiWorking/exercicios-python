import concurrent.futures
import time
import matplotlib.pyplot as plt
from flask import Flask
import io
import base64

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_subtree(node, target, found):
    if node is None or found[0]:
        return
    if node.value == target:
        found[0] = True
        return
    search_subtree(node.left, target, found)
    search_subtree(node.right, target, found)

def parallel_search(root, target):
    found = [False]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_left = executor.submit(search_subtree, root.left, target, found)
        future_right = executor.submit(search_subtree, root.right, target, found)
        concurrent.futures.wait([future_left, future_right])

    return found[0]

def create_tree(size):
    root = TreeNode(1)
    current = root
    for i in range(2, size + 2):
        current.right = TreeNode(i)
        current = current.right
    return root

def measure_search_time(size, target):
    root = create_tree(size)
    start_time = time.time()
    parallel_search(root, target)
    end_time = time.time()
    return end_time - start_time

app = Flask(__name__)

@app.route('/')
def plot():
    sizes = [2**i for i in range(10)]
    times = [measure_search_time(size, size) for size in sizes]  # Corrigido: usar size diretamente para target

    plt.figure()
    plt.plot(sizes, times, marker='o')
    plt.xlabel('Tamanho da Árvore (nós)')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Tempo de Execução da Busca Paralela')
    plt.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return f'<img src="data:image/png;base64,{plot_url}"/>'

if __name__ == '__main__':
    app.run(debug=True)
