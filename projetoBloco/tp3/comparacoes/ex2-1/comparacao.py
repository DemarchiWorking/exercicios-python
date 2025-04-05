import matplotlib.pyplot as plt

tamanhos = ['1k', '10k', '100k', '1M', '10M']
tempos = {
    'Sequencial': [0.000006, 0.000052, 0.000601, 0.006561, 0.062421],
    '2 Threads': [0.000007, 0.000015, 0.000098, 0.001170, 0.012393],
    '4 Threads': [0.001156, 0.000009, 0.000051, 0.000483, 0.015436],
    '8 Threads': [0.002729, 0.001912, 0.001907, 0.005883, 0.013492]
}

plt.figure(figsize=(12, 6))

for label, dados in tempos.items():
    plt.plot(tamanhos, dados, 'o-', label=label)

plt.xlabel('Tamanho da Lista')
plt.ylabel('Tempo Médio (segundos)')
plt.title('Crescimento do Tempo de Execução vs Tamanho da Lista')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Escala logarítmica para melhor visualização
plt.show()