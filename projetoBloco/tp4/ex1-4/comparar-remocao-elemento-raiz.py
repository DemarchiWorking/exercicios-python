import matplotlib.pyplot as plt

# Tempos médios de execução (em ms)
heaps = ['Min-Heap', 'Max-Heap']
tempos = [0.001706, 0.001760]  # Médias calculadas para Min-Heap e Max-Heap

# Criando o gráfico de barras
plt.bar(heaps, tempos, color=['blue', 'green'])
plt.title('Comparação dos Tempos de Remoção de Raiz - Min-Heap vs Max-Heap')
plt.xlabel('Tipo de Heap')
plt.ylabel('Tempo Médio (ms)')

# Adicionando os valores no topo das barras
for i, tempo in enumerate(tempos):
    plt.text(i, tempo + 0.00001, f'{tempo:.6f} ms', ha='center', fontsize=10)

# Exibir o gráfico
plt.show()
