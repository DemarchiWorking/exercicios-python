import time
import matplotlib.pyplot as plt
from flask import Flask, jsonify

app = Flask(__name__)


def permute(s, answer):
    if len(s) == 0:
        print(answer)
        return
    used = set()
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        if ch not in used:  # Trata duplicações
            permute(rest, answer + ch)
        used.add(ch)


@app.route('/permute/<string>')
def solve_permute(string):
    start_time = time.perf_counter()
    permute(string, "")
    end_time = time.perf_counter()
    execution_time = end_time - start_time  # Tempo em segundos
    return jsonify({'string': string, 'tempo': execution_time})


if __name__ == '__main__':
    strings = ["A", "AB", "ABC", "ABCD", "ABCDE", "ABCDEF"]
    tempos = []

    for s in strings:
        start_time = time.perf_counter()
        permute(s, "")
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        tempos.append(execution_time)
        print(f"Tempo para '{s}': {execution_time:.4f} segundos")

    plt.figure(figsize=(10, 6))
    plt.plot(strings, tempos, marker='o')
    plt.xlabel('String')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Tempo de Execução para Gerar Permutações de uma String')
    plt.grid(True)
    plt.savefig('permutations_tempo_execucao.png')
    plt.show()

    app.run(debug=True)
