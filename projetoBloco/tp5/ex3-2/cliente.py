import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("certificado.crt")  # Certificado do servidor

original_send = socket.socket.send
original_recv = socket.socket.recv

def monkey_patch():
    def intercepted_send(self, data, *args, **kwargs):
        print(f"Interceptado (envio): {data}")
        return original_send(self, data, *args, **kwargs)

    def intercepted_recv(self, bufsize, *args, **kwargs):
        data = original_recv(self, bufsize, *args, **kwargs)
        print(f"Interceptado (recebido): {data}")
        return data

    socket.socket.send = intercepted_send
    socket.socket.recv = intercepted_recv

monkey_patch()

with socket.create_connection(('servidor-tls', 8443)) as raw_sock:
    with context.wrap_socket(raw_sock, server_hostname='servidor-tls') as cliente_tls:
        print("Cliente: conexão estabelecida")

        mensagem = "Mensagem segura com logging de pacotes"
        cliente_tls.sendall(mensagem.encode())
        resposta = cliente_tls.recv(1024)

        print(f"Cliente: recebido: {resposta.decode()}")

