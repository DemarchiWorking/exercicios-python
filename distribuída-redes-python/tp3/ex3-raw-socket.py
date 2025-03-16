import socket
import struct

# Criar um raw socket
raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

# Escutar pacotes
print("Capturando pacotes ICMP...")
while True:
    # Receber um pacote
    pacote, endereco = raw_socket.recvfrom(65535)

    # Exibir informações básicas
    print(f"\nPacote recebido de: {endereco}")

    # Decodificar cabeçalho ICMP (20 bytes de cabeçalho IP + dados ICMP)
    cabecalho_ip = pacote[:20]  # Cabeçalho IP
    cabecalho_icmp = pacote[20:28]  # Cabeçalho ICMP

    # Desempacotar o cabeçalho ICMP (Tipo, Código, Checksum, ID, Seq)
    tipo, codigo, checksum, id, seq = struct.unpack("!BBHHH", cabecalho_icmp)

    print("=== Detalhes do Pacote ICMP ===")
    print(f"Tipo: {tipo}")
    print(f"Código: {codigo}")
    print(f"Checksum: {checksum}")
    print(f"ID: {id}")
    print(f"Sequência: {seq}")
