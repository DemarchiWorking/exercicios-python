import matplotlib.pyplot as plt

metodos = [
    "BFS Não Ordenado (Não Orientado)",
    "BFS Ordenado (Não Orientado)",
    "BFS Não Ordenado (Orientado)",
    "BFS Ordenado (Orientado)"
]
tempos = [0.011642, 0.009197, 0.003847, 0.003947]

plt.figure(figsize=(10, 6))
plt.bar(metodos, tempos, color=['blue', 'green', 'orange', 'purple'])
plt.xlabel("Métodos", fontsize=12)
plt.ylabel("Tempo de Execução (ms)", fontsize=12)
plt.title("Comparação de Tempos de Execução - BFS", fontsize=14)
plt.xticks(rotation=20, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
