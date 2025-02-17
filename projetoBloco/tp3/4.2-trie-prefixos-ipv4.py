#Exercício 4.2 – Implementar uma Trie para Prefixos IPv4
#Descrição: Crie uma estrutura Trie para armazenar prefixos IPv4 e implemente a busca pelo “longest prefix match” para um endereço dado.
#Exemplo: Insira os prefixos ["192.168.0.0/16", "192.168.1.0/24", "10.0.0.0/8"] e, para o IP "192.168.1.100", retorne o prefixo mais específico encontrado.

import ipaddress
import time

class NodoTrie:
    def __init__(self):
        self.filhos = {}
        self.prefixo = None

class Trie:
    def __init__(self):
        self.raiz = NodoTrie()

    def inserir_prefixo(self, prefixo):
        """Insere um prefixo IPv4 na Trie.
        Parâmetros:prefixo (str): O prefixo IPv4 a ser inserido na Trie.
        """
        nodo = self.raiz
        rede = ipaddress.IPv4Network(prefixo, strict=False)
        for bit in bin(int(rede.network_address))[2:].zfill(32)[:rede.prefixlen]:
            if bit not in nodo.filhos:
                nodo.filhos[bit] = NodoTrie()
            nodo = nodo.filhos[bit]
        nodo.prefixo = prefixo

    def buscar_prefixo_mais_especifico(self, endereco_ip):
        """Busca o prefixo mais específico para um endereço IPv4 dado.
        Parâmetros:endereco_ip (str): O endereço IPv4 para o qual procurar o prefixo mais específico.
        Retorna:str: O prefixo mais específico encontrado.
        """
        nodo = self.raiz
        rede = ipaddress.IPv4Address(endereco_ip)
        prefixo_mais_long = None
        for bit in bin(int(rede))[2:].zfill(32):
            if bit in nodo.filhos:
                nodo = nodo.filhos[bit]
                if nodo.prefixo:
                    prefixo_mais_long = nodo.prefixo
            else:
                break
        return prefixo_mais_long

if __name__ == "__main__":
    trie = Trie()
    prefixos = ["192.168.0.0/16", "192.168.1.0/24", "10.0.0.0/8"]

    # Medir o tempo de inserção dos prefixos
    inicio_insercao = time.perf_counter()
    for prefixo in prefixos:
        trie.inserir_prefixo(prefixo)
    fim_insercao = time.perf_counter()
    tempo_insercao = fim_insercao - inicio_insercao

    # Medir o tempo de busca do prefixo mais específico
    endereco = "192.168.1.100"
    inicio_busca = time.perf_counter()
    prefixo_mais_especifico = trie.buscar_prefixo_mais_especifico(endereco)
    fim_busca = time.perf_counter()
    tempo_busca = fim_busca - inicio_busca

    print(f"Prefixo específico para o endereço {endereco} = {prefixo_mais_especifico}.")
    print(f"Inserção dos prefixos em {tempo_insercao:.8f} seg")
    print(f"Busca do prefixo mais específico em {tempo_busca:.8f} seg")

