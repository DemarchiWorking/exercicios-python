from flask import Flask, render_template_string
import matplotlib.pyplot as plt
import random
import io
import base64

app = Flask(__name__)

def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

def generate_items(num_items, seed=None):
    if seed is not None:
        random.seed(seed)  # Definindo uma semente aleatória
    weights = [random.randint(1, 100) for _ in range(num_items)]
    values = [random.randint(1, 100) for _ in range(num_items)]
    return weights, values

def measure_knapsack(num_items, capacity):
    seed = random.randint(0, 10000)  # Gerando uma semente aleatória diferente a cada vez
    weights, values = generate_items(num_items, seed)
    max_value = knapsack(values, weights, capacity)
    print(f"Semente: {seed}")
    print(f"Número de Itens: {num_items}, Capacidade: {capacity}")
    print(f"Pesos: {weights}")
    print(f"Valores: {values}")
    print(f"Valor Máximo: {max_value}")
    return max_value

@app.route('/')
def plot():
    num_items_list = [10, 20, 30, 40, 50]
    capacity = 100
    results = [measure_knapsack(num_items, capacity) for num_items in num_items_list]

    plt.figure(figsize=(10, 5))
    plt.plot(num_items_list, results, marker='o')
    plt.xlabel('Número de Itens')
    plt.ylabel('Valor Máximo')
    plt.title('Problema da Mochila: Programação Dinâmica')
    plt.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    html = f'<img src="data:image/png;base64,{plot_url}"/>'
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
