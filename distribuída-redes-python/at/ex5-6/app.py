from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


alunos = []

@app.route('/')
def home():
    return render_template('listar_alunos.html', alunos=alunos)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        nota = float(request.form['nota'])
        alunos.append({'nome': nome, 'nota': nota})
        return redirect(url_for('home'))
    return render_template('cadastrar.html')

@app.route('/listar')
def listar():
    ordenados = sorted(alunos, key=lambda x: x['nota'], reverse=True)
    return render_template('listar_alunos.html', alunos=ordenados)

if __name__ == '__main__':
    app.run(debug=True)
