import matplotlib.pyplot as plt
import numpy as np

# Dados convertidos para segundos
tamanhos = np.array([7, 14, 28, 56, 112, 224, 448, 896])
tempos = {
    'Inserção': np.array([0.0058, 0.0084, 0.0153, 0.0373, 0.0815, 0.1713, 0.3885, 0.9220]) / 1000,
    'Em Ordem': np.array([0.0020, 0.0027, 0.0042, 0.0079, 0.0160, 0.0295, 0.0591, 0.1318]) / 1000,
    'Pré-Ordem': np.array([0.0017, 0.0023, 0.0040, 0.0076, 0.0151, 0.0290, 0.0573, 0.1850]) / 1000,
    'Pós-Ordem': np.array([0.0016, 0.0023, 0.0040, 0.0076, 0.0154, 0.0297, 0.0581, 0.1282]) / 1000
}

# Configuração do estilo
plt.style.use('seaborn-v0_8')
cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# 1. Gráfico Comparativo Geral
plt.figure(figsize=(14, 7))
for i, (op, tempo) in enumerate(tempos.items()):
    plt.plot(tamanhos, tempo, 'o-', color=cores[i], linewidth=2, markersize=8, label=op)

plt.title('Tempo de Execução por Operação vs Número de Elementos', fontsize=14, pad=20)
plt.xlabel('Número de Elementos na Árvore', fontsize=12)
plt.ylabel('Tempo de Execução (segundos)', fontsize=12)
plt.xticks(tamanhos, fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()

# Anotações de desempenho
plt.annotate('Melhor desempenho\npara poucos elementos',
             xy=(14, 0.001), xytext=(50, 0.0005),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10)

plt.annotate('Pré-Ordem menos eficiente\nem grandes volumes',
             xy=(896, 0.1850 / 1000), xytext=(600, 0.00015),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10)
plt.show()

# 2. Gráficos Individuais
fig, axs = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Tempo de Execução por Tipo de Operação', fontsize=16, y=1.02)

for ax, (op, tempo), cor in zip(axs.flat, tempos.items(), cores):
    bars = ax.bar(tamanhos.astype(str), tempo, color=cor)
    ax.set_title(op, fontsize=13)
    ax.set_xlabel('Número de Elementos', fontsize=11)
    ax.set_ylabel('Tempo (segundos)', fontsize=11)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    # Adicionar valores nas barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                f'{height:.6f}',
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()

# 3. Gráfico de Proporções
plt.figure(figsize=(12, 7))
tempo_total = sum(tempos.values())  # Soma todos os tempos para cada tamanho

for op, tempo in tempos.items():
    proporcao = tempo / tempo_total * 100
    plt.plot(tamanhos, proporcao, 'o-', label=op)

plt.title('Proporção do Tempo por Operação', fontsize=14)
plt.xlabel('Número de Elementos', fontsize=12)
plt.ylabel('Porcentagem do Tempo Total (%)', fontsize=12)
plt.xticks(tamanhos)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()