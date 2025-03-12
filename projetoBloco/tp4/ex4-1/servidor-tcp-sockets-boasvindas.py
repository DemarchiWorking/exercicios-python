import socket

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Servidor escutando na {PORT}...")

while True:
    conn, addr = server.accept()
    print(f"Conexão recebida de {addr}")
    conn.sendall(b"Bemvindo ao Servidor TCP!\n")
    conn.close()
