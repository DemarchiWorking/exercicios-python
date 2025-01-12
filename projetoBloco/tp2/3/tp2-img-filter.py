import os
import asyncio
from PIL import Image, ImageFilter
import time
import matplotlib.pyplot as plt
from flask import Flask, render_template_string
import base64

# Função assíncrona para processar cada imagem
async def processar_imagem(caminho_imagem, dir_saida):
    img = Image.open(caminho_imagem)
    img = img.filter(ImageFilter.BLUR)
    img.save(os.path.join(dir_saida, os.path.basename(caminho_imagem)))

# Função principal para gerenciar o processamento assíncrono
async def main_processamento_imagens():
    dir_entrada = "input_images"
    dir_saida = "output_images"
    os.makedirs(dir_saida, exist_ok=True)
    imagens = [os.path.join(dir_entrada, img) for img in os.listdir(dir_entrada) if img.endswith(".jpg")]

    await asyncio.gather(*(processar_imagem(img, dir_saida) for img in imagens))

# Função para medir o tempo de execução
async def medir_tempo(num_threads):
    start_time = time.time()
    await main_processamento_imagens()
    end_time = time.time()
    return end_time - start_time

# Função para gerar o gráfico
async def gerar_grafico():
    num_threads = [1, 2, 4, 8, 16, 32]
    tempos = [await medir_tempo(n) for n in num_threads]

    plt.plot(num_threads, tempos, marker='o')
    plt.xlabel('Número de Threads')
    plt.ylabel('Tempo (segundos)')
    plt.title('Número de Threads x Tempo de Processamento')
    plt.savefig('grafico_tempo.png')

# Servidor Flask para exibir o gráfico
app = Flask(__name__)

@app.route('/')
async def index():
    await gerar_grafico()
    with open("grafico_tempo.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    img_tag = f'<img src="data:image/png;base64,{encoded_image}"/>'
    return render_template_string(f"<html><body>{img_tag}</body></html>")

if __name__ == "__main__":
    app.run(debug=True)
