import ssl
import socket

def verificar_certificado_https(hostname, porta=443):
    try:
        contexto_ssl = ssl.create_default_context()
        contexto_ssl.check_hostname = False
        contexto_ssl.verify_mode = ssl.CERT_NONE

        with socket.create_connection((hostname, porta)) as sock:
            with contexto_ssl.wrap_socket(sock, server_hostname=hostname) as conexao_ssl:
                certificado = conexao_ssl.getpeercert()
                print(f"Certificado recebido do servidor {hostname}:")


                for chave, valor in certificado.items():
                    print(f"{chave}: {valor}")

                print("\nA conexão foi bem-sucedida, mas a validação foi ignorada (aceitando certificados autossinados).")

    except ssl.SSLCertVerificationError as erro:
        print(f"Erro ao verificar certificado SSL: {erro}")
    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")

if __name__ == "__main__":
    servidor = "meu-servidor.local"
    verificar_certificado_https(servidor)
