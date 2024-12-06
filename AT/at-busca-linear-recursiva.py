def busca_linear_recursiva(contatos, nome, indice=0):
    if indice >= len(contatos):
        return "Nao encontrado"

    if contatos[indice]['nome'] == nome:
        return contatos[indice]['telefone']

    return busca_linear_recursiva(contatos, nome, indice + 1)

contatos = [
    {'nome': 'Ronald', 'telefone': '21-99813-6612'},
    {'nome': 'Eduardo', 'telefone': '21-99815-5341'},
    {'nome': 'Patricia', 'telefone': '21-92456-1154'},
    {'nome': 'Angelo', 'telefone': '21-99671-1143'},
    {'nome': 'Miguel', 'telefone': '21-99813-9841'},
    {'nome': 'Ludmila', 'telefone': '21-99115-4142'},
    {'nome': 'Helena', 'telefone': '21-99136-5188'}
]
nome_busca = 'Helena'
telefone = busca_linear_recursiva(contatos, nome_busca)

if telefone != "Nao encontrado":
    print(f"Nome: {nome_busca} | Telefone {telefone}")
else:
    print(telefone)
