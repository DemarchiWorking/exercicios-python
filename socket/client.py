import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    message = input("Digite a mensagem para enviar ao servidor: ")
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"Resposta do servidor: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
