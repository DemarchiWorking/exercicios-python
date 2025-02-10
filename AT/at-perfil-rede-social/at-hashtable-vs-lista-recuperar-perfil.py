import time
import random
from flask import Flask, render_template_string
import matplotlib.pyplot as plt
import os


# Implementação da Hashtable
class RedeSocialHashtable:
    def __init__(self):
        self.usuarios = {}

    def adicionar_usuario(self, nome_usuario, perfil):
        self.usuarios[nome_usuario] = perfil

    def recuperar_perfil(self, nome_usuario):
        perfil = self.usuarios.get(nome_usuario, "Usuário não encontrado")
        print(perfil)
        return perfil


# Implementação da Lista Sequencial
class RedeSocialLista:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, nome_usuario, perfil):
        self.usuarios.append((nome_usuario, perfil))

    def recuperar_perfil(self, nome_usuario):
        for usuario, perfil in self.usuarios:
            if usuario == nome_usuario:
                print(perfil)
                return perfil
        return "Usuário não encontrado"


# Função para medir o tempo total de recuperação
def medir_tempo_total(recuperar_func, nome_usuario):
    inicio_tempo = time.perf_counter()
    resultado = recuperar_func(nome_usuario)
    fim_tempo = time.perf_counter()
    return fim_tempo - inicio_tempo, resultado


# Configuração do Flask
app = Flask(__name__)


@app.route('/')
def index():
    # Adicionar 100000 usuários na hashtable e na lista sequencial
    hashtable = RedeSocialHashtable()
    lista = RedeSocialLista()

    for i in range(1000000):
        nome_usuario = f'usuario{i}'
        perfil = {'id': i, 'nome': f'usuario{i}', 'idade': {random.randint(18, 50)}}
        hashtable.adicionar_usuario(nome_usuario, perfil)
        lista.adicionar_usuario(nome_usuario, perfil)

    # Escolher um nome de usuário aleatório para a busca
    nome_usuario_aleatorio = f'usuario{random.randint(0, 999999)}'

    # Medir tempo total de recuperação para ambos
    tempo_total_hashtable, _ = medir_tempo_total(hashtable.recuperar_perfil, nome_usuario_aleatorio)
    tempo_total_lista, _ = medir_tempo_total(lista.recuperar_perfil, nome_usuario_aleatorio)

    # Plotar gráfico
    fig, ax = plt.subplots()
    ax.bar(['Hashtable', 'Lista Sequencial'], [tempo_total_hashtable, tempo_total_lista], color=['blue', 'green'])
    ax.set_title('Tempo de Recuperação: Hashtable vs Lista Sequencial')
    ax.set_ylabel('Tempo (segundos)')

    # Salvar gráfico na pasta static
    static_path = os.path.join(app.root_path, 'static')
    if not os.path.exists(static_path):
        os.makedirs(static_path)
    plot_path = os.path.join(static_path, 'comparacao_de_tempo.png')
    plt.savefig(plot_path)

    # Renderizar templates com tempos de recuperação
    html_template = '''
        <h1>Tempo de Recuperação: Hashtable vs Lista Sequencial</h1>
        <img src="/static/comparacao_de_tempo.png" alt="Gráfico de Comparação de Tempo">
        <p>Tempo de recuperação na Hashtable: {{ "%.10f" | format(tempo_total_hashtable) }} segundos</p>
        <p>Tempo de recuperação na Lista Sequencial: {{ "%.10f" | format(tempo_total_lista) }} segundos</p>
    '''

    return render_template_string(html_template, tempo_total_hashtable=tempo_total_hashtable,
                                  tempo_total_lista=tempo_total_lista)


if __name__ == '__main__':
    app.run(debug=True)
