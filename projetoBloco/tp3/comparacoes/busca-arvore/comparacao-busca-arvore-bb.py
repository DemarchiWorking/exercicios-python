import matplotlib.pyplot as plt

# Tempos de inserção (em milissegundos)
tempos_insercao = [0.0025, 0.0026, 0.0008, 0.0009, 0.0007, 0.0006, 0.0005]

# Tempos de busca (em milissegundos)
tempos_busca = [0.0011, 0.0008]

# Tempos de remoção (em milissegundos)
tempos_remocao = [0.0017, 0.0010, 0.0019]

# Calculando as médias
media_tempo_insercao = sum(tempos_insercao) / len(tempos_insercao)
media_tempo_busca = sum(tempos_busca) / len(tempos_busca)
media_tempo_remocao = sum(tempos_remocao) / len(tempos_remocao)

# Criando o gráfico
operacoes = ['Inserção', 'Busca', 'Remoção']
tempos_medios = [media_tempo_insercao, media_tempo_busca, media_tempo_remocao]

plt.bar(operacoes, tempos_medios, color=['blue', 'green', 'red'])
plt.xlabel('Operações')
plt.ylabel('Tempo Médio (ms)')
plt.title('Tempo Médio das Operações na Árvore')
plt.show()
