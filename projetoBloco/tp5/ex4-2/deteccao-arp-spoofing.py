from scapy.all import ARP, sniff
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

historico_arp = {}

def processar_pacote_sniffado(pacote):
    if pacote.haslayer(ARP) and pacote[ARP].op == 2:  # ARP Reply
        ip_real = pacote[ARP].psrc
        mac_resposta = pacote[ARP].hwsrc

        if ip_real in historico_arp:
            mac_anterior = historico_arp[ip_real]
            if mac_anterior != mac_resposta:
                print(f"(alerta): possivel ARP  spoofing detectado para ip {ip_real}!")
                print(f"mac anterior: {mac_anterior}, mac atual: {mac_resposta}")
        else:
            historico_arp[ip_real] = mac_resposta

def iniciar_sniff(interface):
    print(f"iniciando monitoramento ARP na '{interface}'...")
    sniff(iface=interface, store=False, prn=processar_pacote_sniffado)

if __name__ == "__main__":
    print("xxx detecaao de ARP spoofing xxx ")
    interface_rede = input("entre com o nome da interface de rede: ")

    try:
        iniciar_sniff(interface_rede)
    except PermissionError:
        print("(erro): execute sudo.")
    except Exception as erro:
        print(f"(erro) ao executar: {erro}")
