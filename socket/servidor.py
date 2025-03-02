import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)

    print("Servidor iniciado. Aguardando conexões...")

    client_socket, client_address = server_socket.accept()
    print(f"Conexão estabelecida com {client_address}")

    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(f"Mensagem recebida: {message}")
        client_socket.send("Mensagem recebida".encode())

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()
