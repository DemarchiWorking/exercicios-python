import random
import string

livros = [{'isbn': isbn, 'nome': ''.join(random.choices(string.ascii_letters, k=10))}
          for isbn in range(1, 100001)]

livros.sort(key=lambda x: x['isbn'])

isbn_alvo = livros[random.randint(0, 99999)]['isbn']

def busca_binaria(livros, isbn_alvo):
    esquerdo, direito = 0, len(livros) - 1
    iteracoes = 0
    while esquerdo <= direito:
        iteracoes += 1
        meio = (esquerdo + direito) // 2
        if livros[meio]['isbn'] == isbn_alvo:
            return meio, iteracoes
        elif livros[meio]['isbn'] < isbn_alvo:
            esquerdo = meio + 1
        else:
            direito = meio - 1
    return -1, iteracoes
def busca_linear(livros, isbn_alvo):
    iteracoes = 0

    for i, livro in enumerate(livros):
        iteracoes += 1
        if livro['isbn'] == isbn_alvo:
            return i, iteracoes
    return -1, iteracoes
def escolha_busca(tipo_busca):
    if tipo_busca == 1:
        resultado, iteracoes = busca_binaria(livros, isbn_alvo)
        metodo = "Busca Binária"
    elif tipo_busca == 2:
        resultado, iteracoes = busca_linear(livros, isbn_alvo)
        metodo = "Busca Linear"
    else:
        return "Tipo de busca inválido."
    if resultado != -1:
        return f"{metodo} encontrou o ISBN em {iteracoes} iterações."
    else:
        return f"{metodo} não encontrou o ISBN."

print(escolha_busca(1));print(escolha_busca(2))
