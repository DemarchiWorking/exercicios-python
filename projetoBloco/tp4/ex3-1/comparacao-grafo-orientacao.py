import matplotlib.pyplot as plt

tipos_grafo = ["Grafo Não-Orientado", "Grafo Orientado"]
tempos = [0.076143, 0.056907]


plt.bar(tipos_grafo, tempos, color=['blue', 'green'], alpha=0.7)

plt.title("Comparação de Tempo de Execução")
plt.ylabel("Tempo (ms)")
plt.xlabel("Tipos de Grafo")

for i, tempo in enumerate(tempos):
    plt.text(i, tempo + 0.001, f"{tempo:.6f} ms", ha='center')

plt.show()
