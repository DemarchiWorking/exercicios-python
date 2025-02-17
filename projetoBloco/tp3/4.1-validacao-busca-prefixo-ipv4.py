#Grupo 4 – Busca Otimizada de Prefixos IPv4/IPv6
#Exercício 4.1 – Validação e Busca de Prefixo em IPv4
#Descrição: Utilize o módulo ipaddress para validar se um dado endereço IPv4 está contido em um prefixo (por exemplo, "192.168.1.0/24").
#Exemplo: Verifique se o IP "192.168.1.5" está dentro do prefixo "192.168.1.0/24".

import ipaddress
import time


def validar_ipv4(endereco_ip, prefixo_ip):
    """Verifica se um endereço IPv4 está contido em um prefixo.
    Parâmetros:endereco_ip (str): O endereço IPv4 a ser verificado.
    prefixo_ip (str): O prefixo IPv4 na forma "192.168.1.0/24".
    Retorna:bool: True se o endereço estiver contido no prefixo, False caso contrário.
    """
    try:
        # Cria objetos de endereço e rede IPv4
        ip = ipaddress.IPv4Address(endereco_ip)
        rede = ipaddress.IPv4Network(prefixo_ip, strict=False)

        # Verifica se o endereço IP está contido na rede
        return ip in rede
    except ValueError as e:
        print(f"Erro: {e}")
        return False


if __name__ == "__main__":
    endereco = "192.168.1.5"
    prefixo = "192.168.1.0/24"

    # Medição de tempo de execução performática e precisa
    inicio_tempo = time.perf_counter()
    resultado = validar_ipv4(endereco, prefixo)
    fim_tempo = time.perf_counter()
    tempo_execucao = fim_tempo - inicio_tempo

    if resultado:
        print(f"O IP {endereco} está contido no prefixo {prefixo}.")
    else:
        print(f"O IP {endereco} NÃO está contido no prefixo {prefixo}.")

    print(f"Tempo de execução: {tempo_execucao:.8f} segundos")
