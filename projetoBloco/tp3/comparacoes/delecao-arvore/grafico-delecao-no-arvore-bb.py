import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
tempos_execucoes = [
    {'Nó sem filhos': 0.003998, 'Nó com um filho': 0.001433, 'Nó com dois filhos': 0.001854},
    {'Nó sem filhos': 0.004028, 'Nó com um filho': 0.001492, 'Nó com dois filhos': 0.001773},
    {'Nó sem filhos': 0.003887, 'Nó com um filho': 0.001503, 'Nó com dois filhos': 0.001983}
]

# Calculando médias
medias = {tipo: sum(execucao[tipo] for execucao in tempos_execucoes) / len(tempos_execucoes)
          for tipo in tempos_execucoes[0].keys()}

# Criando gráficos
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Gráfico das médias
axes[0].bar(medias.keys(), medias.values(), color=['#66c2a5', '#fc8d62', '#8da0cb'])
axes[0].set_title("Média dos Tempos de Remoção")
axes[0].set_xlabel("Casos de Remoção")
axes[0].set_ylabel("Tempo Médio (ms)")

# Gráfico das execuções individuais
largura = 0.2
x = np.arange(len(medias))
for i, execucao in enumerate(tempos_execucoes):
    valores = list(execucao.values())
    axes[1].bar(x + i * largura, valores, width=largura, label=f'Execução {i + 1}')
axes[1].set_title("Tempos de Remoção por Execução")
axes[1].set_xlabel("Casos de Remoção")
axes[1].set_ylabel("Tempo (ms)")
axes[1].set_xticks(x + largura)
axes[1].set_xticklabels(medias.keys())
axes[1].legend()

plt.tight_layout()
plt.show()
