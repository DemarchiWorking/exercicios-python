from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///turma.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    nota = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "nota": self.nota}

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    data = request.json
    aluno = Aluno(nome=data['nome'], nota=data['nota'])
    db.session.add(aluno)
    db.session.commit()
    return jsonify(aluno.to_dict()), 201

@app.route('/listar', methods=['GET'])
def listar():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
