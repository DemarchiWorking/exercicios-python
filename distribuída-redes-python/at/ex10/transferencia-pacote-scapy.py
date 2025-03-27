import logging
from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def registrar_pacote(pacote):
    with open("registro_pacotes.txt", "a") as arquivo_log:
        arquivo_log.write(f"Data e Hora: {datetime.now()}\n")
        arquivo_log.write(f"Resumo do Pacote: {pacote.summary()}\n")
        if pacote.haslayer(IP):
            ip_origem = pacote[IP].src
            ip_destino = pacote[IP].dst
            arquivo_log.write(f"Origem: {ip_origem}, Destino: {ip_destino}\n")
        if pacote.haslayer(TCP):
            porta_origem = pacote[TCP].sport
            porta_destino = pacote[TCP].dport
            arquivo_log.write(f"Protocolo: TCP, Porta Origem: {porta_origem}, Porta Destino: {porta_destino}\n")
        if pacote.haslayer(UDP):
            porta_origem = pacote[UDP].sport
            porta_destino = pacote[UDP].dport
            arquivo_log.write(f"Protocolo: UDP, Porta Origem: {porta_origem}, Porta Destino: {porta_destino}\n")
        arquivo_log.write("-" * 50 + "\n")


def processar_pacote(pacote):
    print(f"Pacote Capturado: {pacote.summary()}")

    if pacote.haslayer(TCP):
        ip_origem = pacote[IP].src
        ip_destino = pacote[IP].dst
        porta_origem = pacote[TCP].sport
        porta_destino = pacote[TCP].dport
        print(f"(TCP)Origem: {ip_origem}:{porta_origem} = Destino: {ip_destino}:{porta_destino}")

    elif pacote.haslayer(UDP):
        ip_origem = pacote[IP].src
        ip_destino = pacote[IP].dst
        porta_origem = pacote[UDP].sport
        porta_destino = pacote[UDP].dport
        print(f"(UDP)Origem: {ip_origem}:{porta_origem} = Destino: {ip_destino}:{porta_destino}")

    elif pacote.haslayer(ICMP):
        ip_origem = pacote[IP].src
        ip_destino = pacote[IP].dst
        print(f"(ICMP)Origem: {ip_origem} = Destino: {ip_destino}")

    registrar_pacote(pacote)


def iniciar_monitoramento(interface, quantidade_pacotes):
    print(f"Ligando a captura de pacotes na interface '{interface}'")
    print(f"Capturando {quantidade_pacotes} pacotes.\n")
    sniff(iface=interface, prn=processar_pacote, store=False, count=quantidade_pacotes)
    print("fim! No arquivo 'registro_pacotes.txt' para detalhes.")


if __name__ == "__main__":
    print("xxx Monitoramento de Transferências na Rede xxx")
    interface = input("Entre com nome da interface de rede:")
    quantidade_pacotes = int(input("Entre o número de pacotes a capturar:"))

    try:
        iniciar_monitoramento(interface, quantidade_pacotes)
    except PermissionError:
        print("Erro: Execute o programa como administrador usando 'sudo'.")
    except Exception as e:
        print(f"Erro ao iniciar o monitoramento: {e}")
