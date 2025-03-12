import socket

UDP_IP = "servidor"
UDP_PORT = 5005
MESSAGE = "Ola, servidor UDP!"

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"Enviando mensagem para {UDP_IP}:{UDP_PORT}")
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

    data, addr = sock.recvfrom(1024)
    print(f"Resposta do servidor: {data.decode()}")
except Exception as e:
    print(f"Erro no cliente UDP: {e}")
finally:
    sock.close()
