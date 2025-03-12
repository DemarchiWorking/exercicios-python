import socket

HOST = "servidor"
PORT = 5000


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

data = client.recv(1024)
print(f"Servidor: {data.decode()}")


try:
    while True:
        mensagem = input("Digite a msg para o servidor: ")
        client.sendall(mensagem.encode())
        resposta = client.recv(1024)
        print(f"Servidor: {resposta.decode()}")
except KeyboardInterrupt:
    print("Fechando ..")
finally:
    client.close()
