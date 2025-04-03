import time
import matplotlib.pyplot as plt
from flask import Flask, jsonify

app = Flask(__name__)


def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n - 1, source, auxiliary, target)
        hanoi(n - 1, auxiliary, target, source)


@app.route('/hanoi/<int:discos>')
def solve_hanoi(discos):
    start_time = time.perf_counter()
    hanoi(discos, 'A', 'C', 'B')
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000  # Convertendo para ms
    return jsonify({'discos': discos, 'tempo': execution_time})


if __name__ == '__main__':
    tempos = []
    discos = [1, 5, 10, 15, 20, 25, 26,27, 28, 29, 30]

    for n in discos:
        start_time = time.perf_counter()
        hanoi(n, 'A', 'C', 'B')
        end_time = time.perf_counter()
        tempos.append((end_time - start_time) * 1000)

    plt.figure(figsize=(10, 6))
    plt.plot(discos, tempos, marker='o')
    plt.xlabel('Número de Discos')
    plt.ylabel('Tempo de Execução (ms)')
    plt.title('Tempo de Execução para Resolver as Torres de Hanói')
    plt.grid(True)
    plt.savefig('hanoi_tempo_execucao.png')
    plt.show()

    app.run(debug=True)
