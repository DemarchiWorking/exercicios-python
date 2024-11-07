class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def hash_func(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self.hash_func(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                item[1] = valor
                return
        self.tabela[indice].append([chave, valor])

    def buscar(self, chave):
        indice = self.hash_func(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        return None

    def remover(self, chave):
        indice = self.hash_func(chave)
        for i, item in enumerate(self.tabela[indice]):
            if item[0] == chave:
                del self.tabela[indice][i]
                return True
        return False

if __name__ == "__main__":
    tabela = TabelaHash(10)
    tabela.inserir("chave1", "valor1")
    tabela.inserir("chave2", "valor2")
    print(tabela.buscar("chave1"))
    print(tabela.buscar("chave2"))
