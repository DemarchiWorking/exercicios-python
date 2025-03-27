import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("certificado.crt")


def monkey_patch_socket(sock):
    original_send = sock.send
    original_recv = sock.recv

    def intercepted_send(data, *args, **kwargs):
        print(f"interceptado (envio): {data}")
        return original_send(data, *args, **kwargs)

    def intercepted_recv(bufsize, *args, **kwargs):
        data = original_recv(bufsize, *args, **kwargs)
        print(f"interceptado (recebido): {data}")
        return data

    sock.send = intercepted_send
    sock.recv = intercepted_recv


with socket.create_connection(('servidor-tls', 8443)) as sock:
    monkey_patch_socket(sock)

    with context.wrap_socket(sock, server_hostname='servidor-tls') as cliente_tls:
        print("cliente: conexão estabelecida")

        mensagem = "mensagem segura com logging de pacotes"
        cliente_tls.sendall(mensagem.encode())
        resposta = cliente_tls.recv(1024)

        print(f"cliente: recebido: {resposta.decode()}")
