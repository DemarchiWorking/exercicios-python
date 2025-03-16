import os
from flask import Flask, render_template
import threading
import requests
import time

app = Flask(__name__)

notas_estudantes = [
    {"nome": "Alice", "nota": 9.0},
    {"nome": "Bruno", "nota": 7.5},
    {"nome": "Carlos", "nota": 8.2},
]

@app.route('/')
def inicio():
    return render_template("notas.html", estudantes=notas_estudantes)

def iniciar_servidor():
    app.run(port=8080, debug=True, use_reloader=False)

def aguardar_servidor(url="http://localhost:8080", tempo_limite=10):
    inicio = time.time()
    while time.time() - inicio < tempo_limite:
        try:
            resposta = requests.get(url)
            if resposta.status_code == 200:
                print("Servidor está funcionando!")
                return
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)
    raise Exception("O servidor não iniciou dentro do prazo!")

def acessar_pagina(url="http://localhost:8080"):
    resposta = requests.get(url)
    print("Código de Status:", resposta.status_code)
    print("Conteúdo da Página:")
    print(resposta.text)

if __name__ == "__main__":
    pasta_templates = "templates"
    os.makedirs(pasta_templates, exist_ok=True)
    with open(os.path.join(pasta_templates, "notas.html"), "w") as arquivo:
        arquivo.write("""<!DOCTYPE html>
<html lang=\"pt\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Notas dos Estudantes</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        table { width: 50%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f4f4f4; }
    </style>
</head>
<body>
    <h1>Notas dos Estudantes</h1>
    <table>
        <tr>
            <th>Nome</th>
            <th>Nota</th>
        </tr>
        {% for estudante in estudantes %}
        <tr>
            <td>{{ estudante.nome }}</td>
            <td>{{ estudante.nota }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>""")

    servidor_thread = threading.Thread(target=iniciar_servidor, daemon=True)
    servidor_thread.start()

    aguardar_servidor()
    acessar_pagina()
