import time
from time import perf_counter
from flask import Flask, render_template_string
import random
import io
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_brute_force(coins, amount):
    if amount == 0:
        return 0
    min_coins = float('inf')
    for coin in coins:
        if amount - coin >= 0:
            num_coins = coin_change_brute_force(coins, amount - coin)
            if num_coins != float('inf'):
                min_coins = min(min_coins, num_coins + 1)
    return min_coins

def measure_time(func, coins, amount):
    start_time = perf_counter()
    result = func(coins, amount)
    end_time = perf_counter()
    elapsed_time = round((end_time - start_time) * 1000, 10)
    return result, elapsed_time

@app.route('/')
def plot():
    coins = [1, 5, 10, 25, 50, 100]
    amounts = list(range(1, 51))

    dp_times = []
    bf_times = []

    for amount in amounts:
        dp_result, dp_time = measure_time(coin_change_dp, coins, amount)
        bf_result, bf_time = measure_time(coin_change_brute_force, coins, amount)
        dp_times.append(dp_time)
        bf_times.append(bf_time)
        print(f"Valor: {amount}, DP (ms): {dp_time:.10f}, Bruteforce (ms): {bf_time:.10f}, Resultados: DP - {dp_result}, BF - {bf_result}")

    plt.figure(figsize=(12, 7))
    plt.plot(amounts, dp_times, label='Prog. Dinâmica', marker='o')
    plt.plot(amounts, bf_times, label='Força Bruta', marker='o')
    plt.xlabel('Valor (centavos)')
    plt.ylabel('Tempo de Execução (ms)')
    plt.title('Comparação de Tempo: Prog. Dinâmica vs Força Bruta com Moedas')
    plt.legend()
    plt.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    html = f"""
    <h1>Problema do Troco de Moedas</h1>
    <h2>Gráfico de Tempo de Execução</h2>
    <img src="data:image/png;base64,{plot_url}"/>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
