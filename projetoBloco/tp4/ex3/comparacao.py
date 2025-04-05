import matplotlib.pyplot as plt

medias = [
    {'Tamanho': 100, 'Média DFS (ms)': 0.055049385, 'Média BFS (ms)': 0.0475, 'Média Diferença (BFS-DFS)': -0.00755, 'Média Razão (BFS/DFS)': 0.86435},
    {'Tamanho': 200, 'Média DFS (ms)': 0.112538975, 'Média BFS (ms)': 0.082358285, 'Média Diferença (BFS-DFS)': -0.03018069, 'Média Razão (BFS/DFS)': 0.7329},
    {'Tamanho': 300, 'Média DFS (ms)': 0.16456704, 'Média BFS (ms)': 0.115823005, 'Média Diferença (BFS-DFS)': -0.048744035, 'Média Razão (BFS/DFS)': 0.70425},
    {'Tamanho': 400, 'Média DFS (ms)': 0.24161123, 'Média BFS (ms)': 0.17335676, 'Média Diferença (BFS-DFS)': -0.06825447, 'Média Razão (BFS/DFS)': 0.71935},
    {'Tamanho': 500, 'Média DFS (ms)': 0.292831925, 'Média BFS (ms)': 0.21984758, 'Média Diferença (BFS-DFS)': -0.072984345, 'Média Razão (BFS/DFS)': 0.7498},
    {'Tamanho': 1000, 'Média DFS (ms)': 0.585829705, 'Média BFS (ms)': 0.426882285, 'Média Diferença (BFS-DFS)': -0.15894742, 'Média Razão (BFS/DFS)': 0.72865},
    {'Tamanho': 1500, 'Média DFS (ms)': 0.883599635, 'Média BFS (ms)': 0.758603735, 'Média Diferença (BFS-DFS)': -0.125, 'Média Razão (BFS/DFS)': 0.8602},
    {'Tamanho': 3000, 'Média DFS (ms)': 2.18788388, 'Média BFS (ms)': 1.645716895, 'Média Diferença (BFS-DFS)': -0.542166985, 'Média Razão (BFS/DFS)': 0.7496}
]

tamanhos = [d['Tamanho'] for d in medias]
tempos_dfs = [d['Média DFS (ms)'] for d in medias]
tempos_bfs = [d['Média BFS (ms)'] for d in medias]

plt.figure(figsize=(10, 6))
plt.plot(tamanhos, tempos_dfs, label='DFS', marker='o')
plt.plot(tamanhos, tempos_bfs, label='BFS', marker='x')

plt.xlabel('Tamanho do Grafo')
plt.ylabel('Tempo de Execução Médio (ms)')
plt.title('Comparação do Tempo de Execução de DFS e BFS por Tamanho do Grafo')
plt.grid(True)
plt.legend()
plt.show()