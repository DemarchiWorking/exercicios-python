import concurrent.futures
import time

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def busca_sequencial(no, valor_procurado):
    """Busca sequencial de um valor na árvore."""
    if no is None:
        return False
    if no.valor == valor_procurado:
        return True
    return busca_sequencial(no.esquerda, valor_procurado) or busca_sequencial(no.direita, valor_procurado)

def busca_paralela(no, valor_procurado):
    """Busca paralela de um valor na árvore."""
    if no is None:
        return False
    if no.valor == valor_procurado:
        return True

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futuros = []
        if no.esquerda is not None:
            futuros.append(executor.submit(busca_paralela, no.esquerda, valor_procurado))
        if no.direita is not None:
            futuros.append(executor.submit(busca_paralela, no.direita, valor_procurado))

        for futuro in concurrent.futures.as_completed(futuros):
            if futuro.result():
                return True

    return False

if __name__ == "__main__":
    raiz = No(50)
    raiz.esquerda = No(30)
    raiz.direita = No(70)
    raiz.esquerda.esquerda = No(20)
    raiz.esquerda.direita = No(40)
    raiz.direita.esquerda = No(60)
    raiz.direita.direita = No(80)

    valor_procurado = 60

    inicio_tempo_seq = time.perf_counter()
    encontrado_seq = busca_sequencial(raiz, valor_procurado)
    fim_tempo_seq = time.perf_counter()
    tempo_execucao_seq = fim_tempo_seq - inicio_tempo_seq

    if encontrado_seq:
        print(f"B Sequencial: Valor {valor_procurado} encontrado na arvore.")
    else:
        print(f"B Sequencial: Valor {valor_procurado} não encontrado na arvore.")
    print(f"Tempo de execução (sequencial): {tempo_execucao_seq:.8f} segundos")

    inicio_tempo_par = time.perf_counter()
    encontrado_par = busca_paralela(raiz, valor_procurado)
    fim_tempo_par = time.perf_counter()
    tempo_execucao_par = fim_tempo_par - inicio_tempo_par

    if encontrado_par:
        print(f"Busca Paralela: Valor {valor_procurado} encontrado na arvore.")
    else:
        print(f"Busca Paralela: Valor {valor_procurado} não encontrado na arvore.")
    print(f"Tempo de execução (paralela): {tempo_execucao_par:.8f} segundos")
