import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
sizes = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304]
sequential = [0.069, 0.145, 0.342, 0.673, 1.562, 4.098, 8.025, 18.332, 37.877, 78.305, 154.342, 318.140, 706.720]
parallel = [0.069, 0.147, 0.324, 1.112, 1.434, 3.561, 8.530, 16.527, 35.547, 74.070, 155.384, 339.182, 704.807]
speedups = [1.00, 0.99, 1.06, 0.60, 1.09, 1.15, 0.94, 1.11, 1.07, 1.06, 0.99, 0.94, 1.00]

# Criando a figura com 2 subplots
plt.figure(figsize=(14, 6))

# Gráfico 1: Tempos de execução
plt.subplot(1, 2, 1)
plt.plot(sizes, sequential, 'bo-', label='Sequencial', markersize=6)
plt.plot(sizes, parallel, 'go-', label='Paralelo', markersize=6)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Tamanho do Array (elementos)', fontsize=12)
plt.ylabel('Tempo de Execução (ms)', fontsize=12)
plt.title('Tempo de Ordenação: Sequencial vs Paralelo', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, which="both", ls="--", alpha=0.5)

# Adicionando valores nos pontos de dados
for i, size in enumerate(sizes):
    if i % 3 == 0:  # Mostrar apenas alguns para não poluir
        plt.annotate(f'{sequential[i]:.2f}ms', (size, sequential[i]),
                    textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)
        plt.annotate(f'{parallel[i]:.2f}ms', (size, parallel[i]),
                    textcoords="offset points", xytext=(0,-15), ha='center', fontsize=8)

# Gráfico 2: Speedup
plt.subplot(1, 2, 2)
bars = plt.bar(range(len(sizes)), speedups, color=['r' if x < 1 else 'g' for x in speedups])
plt.axhline(y=1, color='k', linestyle='--')
plt.xticks(range(len(sizes)), [f'{size//1024}K' if size < 1000000 else f'{size//1048576}M'
                              for size in sizes], rotation=45)
plt.xlabel('Tamanho do Array', fontsize=12)
plt.ylabel('Speedup (T_seq/T_par)', fontsize=12)
plt.title('Ganho de Performance (Speedup)', fontsize=14)

# Adicionando valores nas barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}x',
             ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('comparacao_ordenacao.png', dpi=300, bbox_inches='tight')
plt.show()