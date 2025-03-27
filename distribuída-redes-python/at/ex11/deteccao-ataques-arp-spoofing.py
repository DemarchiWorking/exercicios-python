from scapy.all import ARP, Ether, sniff, srp
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def obter_endereco_mac(endereco_ip):
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    requisicao_arp = ARP(pdst=endereco_ip)
    pacote_broadcast = broadcast / requisicao_arp
    resposta, _ = srp(pacote_broadcast, timeout=1, verbose=False)

    if resposta:
        return resposta[0][1].hwsrc
    else:
        return None

def processar_pacote_sniffado(pacote):
    if pacote.haslayer(ARP) and pacote[ARP].op == 2:
        ip_real = pacote[ARP].psrc
        mac_resposta = pacote[ARP].hwsrc

        mac_legitimo = obter_endereco_mac(ip_real)

        if mac_legitimo and mac_legitimo != mac_resposta:
            print(f"(WARNING) Detecção de ARP Spoofing!")
            print(f"|IP|: {ip_real} | MAC Legitmo= {mac_legitimo} | MAC suspeito: {mac_resposta}")

def iniciar_sniff(interface):
    print(f"Começando a monitor ARP na interface '{interface}'...")
    sniff(iface=interface, store=False, prn=processar_pacote_sniffado)

if __name__ == "__main__":
    print("xxx Detecta ARP Spoofing xxx")
    interface_rede = input("Entre com o nome da interface de rede: ")

    try:
        iniciar_sniff(interface_rede)
    except PermissionError:
        print("ERRO: Execute com permissao de sudo.")
    except Exception as erro:
        print(f"ERRO: A executar o programa: {erro}")
