import matplotlib.pyplot as plt


tempos_simples = [0.01372, 0.01591]
tempos_heap = [0.01238, 0.01229]

media_simples = sum(tempos_simples) / len(tempos_simples)
media_heap = sum(tempos_heap) / len(tempos_heap)

print(f"Média - Prim Simples: {media_simples:.5f} ms")
print(f"Média - Prim Heap: {media_heap:.5f} ms")


metodos = ["Prim Simples", "Prim Heap"]
medias = [media_simples, media_heap]

plt.bar(metodos, medias, color=["blue", "green"])
plt.title("Comparação de Tempos de Execução (ms)")
plt.ylabel("Tempo Médio (ms)")
plt.xlabel("Método")
plt.show()
