from flask import Flask, render_template_string
import random
import string
import time
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-j-1):
            if lista[i]['preco'] > lista[i+1]['preco']:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

def gerar_produtos(num):
    return [
        {
            "id": i,
            "nome": ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
            "preco": random.uniform(1.0, 100.0)
        }
        for i in range(num)
    ]

def medir_tempo(funcao_ordenar, dados):
    tempo_inicial = time.time()
    funcao_ordenar(dados)
    tempo_final = time.time()
    return tempo_final - tempo_inicial

@app.route('/')
def index():
    tempo_1000 = [medir_tempo(bubble_sort, gerar_produtos(1000)) for _ in range(2)]
    tempo_10000 = [medir_tempo(bubble_sort, gerar_produtos(10000)) for _ in range(2)]
    avg_time_1000 = sum(tempo_1000) / len(tempo_1000)
    avg_time_10000 = sum(tempo_10000) / len(tempo_10000)

    tempos = {
        '1000': avg_time_1000,
        '10000': avg_time_10000
    }

    fig, ax = plt.subplots()
    ax.plot(tempos.keys(), tempos.values(), marker='o')
    ax.set_title('Média de Tempo de Execução do Bubble Sort')
    ax.set_xlabel('Quantidade de Itens')
    ax.set_ylabel('Tempo (segundos)')

    caminho = os.path.join(app.root_path, 'static')
    if not os.path.exists(caminho):
        os.makedirs(caminho)
    plot_path = os.path.join(caminho, 'plot.png')
    plt.savefig(plot_path)

    return render_template_string('''
        <h1>Média de Tempo de Execução do Bubble Sort</h1>
        <img src="/static/plot.png" alt="Gráfico de Tempo de Execução">
    ''')

if __name__ == '__main__':
    app.run(debug=True)
