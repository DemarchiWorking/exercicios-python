import time
import matplotlib.pyplot as plt


def torres_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 da torre {origem} para a torre {destino}")
        return
    torres_de_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o disco {n} da torre {origem} para a torre {destino}")
    torres_de_hanoi(n - 1, auxiliar, destino, origem)


def medir_tempo_hanoi(n):
    start_time = time.time()
    torres_de_hanoi(n, 'A', 'C', 'B')
    end_time = time.time()
    tempo_execucao = (end_time - start_time) * 1000  # Convertendo para milissegundos
    return tempo_execucao


def testar_hanoi():
    numeros_de_discos = list(range(1, 31))
    tempos = []

    for n in numeros_de_discos:
        print(f"Resolvendendo as Torres de Hanói para {n} discos:")
        tempo = medir_tempo_hanoi(n)
        tempos.append(tempo)
        print(f"Tempo de execução para {n} discos: {tempo:.6f} ms\n")

    # Plotando e salvando o gráfico
    plt.plot(numeros_de_discos, tempos, marker='o')
    plt.title('Tempo de Execução das Torres de Hanói')
    plt.xlabel('Número de Discos')
    plt.ylabel('Tempo de Execução (ms)')
    plt.grid(True)
    plt.savefig('tempo_execucao_torres_de_hanoi.png')


if __name__ == "__main__":
    testar_hanoi()
