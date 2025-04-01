def lista_adjacencia(vertices, arestas):
    lista = {vertice: [] for vertice in vertices}

    for origem, destino, peso in arestas:
        lista[origem].append((destino, peso))
        lista[destino].append((origem, peso))

    return lista

bairros = ['A', 'B', 'C', 'D', 'E', 'F']
conexoes = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 8), ('C', 'E', 3),
    ('D', 'F', 6),
    ('E', 'F', 1)
]

lista = lista_adjacencia(bairros, conexoes)

print("lista de adjacencia:")
for vertice, vizinhos in lista.items():
    print(f"{vertice}: {vizinhos}")


