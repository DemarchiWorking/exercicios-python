from flask import Flask, request, send_from_directory
import os

PASTA_DE_ENVIO = "arquivos"
os.makedirs(PASTA_DE_ENVIO, exist_ok=True)

aplicativo = Flask(__name__)
aplicativo.config["PASTA_DE_ENVIO"] = PASTA_DE_ENVIO


@aplicativo.route("/enviar", methods=["POST"])
def enviar_arquivo():
    if "arquivo" not in request.files:
        return {"mensagem": "Nenhum arquivo foi recebido"}, 400
    arquivo = request.files["arquivo"]
    if arquivo.filename == "":
        return {"mensagem": "O nome do arquivo não é válido"}, 400
    arquivo.save(os.path.join(aplicativo.config["PASTA_DE_ENVIO"], arquivo.filename))
    return {"mensagem": f"Arquivo {arquivo.filename} enviado com sucesso!"}, 200


@aplicativo.route("/baixar/<nome_do_arquivo>", methods=["GET"])
def baixar_arquivo(nome_do_arquivo):
    return send_from_directory(aplicativo.config["PASTA_DE_ENVIO"], nome_do_arquivo, as_attachment=True)

if __name__ == "__main__":
    aplicativo.run(host="0.0.0.0", port=5000, debug=True)