import matplotlib.pyplot as plt

categorias = ['Max-Heap', 'Min-Heap']
tempos = [0.00138275, 0.00042825]

plt.bar(categorias, tempos, color=['blue', 'green'])
plt.title('Comparação de Tempos de Busca - Heap')
plt.xlabel('Tipo de Heap')
plt.ylabel('Tempo Médio (ms)')

for i, tempo in enumerate(tempos):
    plt.text(i, tempo + 0.00005, f'{tempo:.7f}', ha='center', fontsize=10)

plt.show()
