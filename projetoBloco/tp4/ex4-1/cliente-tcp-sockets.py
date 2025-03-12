import socket

HOST = "servidor"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.sendall(b"Receba!\n")

data = client.recv(1024)
print(f"Resposta do servidor: {data.decode()}")

client.close()
