import matplotlib.pyplot as plt
import numpy as np

labels = [f'Proc {i}' for i in range(1, 11)]  # Rótulos para os 10 pares de barras
tempos_lista = [0.0689, 0.1382, 0.2242, 0.3059, 0.3908, 0.4725, 0.5589, 0.6421, 0.7307, 0.8183]  # Tempos da lista
tempos_heap = [0.0006, 0.0006, 0.0007, 0.0007, 0.0007, 0.0007, 0.0007, 0.0006, 0.0006, 0.0007]  # Tempos do heap

x = np.arange(len(labels))
largura = 0.35

plt.figure(figsize=(12, 6))
plt.bar(x - largura/2, tempos_lista, largura, label='Lista', color='blue')  # Barras azuis (lista)
plt.bar(x + largura/2, tempos_heap, largura, label='Heap', color='red')    # Barras vermelhas (heap)

plt.xlabel('Execuções (pares)')
plt.ylabel('Tempo (ms)')
plt.title('Comparação entre Lista e Heap')
plt.xticks(x, labels)
plt.legend()
plt.grid(axis='y')

plt.tight_layout()
plt.show()
