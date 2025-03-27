import matplotlib.pyplot as plt


tempos_gulosa = [0.014918, 0.016481, 0.018014]
tempos_linear = [0.012463, 0.015018, 0.014798]

media_gulosa = sum(tempos_gulosa) / len(tempos_gulosa)
media_linear = sum(tempos_linear) / len(tempos_linear)

print(f"media - mochila: {media_gulosa:.6f} ms")
print(f"media - mochila: {media_linear:.6f} ms")


metodos = ["Mochila Heurestica Gulosa", "Mochila Linear Aproximada Inteiros"]
medias = [media_gulosa, media_linear]

plt.bar(metodos, medias, color=["blue", "green"])
plt.title("Comparação de Tempos de Execução (ms)")
plt.ylabel("Tempo Médio (ms)")
plt.xlabel("Método")
plt.show()
