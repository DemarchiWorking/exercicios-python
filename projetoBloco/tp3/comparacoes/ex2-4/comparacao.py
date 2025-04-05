import matplotlib.pyplot as plt

intervalos = ['1-1.000', '1-5.000', '1-10.000', '1-50.000', '1-100.000']
tempos_seq = [0.000203, 0.001732, 0.004218, 0.032886, 0.088833]
tempos_par = [0.001311, 0.003007, 0.005523, 0.015196, 0.034965]

plt.figure(figsize=(10, 5))

plt.plot(intervalos, tempos_seq, 'b-o', label='Sequencial', linewidth=2)
plt.plot(intervalos, tempos_par, 'r--s', label='Paralelo', linewidth=2)

plt.xlabel('Intervalo de Números')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Comparação de Tempos: Sequencial vs Paralelo')
plt.legend()

plt.tight_layout()
plt.show()