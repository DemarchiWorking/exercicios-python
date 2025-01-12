import asyncio
import aiohttp
import time
import matplotlib.pyplot as plt
from flask import Flask, render_template, send_file
import io

app = Flask(__name__)

async def baixar_url(sessao, url):
    async with sessao.get(url) as resposta:
        conteudo = await resposta.text()
        print(f"Baixado {url}: {len(conteudo)} bytes")

async def baixar_todas(urls, num_downloads_concorrentes):
    async with aiohttp.ClientSession() as sessao:
        tarefas = []
        for i in range(0, len(urls), num_downloads_concorrentes):
            chunk = urls[i:i + num_downloads_concorrentes]
            tarefas += [baixar_url(sessao, url) for url in chunk]
        await asyncio.gather(*tarefas)

def medir_tempo(urls, num_downloads_concorrentes):
    inicio_tempo = time.time()
    asyncio.run(baixar_todas(urls, num_downloads_concorrentes))
    fim_tempo = time.time()
    return fim_tempo - inicio_tempo

@app.route('/')
def index():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/photos",
        "https://jsonplaceholder.typicode.com/todos",
        "https://jsonplaceholder.typicode.com/users"
    ]

    num_downloads_concorrentes_lista = [1, 2, 3, 4, 5, 6, 7, 8]
    tempos = []

    for num_downloads_concorrentes in num_downloads_concorrentes_lista:
        tempo_gasto = medir_tempo(urls, num_downloads_concorrentes)
        tempos.append(tempo_gasto)
        print(f"Downloads: {num_downloads_concorrentes}, Tempo: {tempo_gasto:.2f} segundos")

    plt.plot(num_downloads_concorrentes_lista, tempos, marker='o')
    plt.xlabel('Número de downloads concorrentes')
    plt.ylabel('Tempo (segundos)')
    plt.title('Número de downloads concorrentes vs Tempo')
    plt.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

