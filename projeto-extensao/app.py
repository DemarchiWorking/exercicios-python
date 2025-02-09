from flask import Flask, request, render_template, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

# Conectando ao banco de dados SQLite
def conectar_banco():
    conexao = sqlite3.connect('banco_de_dados.db')
    return conexao

# Criando a tabela no banco de dados
def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projetos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo_projeto TEXT,
            categoria TEXT,
            contato TEXT,
            nome TEXT,
            descricao TEXT,
            autor TEXT
        )
    ''')
    conexao.commit()
    conexao.close()

# Truncar descrição para exibir no template
def truncar_descricao(descricao, limite=30):
    if len(descricao) > limite:
        return descricao[:limite] + "..."
    return descricao

# Página inicial com o formulário
@app.route('/')
def formulario():
    autor = request.args.get('autor')
    return render_template('formulario.html', autor=autor)

# Rota para processar o formulário
@app.route('/processar', methods=['POST'])
def processar_formulario():
    titulo_projeto = request.form['titulo_projeto']
    categoria = request.form['categoria']
    contato = request.form['contato']
    nome = request.form['nome']
    descricao = request.form['descricao']
    autor = request.form['autor']

    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO projetos (titulo_projeto, categoria, contato, nome, descricao, autor)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (titulo_projeto, categoria, contato, nome, descricao, autor))
    conexao.commit()
    conexao.close()

    return redirect(url_for('formulario', autor=autor))

# Rota para listar todos os projetos
@app.route('/projetos')
def listar_projetos():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT id, titulo_projeto, categoria, descricao, nome, autor FROM projetos')
    projetos = cursor.fetchall()
    conexao.close()

    # Truncar descrições
    projetos = [(id, titulo, categoria, truncar_descricao(descricao), nome, autor) for id, titulo, categoria, descricao, nome, autor in projetos]
    return render_template('lista_projetos.html', projetos=projetos)

@app.route('/detalhe/<int:id>')
def get_projeto_by_id(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    query = "SELECT id, titulo_projeto, categoria, descricao, nome, autor FROM projetos WHERE id = :id"
    cursor.execute(query, {"id": id})
    projeto = cursor.fetchone()
    conexao.close()

    if projeto:
        projeto_dict = {
            'id': projeto[0],
            'titulo_projeto': projeto[1],
            'categoria': projeto[2],
            'descricao': projeto[3],
            'nome': projeto[4],
            'autor': projeto[5]
        }
        return jsonify(projeto_dict)
    else:
        return jsonify({'error': 'Projeto não encontrado'}), 404

# Rota para deletar um projeto
@app.route('/deletar/<int:id>')
def deletar_projeto(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM projetos WHERE id = ?', (id,))
    conexao.commit()
    conexao.close()
    return redirect(url_for('listar_projetos'))

if __name__ == '__main__':
    criar_tabela()
    app.run(host='0.0.0.0', port=5000)

