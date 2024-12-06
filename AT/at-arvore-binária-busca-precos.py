class NoArvoreBinaria:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = NoArvoreBinaria(valor)
        else:
            self._inserir(valor, self.raiz)

    def _inserir(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoArvoreBinaria(valor)
            else:
                self._inserir(valor, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = NoArvoreBinaria(valor)
            else:
                self._inserir(valor, no_atual.direita)

    def buscar(self, valor):
        return self._buscar(valor, self.raiz)

    def _buscar(self, valor, no_atual):
        if no_atual is None:
            return False
        if valor == no_atual.valor:
            return True
        elif valor < no_atual.valor:
            return self._buscar(valor, no_atual.esquerda)
        else:
            return self._buscar(valor, no_atual.direita)

arvore = ArvoreBinariaBusca()
precos = [100, 50, 150, 30, 70, 130, 170]

for preco in precos:
    arvore.inserir(preco)

preco_busca = 70
disponivel = arvore.buscar(preco_busca)
if(disponivel):
    print(f"Preço {preco_busca}  disponível:  {disponivel}")
else:
    print(f"Preço {preco_busca} não disponível: {disponivel}")
