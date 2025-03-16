import os
import socket
import ssl
import threading


HOST = "0.0.0.0"
PORT = 8443

CERT_FILE = "cert.pem"
KEY_FILE = "key.pem"

HTML_PAGE = """\
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notas dos Estudantes</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        table { width: 50%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f4f4f4; }
    </style>
</head>
<body>
    <h1>Notas dos Estudantes</h1>
    <table>
        <tr>
            <th>Nome</th>
            <th>Nota</th>
        </tr>
        <tr><td>Alice</td><td>9.0</td></tr>
        <tr><td>Bruno</td><td>7.5</td></tr>
        <tr><td>Carlos</td><td>8.2</td></tr>
    </table>
</body>
</html>
"""

def handle_client(connection):
    try:
        request = connection.recv(1024).decode()
        print(f"\n[+] Requisição recebida:\n{request}")


        connection.sendall(HTML_PAGE.encode())

    except Exception as e:
        print(f"[!] Erro ao processar requisição: {e}")

    finally:
        connection.close()

def iniciar_servidor():
    # Criando um socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    secure_socket = ssl.wrap_socket(server_socket, keyfile=KEY_FILE, certfile=CERT_FILE, server_side=True)

    secure_socket.bind((HOST, PORT))
    secure_socket.listen(5)
    print(f"[+] Servidor HTTPS rodando em https://localhost:{PORT}")

    while True:
        client_connection, client_address = secure_socket.accept()
        print(f"[+] Conexão recebida de {client_address}")


        threading.Thread(target=handle_client, args=(client_connection,), daemon=True).start()

if __name__ == "__main__":
    if not os.path.exists(CERT_FILE) or not os.path.exists(KEY_FILE):
        print("[!] Certificado SSL não encontrado! Gere um antes de executar.")
    else:
        iniciar_servidor()
