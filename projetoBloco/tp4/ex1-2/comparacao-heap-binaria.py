import matplotlib.pyplot as plt

tempos_execucao_1 = [0.008016, 0.003807, 0.003797, 0.004819]
tempos_execucao_2 = [0.006432, 0.003727, 0.013897, 0.004989]
topicos = [
    "Criar Max-Heap",
    "Inserção Max-Heap",
    "Exibir Heap",
    "Criar Min-Heap"
]

medias = [(t1 + t2) / 2 for t1, t2 in zip(tempos_execucao_1, tempos_execucao_2)]

plt.figure(figsize=(10, 6))
plt.bar(topicos, medias, color='skyblue')

plt.title("Média de Tempo por Tópico", fontsize=14)
plt.xlabel("Tópicos", fontsize=12)
plt.ylabel("Tempo Médio (ms)", fontsize=12)
plt.xticks(rotation=15)
plt.tight_layout()

plt.show()
