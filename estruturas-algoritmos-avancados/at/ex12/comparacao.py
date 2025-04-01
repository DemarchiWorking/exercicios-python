import matplotlib.pyplot as plt


cidades = [4, 7, 14]
tempos_held_karp = [0.02740, 0.32490, 147.11170]
tempos_vizinho = [0.00870, 0.01170, 0.02010]
tempos_genetico = [16.71510, 19.18880, 24.67550]

plt.figure(figsize=(10, 6))
plt.plot(cidades, tempos_held_karp, marker='o', label="Held-Karp", color='blue')
plt.plot(cidades, tempos_vizinho, marker='o', label="Vizinho Mais Próximo", color='green')
plt.plot(cidades, tempos_genetico, marker='o', label="Algoritmo Genético", color='red')

plt.title("Comparação de Tempos de Execução por Quantidade de Cidades")
plt.xlabel("Quantidade de Cidades")
plt.ylabel("Tempo de Execução (ms)")
plt.legend()
plt.grid(True)

plt.show()
