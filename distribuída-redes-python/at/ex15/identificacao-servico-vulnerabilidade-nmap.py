import nmap
import asyncio
import argparse
import csv
import socket
import time

class NmapEnhancedScanner:
    def __init__(self):
        self.portScanner = nmap.PortScanner()
        self.portScannerAsync = nmap.PortScannerAsync()


    def varredura_sincrona(self, host, portas):
        inicio = time.time()
        print(f"xxx Realizando varredura síncrona em {host}")
        self.portScanner.scan(hosts=host, arguments=f'-n -p{portas}')
        print("Comando executado:", self.portScanner.command_line())
        print("[RESULTADOS] Hosts Escaneados:")
        for host in self.portScanner.all_hosts():
            print(f"Host: {host} > Status: {self.portScanner[host]['status']['state']}")
            for protocolo in self.portScanner[host].all_protocols():
                print(f"Protocolo: {protocolo}")
                for porta in self.portScanner[host][protocolo].keys():
                    estado = self.portScanner[host][protocolo][porta]['state']
                    print(f"Porta: {porta} - Estado: {estado}")
        fim = time.time()
        print(f"xxx Tempo de execução (sync): {(fim - inicio) * 1000:.2f} ms")

    async def varredura_assincrona(self, host, portas):
        inicio = time.time()  # Registrar o tempo de início

        def callback_result(host, scan_result):
            print(f"[ASSync] Host =  {host} > Resultado:")
            for protocol in scan_result['scan'][host].keys():
                if protocol in ('tcp', 'udp'):
                    for port, data in scan_result['scan'][host][protocol].items():
                        print(f"Porta {port} <> Estado: {data['state']}")

        print(f"xxx Realizando varredura assíncrona em {host}...")
        self.portScannerAsync.scan(hosts=host, arguments=f'-p{portas}', callback=callback_result)
        while self.portScannerAsync.still_scanning():
            print("xxx Escaneamento em andamento...")
            self.portScannerAsync.wait(2)

        fim = time.time()
        print(f"xxx Tempo de execução (async): {(fim - inicio) * 1000:.2f} ms")

    def varredura_intervalo(self, host, porta_inicial, porta_final):
        inicio = time.time()
        portas = f"{porta_inicial} = {porta_final}"
        print(f"xxx Realizando varredura no intervalo de portas {portas} em {host}")
        self.portScanner.scan(hosts=host, arguments=f'-p{portas}')
        print("xxx Comando executado:", self.portScanner.command_line())
        print("(RESULTADOS) Hosts Escaneados:")
        for host in self.portScanner.all_hosts():
            print(f"Host: {host} > Status= {self.portScanner[host]['status']['state']}")
            for protocolo in self.portScanner[host].all_protocols():
                print(f"Protocolo: {protocolo}")
                for porta in self.portScanner[host][protocolo].keys():
                    estado = self.portScanner[host][protocolo][porta]['state']
                    print(f"Porta = {porta} : Estado= {estado}")
        fim = time.time()
        print(f"xxx Tempo de execução (portall): {(fim - inicio) * 1000:.2f} ms")

    def exportar_resultados_csv(self, host, portas):
        print("xxx Exportando resultados para CSV...")
        self.portScanner.scan(hosts=host, arguments=f'-n -p{portas}')
        with open('resultados_scan.csv', mode='w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(['Host', 'Protocolo', 'Porta', 'Estado'])
            for host in self.portScanner.all_hosts():
                for protocolo in self.portScanner[host].all_protocols():
                    for porta in self.portScanner[host][protocolo].keys():
                        estado = self.portScanner[host][protocolo][porta]['state']
                        csv_writer.writerow([host, protocolo, porta, estado])
        print("xxx Exportação concluída. Verifique o arquivo 'resultados_scan.csv'.")

def main():
    parser = argparse.ArgumentParser(description="Scanner Nmap - Combinado e Completo")
    parser.add_argument("--host", type=str, required=True, help="Especifique o host alvo")
    parser.add_argument("--ports", type=str, help="Especifique as portas para escanear (ex: 22,80,443)")
    parser.add_argument("--portall", type=str, help="Especifique o intervalo de portas no formato X-Y (ex: 20-80)")
    parser.add_argument("--mode", type=str, choices=["sync", "async", "csv"], required=True, help="Escolha o modo: sync, async ou csv")
    args = parser.parse_args()

    scanner = NmapEnhancedScanner()

    if args.mode == "sync" and args.portall:
        try:
            porta_inicial, porta_final = map(int, args.portall.split('-'))
            scanner.varredura_intervalo(args.host, porta_inicial, porta_final)
        except ValueError:
            print("(ERR)--portall é (ex: 22-80)")
    elif args.mode == "sync":
        if args.ports:
            scanner.varredura_sincrona(args.host, args.ports)
        else:
            print("(ERR) --ports ou --portall.")
    elif args.mode == "async" and args.ports:
        asyncio.run(scanner.varredura_assincrona(args.host, args.ports))
    elif args.mode == "csv" and args.ports:
        scanner.exportar_resultados_csv(args.host, args.ports)
    else:
        print("(ERR) Argumentos incorretos.")

if __name__ == "__main__":
    main()
