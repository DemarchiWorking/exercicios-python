class Pilha:
    def __init__(self):
        self.items = []
    def esta_vazia(self):
        return len(self.items) == 0
    def empilhar(self, item):
        self.items.append(item)
    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()
        return None
    def topo(self):
        if not self.esta_vazia():
            return self.items[-1]
        return None
    def tamanho(self):
        return len(self.items)

class Navegador:
    def __init__(self):
        self.historico = Pilha()
        self.avancar = Pilha()
        self.pagina_atual = None
    def visitar_pagina(self, url):
        if self.pagina_atual:
            self.historico.empilhar(self.pagina_atual)
        self.pagina_atual = url
        self.avancar = Pilha()  # Limpar a pilha de avançar
        print(f"Abrindo: {self.pagina_atual}")
    def botao_voltar(self):
        if self.historico.esta_vazia():
            print("Nao tem paginas.")
            return
        self.avancar.empilhar(self.pagina_atual)
        self.pagina_atual = self.historico.desempilhar()
        print(f"Voltando : {self.pagina_atual}")
    def botao_avancar(self):
        if self.avancar.esta_vazia():
            print("Não tem paginas.")
            return
        self.historico.empilhar(self.pagina_atual)
        self.pagina_atual = self.avancar.desempilhar()
        print(f"Avançando para: {self.pagina_atual}")
if __name__ == "__main__":
    navegador = Navegador()
    navegador.visitar_pagina("https://google.com/1")
    navegador.visitar_pagina("https://youtube.com/2")
    navegador.visitar_pagina("https://netflix.com/3")
    navegador.botao_voltar()
    navegador.botao_voltar()
    navegador.botao_avancar()
