import matplotlib.pyplot as plt
import numpy as np

sizes = np.array([100, 1000, 5000, 10000, 50000, 100000])
creation = np.array([0.0037, 0.0300, 0.1846, 0.4053, 1.6516, 3.6455])
insertion = np.array([0.0076, 0.0662, 0.3892, 0.7568, 4.2645, 7.8324])
search = np.array([0.00065, 0.0041, 0.0144, 0.0441, 0.3097, 0.5604])
removal = np.array([0.00054, 0.00057, 0.00097, 0.0011, 0.0013, 0.0018])

# Criar 4 subplots (1 por operação)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Heap Binária: Análise Individual por Operação', fontsize=16)

# Gráfico 1: Criação
axes[0, 0].plot(sizes, creation, marker='o', color='blue')
axes[0, 0].set_title('Criação (O(n))')
axes[0, 0].set_xscale('log')
axes[0, 0].set_xticks(sizes)
axes[0, 0].set_xticklabels(['100', '1k', '5k', '10k', '50k', '100k'])
axes[0, 0].grid(True, linestyle='--')

# Gráfico 2: Inserção
axes[0, 1].plot(sizes, insertion, marker='s', color='red')
axes[0, 1].set_title('Inserção (O(n log n))')
axes[0, 1].set_xscale('log')
axes[0, 1].set_xticks(sizes)
axes[0, 1].set_xticklabels(['100', '1k', '5k', '10k', '50k', '100k'])
axes[0, 1].grid(True, linestyle='--')

# Gráfico 3: Busca
axes[1, 0].plot(sizes, search, marker='^', color='green')
axes[1, 0].set_title('Busca (O(1))')
axes[1, 0].set_xscale('log')
axes[1, 0].set_xticks(sizes)
axes[1, 0].set_xticklabels(['100', '1k', '5k', '10k', '50k', '100k'])
axes[1, 0].grid(True, linestyle='--')

# Gráfico 4: Remoção
axes[1, 1].plot(sizes, removal, marker='d', color='purple')
axes[1, 1].set_title('Remoção (O(log n))')
axes[1, 1].set_xscale('log')
axes[1, 1].set_xticks(sizes)
axes[1, 1].set_xticklabels(['100', '1k', '5k', '10k', '50k', '100k'])
axes[1, 1].grid(True, linestyle='--')

# Ajustar labels comuns
for ax in axes.flat:
    ax.set(xlabel='Tamanho da Entrada', ylabel='Tempo (ms)')

plt.tight_layout()
plt.show()