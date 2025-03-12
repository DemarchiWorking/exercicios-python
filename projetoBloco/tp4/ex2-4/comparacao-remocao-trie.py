import matplotlib.pyplot as plt

topico = "Remover Palavra"
tempo = 0.020158

plt.bar(topico, tempo, color='blue')


plt.title('Desempenho de Remoção de Palavra')
plt.xlabel('Tópico')
plt.ylabel('Tempo (ms)')
plt.ylim(0, 0.05)


plt.show()
