#Exercício 4.3 – Implementar Busca de Prefixos para IPv6 utilizando Trie
#Descrição: Adapte a estrutura Trie para trabalhar com endereços IPv6, convertendo-os em uma string binária de 128 bits, e implemente a busca pelo prefixo mais longo.
#Exemplo: Insira os prefixos ["2001:db8::/32", "2001:db8:1234::/48"] e, para o IP "2001:db8:1234:5678::1", retorne o prefixo correspondente.

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
        """Insere um prefixo IPv6 na Trie.
        Parâmetros: prefixo (str): O prefixo IPv6 a ser inserido na Trie"""
        nodo = self.raiz
        rede = ipaddress.IPv6Network(prefixo, strict=False)
        for bit in bin(int(rede.network_address))[2:].zfill(128)[:rede.prefixlen]:
            if bit not in nodo.filhos:
                nodo.filhos[bit] = NodoTrie()
            nodo = nodo.filhos[bit]
        nodo.prefixo = prefixo

    def buscar_prefixo_mais_especifico(self, endereco_ip):
        """Busca o prefixo mais específico para um endereço IPv6 dado.
        Parâmetros:endereco_ip (str): O endereço IPv6 para o qual procurar o prefixo mais específico.
        Retorna:str: O prefixo mais específico encontrado."""
        nodo = self.raiz
        ip = ipaddress.IPv6Address(endereco_ip)
        prefixo_mais_long = None
        for bit in bin(int(ip))[2:].zfill(128):
            if bit in nodo.filhos:
                nodo = nodo.filhos[bit]
                if nodo.prefixo:
                    prefixo_mais_long = nodo.prefixo
            else:
                break
        return prefixo_mais_long

if __name__ == "__main__":
    trie = Trie()
    prefixos = ["2001:db8::/32", "2001:db8:1234::/48"]

    # Medir o tempo de inserção dos prefixos
    inicio_insercao = time.perf_counter()
    for prefixo in prefixos:
        trie.inserir_prefixo(prefixo)
    fim_insercao = time.perf_counter()
    tempo_insercao = fim_insercao - inicio_insercao

    # Medir o tempo de busca do prefixo mais específico
    endereco = "2001:db8:1234:5678::1"
    inicio_busca = time.perf_counter()
    prefixo_mais_especifico = trie.buscar_prefixo_mais_especifico(endereco)
    fim_busca = time.perf_counter()
    tempo_busca = fim_busca - inicio_busca

    print(f"Prefixo mais específico para o endereco {endereco} = {prefixo_mais_especifico}.")
    print(f"Inserção dos prefixos em {tempo_insercao:.8f} seg")
    print(f"Busca do prefixo mais específico: {tempo_busca:.8f} seg")
