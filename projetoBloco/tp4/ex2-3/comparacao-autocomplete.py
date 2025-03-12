import matplotlib.pyplot as plt

operacoes = ['Autocomplete 1', 'Autocomplete 2']
tempos = [0.015819, 0.014828]
media = 0.015324

plt.bar(operacoes, tempos, color=['blue', 'green'], label='Tempos Individuais')

plt.axhline(y=media, color='red', linestyle='--', label=f'Média: {media:.6f} ms')

plt.title('Comparação de Tempos - Autocomplete')
plt.xlabel('Operação')
plt.ylabel('Tempo (ms)')
plt.legend()

for i, tempo in enumerate(tempos):
    plt.text(i, tempo + 0.0001, f'{tempo:.6f} ms', ha='center')

plt.show()
