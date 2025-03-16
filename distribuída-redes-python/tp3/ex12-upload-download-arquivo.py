import requests

URL_DO_SERVIDOR = "http://localhost:5000"

def enviar_arquivo_para_servidor(caminho_arquivo):
    with open(caminho_arquivo, "rb") as arquivo:
        resposta = requests.post(f"{URL_DO_SERVIDOR}/enviar", files={"arquivo": arquivo})
    print(resposta.json())

def baixar_arquivo_do_servidor(nome_arquivo, caminho_para_salvar):
    resposta = requests.get(f"{URL_DO_SERVIDOR}/baixar/{nome_arquivo}")
    if resposta.status_code == 200:
        with open(caminho_para_salvar, "wb") as arquivo:
            arquivo.write(resposta.content)
        print(f"O arquivo {nome_arquivo} foi baixado com sucesso para {caminho_para_salvar}")
    else:
        print(f"Erro ao tentar baixar o arquivo: {resposta.json()}")

if __name__ == "__main__":
    while True:
        print("\n1. Enviar um arquivo")
        print("2. Baixar um arquivo")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            caminho_arquivo = input("Digite o caminho do arquivo que deseja enviar: ")
            enviar_arquivo_para_servidor(caminho_arquivo)
        elif opcao == "2":
            nome_arquivo = input("Digite o nome do arquivo que deseja baixar: ")
            caminho_para_salvar = input("Digite o caminho onde deseja salvar o arquivo: ")
            baixar_arquivo_do_servidor(nome_arquivo, caminho_para_salvar)
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")
