import matplotlib.pyplot as plt


metodos = ['Em-ordem', 'Pre-ordem', 'Pos-ordem']
recursivo = [0.00314, 0.00215, 0.00170]  # Médias do recursivo
iterativo = [0.00459, 0.00308, 0.00294]  # Médias do iterativo


x = range(len(metodos))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar([i - width/2 for i in x], recursivo, width, label='Recursivo', color='skyblue')
rects2 = ax.bar([i + width/2 for i in x], iterativo, width, label='Iterativo', color='lightcoral')

ax.set_xlabel('Métodos')
ax.set_ylabel('Tempo Médio (ms)')
ax.set_title('Comparação de Tempo Médio: Recursivo vs Iterativo')
ax.set_xticks(x)
ax.set_xticklabels(metodos)
ax.legend()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.5f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # Deslocamento vertical
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)


plt.tight_layout()
plt.show()