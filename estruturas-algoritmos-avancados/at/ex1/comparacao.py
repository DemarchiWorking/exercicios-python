import matplotlib.pyplot as plt
import numpy as np

# Dados de tempos (convertidos para segundos)
processos = list(range(1000, 10001, 1000))
tempos_lista_insercao = [0.0689, 0.1382, 0.2242, 0.3059, 0.3908, 0.4725, 0.5589, 0.6421, 0.7307, 0.8183]
tempos_heap_insercao = [0.0006, 0.0006, 0.0007, 0.0007, 0.0007, 0.0007, 0.0007, 0.0006, 0.0006, 0.0007]

# Convertendo os tempos totais também
tempo_total_lista = 3975.221 / 1000  # em segundos
tempo_total_heap = 18.2419 / 1000    # em segundos

execucao_lista = 52.8062 / 1000      # em segundos
execucao_heap = 205.5241 / 1000      # em segundos

# Gráfico de comparação de tempos de inserção
plt.figure(figsize=(12, 6))

plt.bar(np.array(processos) - 250, [t / 1000 for t in tempos_lista_insercao], width=500, color='blue', label='Lista (Inserção)')
plt.bar(np.array(processos) + 250, [t / 1000 for t in tempos_heap_insercao], width=500, color='red', label='Heap (Inserção)')

plt.xlabel('Quantidade de processos adicionados')
plt.ylabel('Tempo de Inserção (segundos)')
plt.title('Comparação de Tempos de Inserção: Lista vs Heap')
plt.legend()
plt.grid(axis='y')

plt.show()

fig, ax = plt.subplots(figsize=(8, 5))

labels = ['Lista', 'Heap']
tempos_totais = [tempo_total_lista, tempo_total_heap]
execucoes = [execucao_lista, execucao_heap]

x = np.arange(len(labels))

ax.bar(x - 0.2, tempos_totais, width=0.4, label='Tempo Total de Inserção', color='blue')
ax.bar(x + 0.2, execucoes, width=0.4, label='Tempo Total de Execução', color='red')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Tempo (segundos)')
ax.set_title('Comparação de Tempos Totais: Lista vs Heap')
ax.legend()

plt.show()
