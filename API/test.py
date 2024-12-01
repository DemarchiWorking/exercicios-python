from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Estudar estrutura de Dados", "completa": True}
]

@app.route("/tarefa", methods=['GET'])
def obter_tarefa():
    return jsonify(tarefas)

@app.route("/tarefa", methods=['POST'])
def adicionar_tarefa():
    dados = request.get_json()
    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": dados.get("titulo"),
        "completa": False,
    }
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

@app.route("/tarefa/<int:tarefa_id>/completar", methods=['PUT'])
def completar_tarefa(tarefa_id):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["completa"] = True
            return jsonify(tarefa), 200
    return jsonify({"erro": "Tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
