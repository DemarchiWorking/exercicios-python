import multiprocessing
import time
from flask import Flask, render_template_string
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def e_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def contar_primos_sequencial(inicio, fim):
    contador = 0
    for numero in range(inicio, fim):
        if e_primo(numero):
            contador += 1
    return contador

def contar_primos_em_intervalo(intervalo):
    inicio, fim = intervalo
    contador = 0
    for numero in range(inicio, fim):
        if e_primo(numero):
            contador += 1
    return contador

def contar_primos_paralelo(inicio, fim):
    num_processos = multiprocessing.cpu_count()
    tamanho_intervalo = (fim - inicio) // num_processos
    intervalos = [(inicio + i * tamanho_intervalo, inicio + (i + 1) * tamanho_intervalo) for i in range(num_processos)]
    intervalos[-1] = (intervalos[-1][0], fim)

    with multiprocessing.Pool(processes=num_processos) as pool:
        contagem_parcial = pool.map(contar_primos_em_intervalo, intervalos)

    total_primos = sum(contagem_parcial)
    return total_primos

@app.route('/')
def comparar_tempos():
    inicio = 1
    fim = 1000000  # Aumentando o intervalo para 1.000.000

    inicio_tempo_sequencial = time.time()
    total_primos_sequencial = contar_primos_sequencial(inicio, fim)
    fim_tempo_sequencial = time.time()
    tempo_sequencial = fim_tempo_sequencial - inicio_tempo_sequencial

    inicio_tempo_paralelo = time.time()
    total_primos_paralelo = contar_primos_paralelo(inicio, fim)
    fim_tempo_paralelo = time.time()
    tempo_paralelo = fim_tempo_paralelo - inicio_tempo_paralelo

    labels = ['Sequencial', 'Paralelo']
    tempos = [tempo_sequencial, tempo_paralelo]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, tempos, color=['blue', 'orange'])
    plt.xlabel('Método')
    plt.ylabel('Tempo (segundos)')
    plt.title('Comparação de Tempos de Execução: Sequencial vs. Paralelo')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imagem_png = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    template = """
    <!doctype html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Comparação de Desempenho</title>
    </head>
    <body>
        <h1>Comparação de Tempos de Execução: Sequencial vs. Paralelo</h1>
        <img src="data:image/png;base64,{{ imagem_png }}" alt="Gráfico de desempenho">
        <p>Total de números primos entre {{ inicio }} e {{ fim }} (sequencial): {{ total_primos_sequencial }}</p>
        <p>Tempo de execução (sequencial): {{ tempo_sequencial }} segundos</p>
        <p>Total de números primos entre {{ inicio }} e {{ fim }} (paralelo): {{ total_primos_paralelo }}</p>
        <p>Tempo de execução (paralelo): {{ tempo_paralelo }} segundos</p>
    </body>
    </html>
    """

    return render_template_string(template, imagem_png=imagem_png,
                                  inicio=inicio, fim=fim,
                                  total_primos_sequencial=total_primos_sequencial, tempo_sequencial=f"{tempo_sequencial:.4f}",
                                  total_primos_paralelo=total_primos_paralelo, tempo_paralelo=f"{tempo_paralelo:.4f}")

if __name__ == "__main__":
    app.run(debug=True)
