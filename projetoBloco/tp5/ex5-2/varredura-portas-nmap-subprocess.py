import nmap
import argparse
import subprocess
import sys
from time import sleep
import os


def processar_resultados_ftp(host, resultado):
    try:
        script = resultado['scan'][host]['tcp'][21]['script']
        print("Comando usado: " + resultado['nmap']['command_line'])
        for chave, valor in script.items():
            print(f"Script {chave} --> {valor}")
    except KeyError:
        pass


class ScannerNmapAssincronoFTP:
    def __init__(self):
        self.portScanner = nmap.PortScanner()
        self.portScannerAsync = nmap.PortScannerAsync()

    def monitorar_escaneamento(self):
        while self.portScannerAsync.still_scanning():
            print("Escaneando >>>")
            self.portScannerAsync.wait(10)

    def escanear_porta_assincrona(self, endereco, porta):
        try:
            print(f"Checando a porta {porta} ..........")
            self.portScanner.scan(endereco, porta)
            self.estado = self.portScanner[endereco]['tcp'][int(porta)]['state']
            print(f" [+] {endereco} tcp/{porta} {self.estado}")

            if porta == '21' and self.portScanner[endereco]['tcp'][int(porta)]['state'] == 'open':
                print('Verificando porta FTP com scripts do nmap......')
                scripts_ftp = [
                    ("ftp-anon.nse", "-A -sV -p21 --script ftp-anon.nse"),
                    ("ftp-bounce.nse", "-A -sV -p21 --script ftp-bounce.nse"),
                    ("ftp-libopie.nse", "-A -sV -p21 --script ftp-libopie.nse"),
                    ("ftp-proftpd-backdoor.nse", "-A -sV -p21 --script ftp-proftpd-backdoor.nse"),
                    ("ftp-vsftpd-backdoor.nse", "-A -sV -p21 --script ftp-vsftpd-backdoor.nse")
                ]
                for nome_script, args in scripts_ftp:
                    print(f"Executando verificação com {nome_script} .....")
                    self.portScannerAsync.scan(endereco, arguments=args, callback=processar_resultados_ftp)
                    self.monitorar_escaneamento()
        except Exception as erro:
            print(f"Erro ao conectar com {endereco} para escaneamento da porta: {str(erro)}")


def executar_comando_nmap(comando):
    try:
        processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        saida, erro = processo.communicate()
        saida = saida.decode('utf-8').strip()
        if erro:
            print(f"Erro: {erro.decode('utf-8').strip()}")
        return saida
    except Exception as e:
        return f"Falha ao executar {comando}: {str(e)}"


def escaneamento_completo_vulnerabilidades(alvo):
    print(f"Iniciando escaneamento detalhado de vulnerabilidades em {alvo}...")


    subprocess.run(["git", "clone", "https://github.com/scipag/vulscan.git", "/usr/share/nmap/scripts/vulscan"])
    subprocess.run(
        ["git", "clone", "https://github.com/vulnersCom/nmap-vulners.git", "/usr/share/nmap/scripts/vulners"])
    subprocess.run(["nmap", "--script-updatedb"])


    comandos_nmap = [
        ["sudo", "nmap", "-sSV", "--script=banner", alvo],
        ["sudo", "nmap", "-T4", "-F", "--host-timeout", "5m", alvo],
        ["sudo", "nmap", "--script", "dns-brute", alvo],
        ["sudo", "nmap", "-sSV", "-p22", "--script", "ssh-hostkey", alvo],
        ["sudo", "nmap", "-sSV", "-p22", "--script", "ssh2-enum-algos", alvo],
        ["sudo", "nmap", "-sSV", "-p21", "--script", "ftp-anon", "ftp.be.debian.org"],
        ["nmap", "-sV", "--script", "vulners", alvo, "-p22,80,3306"],
        ["nmap", "-sV", "--script=vulscan/vulscan.nse", alvo, "-p22,80"]
    ]

    for cmd in comandos_nmap:
        print(f"\nExecutando: {' '.join(cmd)}")
        resultado = executar_comando_nmap(cmd)
        print(resultado)
        sleep(2)

    scripts_adicionais = [
        "ssl-enum-ciphers",
        "http-vuln-cve2017-5638",
        "smb-vuln-ms17-010",
        "http-sql-injection",
        "http-xssed"
    ]

    scanner = ScannerNmapAssincronoFTP()
    scanner.escanear_porta_assincrona(alvo, "21")
    for script in scripts_adicionais:
        print(f"Rodando script {script} com Nmap...")
        scanner.escanear_porta_assincrona(alvo, "80,443")


def parsear_argumentos():
    parser = argparse.ArgumentParser(description="Script para escaneamento de vulnerabilidades com Nmap")
    parser.add_argument("--host", required=True,
                        help="Endereço do host alvo (exemplo: scanme.nmap.org ou 195.234.45.114)")
    return parser.parse_args()


if __name__ == "__main__":
    if os.geteuid() != 0:
        print("use 'sudo'.")
        sys.exit(1)

    args = parsear_argumentos()
    alvo = args.host

    escaneamento_completo_vulnerabilidades(alvo)
