from scapy.all import ARP, Ether, srp, sniff
import ipaddress
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def varrer_rede(intervalo_ip):
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    requisicao_arp = ARP(pdst=str(intervalo_ip))
    pacote_broadcast = broadcast / requisicao_arp
    resposta, _ = srp(pacote_broadcast, timeout=1, verbose=False)

    print("hosts ativos:")
    for _, recebido in resposta:
        print(f"ip: {recebido.psrc}, mac: {recebido.hwsrc}")

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
    if pacote.haslayer(ARP) and pacote[ARP].op == 2:  # ARP Reply
        ip_real = pacote[ARP].psrc
        mac_resposta = pacote[ARP].hwsrc

        mac_legitimo = obter_endereco_mac(ip_real)

        if mac_legitimo and mac_legitimo != mac_resposta:
            print(f"(WARNING) detecaao de ARP spoofing!")
            print(f"| ip: {ip_real} | mac legitimo: {mac_legitimo} | mac suspeito: {mac_resposta}")

def iniciar_sniff(interface):
    print(f"iniciando monitoramento ARP me '{interface}'...")
    sniff(iface=interface, store=False, prn=processar_pacote_sniffado)

if __name__ == "__main__":
    print("xxx Varredura de Rede ARP e Detecção de ARP Spoofing xxx")
    print("1. varredura ARP")
    print("2. monitoramento ARP Spoofing")
    escolha = input("Escolha (1 ou 2): ")

    try:
        if escolha == "1":
            intervalo = input("entre com o intervalo de ip: ")
            varrer_rede(ipaddress.ip_network(intervalo, strict=False))
        elif escolha == "2":
            interface_rede = input("entre com o nome da interface de rede: ")
            iniciar_sniff(interface_rede)
        else:
            print("opcao invalida (1,2).")
    except PermissionError:
        print("(erro): use sudo")
    except Exception as erro:
        print(f"(erro) ao executar: {erro}")
