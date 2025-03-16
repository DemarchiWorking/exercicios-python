import socket

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Escutando na {PORT}...")

while True:
    conn, addr = server.accept()
    print(f"Conexão recebida de {addr}")
    conn.sendall(b"Bemvindo ao Servidor TCP!")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Cliente disse: {data.decode()}")
        resposta = input("Digite sua resposta para o cliente: ")
        conn.sendall(resposta.encode())
    conn.close()
