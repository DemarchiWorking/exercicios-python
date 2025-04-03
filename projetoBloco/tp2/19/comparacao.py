import matplotlib.pyplot as plt
import numpy as np

# Dados (convertidos para ms e unidades simplificadas)
tamanhos = ['0.5k', '5k', '50k', '500k', '1M', '5M']
tempo_seq_ms = [0.011, 0.021, 0.126, 1.161, 29.1, 141.3]
tempo_par_ms = [1.363, 1.182, 0.590, 1.351, 4.8, 21.0]
speedups = [0.008, 0.018, 0.214, 0.859, 6.13, 6.74]

# Configuração do gráfico
plt.figure(figsize=(10, 6))
x = np.arange(len(tamanhos))
width = 0.35

# Barras
bars1 = plt.bar(x - width/2, tempo_seq_ms, width, label='Sequencial', color='#1f77b4')
bars2 = plt.bar(x + width/2, tempo_par_ms, width, label='Paralelo', color='#ff7f0e')

# Linha de speedup
ax2 = plt.gca().twinx()
line, = ax2.plot(x, speedups, 'D-', color='red', label='Speedup')  # Note a vírgula após 'line'
ax2.axhline(1, color='gray', linestyle='--')

# Anotações e formatação
plt.xticks(x, tamanhos)
plt.title('Comparação de Desempenho: Sequencial vs Paralelo')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo (ms)')
ax2.set_ylabel('Speedup (x)')

# Legendas unificadas (correção principal aqui)
handles = [*bars1, *bars2, line]  # Convertendo tuplas para listas e concatenando
labels = [h.get_label() for h in handles]
plt.legend(handles, labels, loc='upper left')

# Exibir o gráfico
plt.tight_layout()
plt.show()