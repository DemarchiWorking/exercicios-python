import matplotlib.pyplot as plt

tempos = [
    0.007114,  # DFS Não Ordenado (Não Orientado)
    0.007965,  # DFS Ordenado (Não Orientado)
    0.003125,  # DFS Não Ordenado (Orientado)
    0.005250   # DFS Ordenado (Orientado)
]

labels = [
    "DFS Não Ordenado (Não Orientado)",
    "DFS Ordenado (Não Orientado)",
    "DFS Não Ordenado (Orientado)",
    "DFS Ordenado (Orientado)"
]

plt.figure(figsize=(10, 6))
plt.bar(labels, tempos, color=['blue', 'green', 'orange', 'red'])

plt.title("Comparação dos Tempos de Execução do DFS", fontsize=14)
plt.xlabel("Tipo de Execução", fontsize=12)
plt.ylabel("Tempo (ms)", fontsize=12)
plt.xticks(rotation=25, fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()


plt.show()
