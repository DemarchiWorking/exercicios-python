import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="certificado.crt", keyfile="chave_privada.key")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind(('127.0.0.1', 8443))
    sock.listen(5)
    print("Servidor TLS esperando conexões...")

    with context.wrap_socket(sock, server_side=True) as servidor_tls:
        conn, addr = servidor_tls.accept()
        print(f"Conexão estabelecida com {addr}")
        while True:
            dados = conn.recv(1024)
            if not dados:
                break
            print(f"Recebido: {dados.decode()}")
            conn.sendall(dados)
        conn.close()
