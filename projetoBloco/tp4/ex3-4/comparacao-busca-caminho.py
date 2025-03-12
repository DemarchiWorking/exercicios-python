import matplotlib.pyplot as plt

métodos = ['BFS', 'DFS']
tempos_médios = [0.0032, 0.0027]

plt.bar(métodos, tempos_médios, color=['blue', 'orange'])

plt.title('Comparação de Tempo Médio (BFS vs DFS)')
plt.xlabel('Método')
plt.ylabel('Tempo Médio (ms)')
plt.ylim(0, 0.005)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
