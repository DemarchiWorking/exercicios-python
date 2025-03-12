import matplotlib.pyplot as plt

media_tempo = 0.008242

plt.bar(["Média de Tempo de Busca"], [media_tempo], color='blue')

plt.title('Tempo Médio para Busca no Trie')
plt.ylabel('Tempo (ms)')

plt.text(0, media_tempo + 0.0001, f'{media_tempo:.6f} ms', ha='center')


plt.show()
