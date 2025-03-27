import matplotlib.pyplot as plt

tempos_simples = [0.020, 0.023]
tempos_heap = [0.018, 0.019]

media_simples = sum(tempos_simples) / len(tempos_simples)
media_heap = sum(tempos_heap) / len(tempos_heap)

print(f"Média - Djikstra Simples: {media_simples:.5f} ms")
print(f"Média - Djikstra Heap: {media_heap:.5f} ms")

metodos = ["Djikstra Simples", "Djikstra Heap"]
medias = [media_simples, media_heap]

plt.bar(metodos, medias, color=["blue", "green"])
plt.title("Comparação de Tempos de Execução (ms)")
plt.ylabel("Tempo Médio (ms)")
plt.xlabel("Método")
plt.show()