import requests

def acessar_servidor(url="http://localhost:8080"):
    try:

        resposta = requests.get(url)
        if resposta.status_code == 200:
            print("Conexão bem-sucedida ao servidor!")
            print("Conteúdo recebido:")
            print(resposta.text)
        else:
            print(f"Servidor respondeu com código: {resposta.status_code}")
    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível conectar ao servidor.")
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro durante a requisição: {e}")


if __name__ == "__main__":
    url_servidor = "http://localhost:8080"
    acessar_servidor(url_servidor)
