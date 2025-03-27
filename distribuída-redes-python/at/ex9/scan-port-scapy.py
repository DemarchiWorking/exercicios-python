import logging
from scapy.all import IP, TCP, sr1, ICMP

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def scan_port(host, port):
    print(f"xxx Escaneando a porta {port}")
    packet = IP(dst=host)/TCP(dport=port, flags="S")
    response = sr1(packet, timeout=0.5, verbose=0)

    if response is not None:
        if response.haslayer(TCP) and response[TCP].flags == 18:
            print(f"A porta {port} tá aberta!")
        elif response.haslayer(TCP) and response[TCP].flags == 0x14:
            print(f"A porta {port} tá fechada.")
        elif response.haslayer(ICMP):
            icmp_type = int(response[ICMP].type)
            icmp_code = int(response[ICMP].code)
            if icmp_type == 3 and icmp_code in [1, 2, 3, 9, 10, 13]:
                print(f"Porta {port} tá filtrada.")
    else:
        print(f"Porta {port} não respondeu.")

def main(alvo, porta_inicial, porta_final):
    print(f"Começando a escanear o alvo {alvo}")
    for port in range(porta_inicial, porta_final + 1):
        scan_port(alvo, port)

if __name__ == "__main__":
    alvo = input("Informe o ip ou hostname do alvo desejado: ")
    porta_inicial = int(input("Entre com a porta inicial: "))
    porta_final = int(input("Entre com a porta final: "))
    main(alvo, porta_inicial, porta_final)
