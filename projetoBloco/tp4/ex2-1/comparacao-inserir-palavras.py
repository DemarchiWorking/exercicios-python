import matplotlib.pyplot as plt

funcoes = ['Inserir Palavras (1x)', 'Exibir Palavras (4x)']
tempos = [0.015865, 0.018468]

plt.bar(funcoes, tempos, color=['blue', 'green'])

plt.title('Comparação das Médias de Tempo - Funções da Trie')
plt.xlabel('Funções')
plt.ylabel('Média de Tempo (ms)')

for i, tempo in enumerate(tempos):
    plt.text(i, tempo + 0.0002, f'{tempo:.6f} ms', ha='center')

plt.show()
