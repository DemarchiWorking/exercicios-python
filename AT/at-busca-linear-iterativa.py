def busca_linear(contatos, nome):
    for contato in contatos:
        if contato['nome'] == nome:
            return contato['telefone']
    return "Nao encontrado"

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
telefone = busca_linear(contatos, nome_busca)

if telefone != "Nao encontrado":
    print(f"Nome : {nome_busca} | Telefone: {telefone}")
else:
    print(telefone)
