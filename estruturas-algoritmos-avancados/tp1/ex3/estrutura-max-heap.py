#Exercício 3: Implementação da estrutura de dados MaxHeap
#Enunciado: Considere a seguinte MaxHeap armazenada em um array:
#[50, 30, 40, 10, 20, 35] #Após a inserção do elemento 45, qual será a nova estrutura do Heap? Justifique sua resposta.

class MaxHeap:
    def __init__(self):
        self.elementos = []

    def indice_pai(self, posicao):
        return (posicao - 1) // 2

    def indice_filho_esquerdo(self, posicao):
        return 2 * posicao + 1

    def indice_filho_direito(self, posicao):
        return 2 * posicao + 2

    def adicionar(self, valor):
        self.elementos.append(valor)
        self._ajustar_para_cima(len(self.elementos) - 1)

    def remover_maior(self):
        if len(self.elementos) == 0:
            raise IndexError("Não é possível remover o maior elemento, a heap está vazia.")

        if len(self.elementos) == 1:
            return self.elementos.pop()

        raiz = self.elementos[0]
        self.elementos[0] = self.elementos.pop()
        self._ajustar_para_baixo(0)
        return raiz

    def obter_maior(self):
        if len(self.elementos) == 0:
            raise IndexError("Não é possível obter o maior elemento, a heap está vazia.")

        return self.elementos[0]

    def _ajustar_para_cima(self, posicao):
        while posicao > 0 and self.elementos[posicao] > self.elementos[self.indice_pai(posicao)]:
            self.elementos[posicao], self.elementos[self.indice_pai(posicao)] = self.elementos[
                self.indice_pai(posicao)], self.elementos[posicao]
            posicao = self.indice_pai(posicao)

    def _ajustar_para_baixo(self, posicao):
        maior = posicao
        esquerdo = self.indice_filho_esquerdo(posicao)
        direito = self.indice_filho_direito(posicao)

        if esquerdo < len(self.elementos) and self.elementos[esquerdo] > self.elementos[maior]:
            maior = esquerdo

        if direito < len(self.elementos) and self.elementos[direito] > self.elementos[maior]:
            maior = direito

        if maior != posicao:
            self.elementos[posicao], self.elementos[maior] = self.elementos[maior], self.elementos[posicao]
            self._ajustar_para_baixo(maior)

    def tamanho(self):
        return len(self.elementos)


# Exemplo de uso
heap_maxima = MaxHeap()
heap_maxima.adicionar(50)
heap_maxima.adicionar(30)
heap_maxima.adicionar(40)
heap_maxima.adicionar(10)
heap_maxima.adicionar(20)
heap_maxima.adicionar(35)

print("Antes:", heap_maxima.elementos)

heap_maxima.adicionar(45)
print("Atual:", heap_maxima.elementos)
print("Maior removido:", heap_maxima.remover_maior())


