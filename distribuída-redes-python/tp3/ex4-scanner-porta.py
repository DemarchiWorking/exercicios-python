import socket
import argparse

def scanear_porta(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"[+] Porta {port} ABERTA")
        else:
            print(f"[-] Porta {port} FECHADA")

def scanear_portas(host, porta_inicial, porta_final):
    print(f"\n[!] Escaneando {host} de {porta_inicial} até {porta_final}...\n")
    for port in range(porta_inicial, porta_final + 1):
        scanear_porta(host, port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scanner de Portas com Python")
    parser.add_argument("host", help="Endereço IP ou hostname do alvo")
    parser.add_argument("porta_inicial", type=int, help="Porta inicial para escaneamento")
    parser.add_argument("porta_final", type=int, help="Porta final para escaneamento")

    args = parser.parse_args()
    scanear_portas(args.host, args.porta_inicial, args.porta_final)
