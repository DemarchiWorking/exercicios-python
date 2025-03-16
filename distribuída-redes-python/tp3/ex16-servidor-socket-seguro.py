import socket
import ssl

HOST = 'localhost'
PORT = 8443

# Criar um socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Criar um contexto SSL que usa o certificado do servidor
context = ssl.create_default_context()
context.load_verify_locations("certificado.pem")  # Adiciona o certificado como confiável

secure_socket = context.wrap_socket(client_socket, server_hostname=HOST)

# Conectar ao servidor HTTPS
secure_socket.connect((HOST, PORT))
print(f"Conectado ao servidor HTTPS em {HOST}:{PORT}")

# Enviar requisição HTTP GET
request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
secure_socket.sendall(request.encode())

# Receber resposta do servidor
response = secure_socket.recv(4096).decode()
print(f"Resposta do servidor:\n{response}")

secure_socket.close()
