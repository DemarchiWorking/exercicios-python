# biblioteca numpy para criar a matriz
import numpy as np

# Matriz 9x9 de zeros (bairros do grafo)
bairros = ['Centro', 'Gonzalés', 'Humberto Antunes', 'Morro do Mathias',
           'Santa Rita', 'Tupinambá', 'Grajaú', 'Bela Vista', 'Independência']
n = len(bairros)
matriz = np.zeros((n, n), dtype=int)

# Definindo as conexões com base no grafo usando índices
conexoes = [
    (0, 1), (0, 6), (0, 2),  # Centro
    (1, 0), (1, 4), (1, 5),  # Gonzalés
    (2, 0), (2, 3),          # Humberto Antunes
    (3, 2),                  # Morro do Mathias
    (4, 1),                  # Santa Rita
    (5, 1),                  # Tupinambá
    (6, 0), (6, 7),          # Grajaú
    (7, 6), (7, 8),          # Bela Vista
    (8, 7)                   # Independência
]

# Preenchendo a matriz com as conexões
for x, y in conexoes:
    matriz[x][y] = 1
    matriz[y][x] = 1  # Adicionando esta linha para grafos não direcionados (bidirecionais)

# Exibindo a matriz de adjacência com rótulos dos bairros
print("Matriz de Adjacência:")
print("   " + "  ".join(bairros))
for i, linha in enumerate(matriz):
    print(f"{bairros[i]:<15} {linha}")
