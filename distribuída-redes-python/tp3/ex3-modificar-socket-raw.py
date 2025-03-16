import socket
import struct

raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

def calcular_checksum(dados):
    soma = 0
    for i in range(0, len(dados), 2):
        parte = (dados[i] << 8) + (dados[i+1] if i+1 < len(dados) else 0)
        soma += parte
        soma = (soma >> 16) + (soma & 0xFFFF)
        soma += (soma >> 16)
        return ~soma & 0xFFFF
        print("Capturando pacotes ICMP...")

        while True:
            pacote, endereco = raw_socket.recvfrom(65535)
            cabecalho_ip = pacote[:20]
            cabecalho_icmp = pacote[20:28]
            payload = pacote[28:]
            tipo, codigo, checksum, id, seq = struct.unpack("!BBHHH", cabecalho_icmp)
            print("\n === Pacote Recebido ===")
            print(f"Tipo: {tipo}, Código: {codigo}, Checksum: {checksum}, ID: {id}, Sequência: {seq}")
            novo_tipo = 0
            novo_codigo = 0
            novo_checksum = 0
            novo_cabecalho_icmp = struct.pack("!BBHHH", novo_tipo, novo_codigo, novo_checksum, id, seq)
            novo_checksum = calcular_checksum(novo_cabecalho_icmp + payload)
            novo_cabecalho_icmp = struct.pack("!BBHHH", novo_tipo, novo_codigo, novo_checksum, id, seq)
            pacote_modificado = cabecalho_ip + novo_cabecalho_icmp + payload
            raw_socket.sendto(pacote_modificado, endereco)
            print(f"Pacote modificado enviado para: {endereco}")