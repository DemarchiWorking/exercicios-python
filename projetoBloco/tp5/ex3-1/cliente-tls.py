import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("certificado.crt")


with socket.create_connection(('127.0.0.1', 8443)) as sock:
    with context.wrap_socket(sock, server_hostname='127.0.0.1') as cliente_tls:
        print("Cliente: conexão estabelecida")
        mensagem = "Olá, servidor TLS!"
        cliente_tls.sendall(mensagem.encode())
        resposta = cliente_tls.recv(1024)
        print(f"Cliente: recebido: {resposta.decode()}")
