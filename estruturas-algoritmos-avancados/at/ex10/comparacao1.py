import matplotlib.pyplot as plt

algoritmos = ['Prim - Lista', 'Prim - Matriz', 'Kruskal - Lista', 'Kruskal - Matriz']
tempos_grafo_pequeno = [0.01310, 0.01460, 0.01150, 0.01210]
tempos_grafo_medio = [0.01680, 0.01540, 0.01700, 0.01420]
tempos_grafo_grande = [0.01810, 0.02870, 0.02160, 0.01760]
tempos_grafo_muito_grande = [0.03440, 0.03260, 0.05150, 0.04080]

x = range(len(algoritmos))
width = 0.2

plt.bar(x, tempos_grafo_pequeno, width=width, label='Grafo Pequeno', color='blue')
plt.bar([i + width for i in x], tempos_grafo_medio, width=width, label='Grafo Médio', color='green')
plt.bar([i + 2 * width for i in x], tempos_grafo_grande, width=width, label='Grafo Grande', color='orange')
plt.bar([i + 3 * width for i in x], tempos_grafo_muito_grande, width=width, label='Grafo Muito Grande', color='red')

plt.xlabel('Algoritmos')
plt.ylabel('Tempo de Execução (ms)')
plt.title('Comparação de Tempos de Execução por Algoritmo e Tipo de Grafo')
plt.xticks([i + 1.5 * width for i in x], algoritmos)
plt.legend()
plt.grid(axis='y')

plt.show()
