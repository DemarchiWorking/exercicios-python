from scapy.all import Ether, IP, sendp, raw #, sniff
import pcapy as pcap
import datetime



def listar_interfaces():
    """Lista todas as interfaces disponíveis para captura."""
    interfaces = pcap.findalldevs()
    print("Interfaces disponíveis:")
    for interface in interfaces:
        print(interface)

def capturar_pacotes(interface):
    """Captura pacotes em tempo real da interface fornecida."""
    print(f"Capturando pacotes na interface {interface}...")
    try:
        cap = pcap.open_live(interface, 65536, 1, 0)
        while True:
            header, payload = cap.next()
            print('%s: capturados %d bytes' % (datetime.datetime.now(), header.getlen()))
    except KeyboardInterrupt:
        print("\nInterrupção pelo usuário. Parando a captura.")
    except Exception as e:
        print(f"Erro ao capturar pacotes: {e}")


def injetar_pacote(interface):
    """Constrói e injeta um pacote Ethernet na interface fornecida."""
    print(f"Injetando pacote na interface {interface}...")
    try:
        # Criando um pacote Ethernet/IP com o Scapy
        pacote = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(dst="192.168.1.1") / "Hello Network"

        # Enviando o pacote pela interface especificada
        sendp(pacote, iface=interface, verbose=False)
        print("Pacote injetado com sucesso!")
    except Exception as e:
        print(f"Erro ao injetar pacote: {e}")

def main():
    print("==== Captura e Injeção de Pacotes com pcapy e scapy ====")
    listar_interfaces()

    interface = input("Digite o nome da interface para usar: ")
    print(f"Você selecionou a interface: {interface}")

    # Escolha da operação
    print("\nEscolha a operação:")
    print("1 - Capturar Pacotes")
    print("2 - Injetar Pacotes")
    opcao = input("Digite 1 ou 2: ")

    if opcao == "1":
        capturar_pacotes(interface)
    elif opcao == "2":
        injetar_pacote(interface)
    else:
        print("Opção inválida. Encerrando o programa.")

#def capturar(interface):
#    print("Capturando pacotes...")
#    pacotes = sniff(iface=interface, count=5)
#    pacotes.show()  # Mostra os pacotes capturados
#    return pacotes

if __name__ == "__main__":
    main()
