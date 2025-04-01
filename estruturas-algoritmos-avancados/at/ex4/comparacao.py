import timeit

def lista_adjacencia(vertices, arestas):
    lista = {vertice: [] for vertice in vertices}
    for origem, destino, peso in arestas:
        lista[origem].append((destino, peso))
        lista[destino].append((origem, peso))
    return lista

def matriz_adjacencia(vertices, arestas):
    n = len(vertices)
    matriz = [[0] * n for _ in range(n)]
    for origem, destino, peso in arestas:
        i, j = vertices.index(origem), vertices.index(destino)
        matriz[i][j] = peso
        matriz[j][i] = peso
    return matriz

def comparar_tempo(vertices, arestas):
    lista_tempo = timeit.timeit(lambda: lista_adjacencia(vertices, arestas), number=1)
    matriz_tempo = timeit.timeit(lambda: matriz_adjacencia(vertices, arestas), number=1)
    print(f"Tempo de execução - Lista de Adjacência: {lista_tempo:.6f} segundos")
    print(f"Tempo de execução - Matriz de Adjacência: {matriz_tempo:.6f} segundos")

def inserir_bairros_e_conexoes(n):
    vertices = [f"Bairro{i}" for i in range(n)]
    arestas = [(f"Bairro{i}", f"Bairro{(i+1) % n}", i % 100 + 1) for i in range(n)]
    return vertices, arestas

def menu():
    while True:
        print("\nMenu:")
        print("1. Comparar tempo de execução")
        print("2. Inserir lista de bairros e conexões")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            vertices = ['A', 'B', 'C', 'D', 'E', 'F']
            arestas = [
                ('A', 'B', 4), ('A', 'C', 2),
                ('B', 'D', 5), ('C', 'D', 8),
                ('C', 'E', 3), ('D', 'F', 6),
                ('E', 'F', 1)
            ]
            comparar_tempo(vertices, arestas)
        elif escolha == "2":
            n = int(input("Quantos bairros deseja inserir? "))
            vertices, arestas = inserir_bairros_e_conexoes(n)
            comparar_tempo(vertices, arestas)
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
