import matplotlib.pyplot as plt
import numpy as np

# Seus dados reais (Tamanho n vs Tempo em ms)
tamanhos = np.array([100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200])
tempos_ms = np.array([0.0149, 0.0289, 0.0578, 0.1169, 0.2288, 0.4701, 0.9449, 1.9006, 3.9642, 8.0862])

# Configuração do gráfico
plt.figure(figsize=(12, 6))

# Gráfico principal (linear-linear)
plt.subplot(1, 2, 1)
plt.plot(tamanhos, tempos_ms, 'bo-', label='Tempo real (ms)')
plt.plot(tamanhos, 0.000158 * tamanhos, 'r--', label='O(n) teórico (0.158 µs/n)')  # Ajustado à sua média
plt.xlabel('Tamanho da Árvore (n)')
plt.ylabel('Tempo de Execução (ms)')
plt.title('Relação Linear Direta\nTamanho vs Tempo')
plt.legend()
plt.grid(True)

# Gráfico log-log para confirmar a linearidade
plt.subplot(1, 2, 2)
plt.loglog(tamanhos, tempos_ms, 'bo-', label='Dados reais')
plt.loglog(tamanhos, 0.000158 * tamanhos, 'r--', label='O(n) teórico')
plt.xlabel('Tamanho (n) - Escala log')
plt.ylabel('Tempo (ms) - Escala log')
plt.title('Confirmação Log-Log\n(Inclinação = 1 → O(n))')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()