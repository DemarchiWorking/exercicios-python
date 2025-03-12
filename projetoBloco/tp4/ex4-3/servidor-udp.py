import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print(f"Servidor UDP escutando na porta {UDP_PORT}...")

    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Recebido de {addr}: {data.decode()}")
        sock.sendto("ack".encode(), addr)
except Exception as e:
    print(f"Erro no servidor UDP: {e}")
finally:
    sock.close()
