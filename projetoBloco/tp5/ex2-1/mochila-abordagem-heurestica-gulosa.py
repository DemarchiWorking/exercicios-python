import timeit

def mochila_gulosa(capacidade, itens):
    if capacidade < 0:
        raise ValueError("a capacidade da mochila não pode ser negativa")

    for peso, valor, nome in itens:
        if peso <= 0:
            raise ValueError(f"peso do item '{nome}' dv ser positivo")
        if valor < 0:
            raise ValueError(f"valor do item '{nome}' n pode ser negativo")

    itens_ordenados = itens.copy()
    itens_ordenados.sort(key=lambda x: x[1] / x[0], reverse=True)

    valor_total = 0
    peso_total = 0
    itens_selecionados = []

    for peso, valor, nome in itens_ordenados:
        if peso_total + peso <= capacidade:
            itens_selecionados.append(nome)
            peso_total += peso
            valor_total += valor

    return itens_selecionados, peso_total, valor_total


itens = [
    (2, 40, "item1"),
    (3, 50, "item2"),
    (5, 100, "item3"),
    (4, 90, "item4"),
]

capacidade = 8

try:
    def executar_e_medirem_tempo():
        global resultado
        resultado = mochila_gulosa(capacidade, itens)

    tempo = timeit.timeit(executar_e_medirem_tempo, number=1) * 1000

    itens_selecionados, peso_total, valor_total = resultado
    print("selecionados:", itens_selecionados)
    print("peso total:", peso_total)
    print("alor total:", valor_total)
    print(f"tempo execucao: {tempo:.6f} ms")
except ValueError as e:
    print(f"(erro): {e}")
