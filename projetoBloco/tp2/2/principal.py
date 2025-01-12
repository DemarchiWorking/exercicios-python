import numpy as np
import time
from soma_paralela import soma_paralela


def soma_sequencial(dados):
    return np.sum(dados)


def principal():
    # Criar vetor grande com números aleatórios
    dados = np.random.randint(1, 100000, size=10000).astype(np.float64)

    # Calcular soma sequencial
    tempo_inicio = time.time()
    resultado_sequencial = soma_sequencial(dados)
    tempo_sequencial = time.time() - tempo_inicio
    print(f"Soma Sequencial: {resultado_sequencial}, Tempo: {tempo_sequencial} segundos")

    # Calcular soma paralela
    tempo_inicio = time.time()
    resultado_paralelo = soma_paralela(dados)
    tempo_paralelo = time.time() - tempo_inicio
    print(f"Soma Paralela: {resultado_paralelo}, Tempo: {tempo_paralelo} segundos")


if __name__ == "__main__":
    principal()
