class RedeBancaria:
    def __init__(self):
        self.transacoes = {}

    def adicionar_transacao(self, conta_origem, conta_destino):
        if conta_origem not in self.transacoes:
            self.transacoes[conta_origem] = []
        self.transacoes[conta_origem].append(conta_destino)
        if conta_destino not in self.transacoes:
            self.transacoes[conta_destino] = []
        self.transacoes[conta_destino].append(conta_origem)

    def mostrar_rede(self):
        print("== Mapa das Transações Bancárias: ==")
        for origem, destinos in self.transacoes.items():
            print(f"{origem} -> {', '.join(map(str, destinos))}")
        print()

    def encontrar_ciclos_dfs(self):
        def dfs(conta, caminho):
            if caminho and caminho[-1] == caminho[0]:
                yield caminho
                return
            for vizinho in self.transacoes.get(conta, []):
                if vizinho not in caminho or (vizinho == caminho[0] and len(caminho) > 2):
                    yield from dfs(vizinho, caminho + [vizinho])

        ciclos = []
        visitado = set()
        for conta in self.transacoes:
            if conta not in visitado:
                for ciclo in dfs(conta, [conta]):
                    ciclo_ordenado = tuple(sorted(ciclo))
                    if ciclo_ordenado not in visitado:
                        ciclos.append(ciclo)
                        visitado.add(ciclo_ordenado)

        return ciclos

# Função Menu Interativo
def menu_interativo():
    rede = RedeBancaria()
    print("Criando rede bancária para exemplo de teste.")

    # Criando um exemplo com 15 transações e 5 ciclos
    transacoes = [
        (12345678, 87654321),
        (87654321, 23456789),
        (23456789, 12345678),  # Ciclo 1
        (34567890, 45678901),
        (45678901, 56789012),
        (56789012, 34567890),  # Ciclo 2
        (67890123, 78901234),
        (78901234, 89012345),
        (89012345, 67890123),  # Ciclo 3
        (90123456, 12345678),
        (23456789, 34567890),
        (34567890, 67890123),
        (67890123, 90123456),  # Ciclo 4
        (89012345, 45678901),
        (56789012, 78901234)   # Ciclo 5
    ]

    for origem, destino in transacoes:
        rede.adicionar_transacao(origem, destino)

    while True:
        print("== Menu Interativo: ==")
        print("1. Mostrar Rede")
        print("2. Detectar Todos os Ciclos")
        print("3. Adicionar Transação")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            rede.mostrar_rede()

        elif escolha == '2':
            ciclos = rede.encontrar_ciclos_dfs()
            if ciclos:
                print("[ALERTA]!!! Ciclos encontrados:")
                for ciclo in ciclos:
                    print(f"  - Ciclo: {' -> '.join(map(str, ciclo))}")
            else:
                print("Nenhum ciclo encontrado.")

        elif escolha == '3':
            conta_origem = int(input("Conta de origem: "))
            conta_destino = int(input("Conta de destino: "))
            rede.adicionar_transacao(conta_origem, conta_destino)
            print("Transação adicionada com sucesso!")

        elif escolha == '4':
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida, tente novamente.")

# Executando o Menu
menu_interativo()
