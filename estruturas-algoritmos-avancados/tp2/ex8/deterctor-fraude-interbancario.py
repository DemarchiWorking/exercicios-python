class RedeBancaria:
    def __init__(self):
        self.transacoes = {}
        self.instituicoes = {}

    def adicionar_transacao(self, conta_origem, conta_destino, instituicao_origem, instituicao_destino):
        if conta_origem not in self.transacoes:
            self.transacoes[conta_origem] = []
        self.transacoes[conta_origem].append(conta_destino)
        self.instituicoes[(conta_origem, conta_destino)] = (instituicao_origem, instituicao_destino)

    def mostrar_rede(self):
        print("== Mapa das Transações Bancárias: ==")
        for origem, destinos in self.transacoes.items():
            print(f"{origem} -> {', '.join(map(str, destinos))}")
        print()

    def encontrar_todos_ciclos_dfs(self):
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

    def priorizar_transacoes(self):
        transacoes_multi_instituicoes = []
        for (conta_origem, conta_destino), (inst_origem, inst_destino) in self.instituicoes.items():
            if inst_origem != inst_destino:
                transacoes_multi_instituicoes.append((conta_origem, conta_destino, inst_origem, inst_destino))
        return transacoes_multi_instituicoes

# Função Menu Interativo
def menu_interativo():
    rede = RedeBancaria()
    print("Criando rede bancária para exemplo de teste.")

    # Criando um exemplo com 15 transações e 5 ciclos
    transacoes = [
        (12345678, 87654321, 'Banco1', 'Banco2'),
        (87654321, 23456789, 'Banco2', 'Banco3'),
        (23456789, 12345678, 'Banco3', 'Banco1'),  # Ciclo 1
        (34567890, 45678901, 'Banco4', 'Banco4'),
        (45678901, 56789012, 'Banco4', 'Banco4'),
        (56789012, 34567890, 'Banco4', 'Banco4'),  # Ciclo 2
        (67890123, 78901234, 'Banco5', 'Banco5'),
        (78901234, 89012345, 'Banco5', 'Banco5'),
        (89012345, 67890123, 'Banco5', 'Banco5'),  # Ciclo 3
        (90123456, 12345678, 'Banco6', 'Banco1'),
        (23456789, 34567890, 'Banco3', 'Banco4'),
        (34567890, 67890123, 'Banco4', 'Banco5'),
        (67890123, 90123456, 'Banco5', 'Banco6'),  # Ciclo 4
        (89012345, 45678901, 'Banco5', 'Banco4'),
        (56789012, 78901234, 'Banco4', 'Banco5')   # Ciclo 5
    ]

    for origem, destino, inst_origem, inst_destino in transacoes:
        rede.adicionar_transacao(origem, destino, inst_origem, inst_destino)

    while True:
        print("== Menu Interativo: ==")
        print("1. Mostrar Rede")
        print("2. Detectar Todos os Ciclos")
        print("3. Adicionar Transação")
        print("4. Priorizar Transações Multi-Institucionais")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            rede.mostrar_rede()

        elif escolha == '2':
            ciclos = rede.encontrar_todos_ciclos_dfs()
            if ciclos:
                print("[ALERTA]!!! Ciclos encontrados:")
                for ciclo in ciclos:
                    print(f"  - Ciclo: {' -> '.join(map(str, ciclo))}")
            else:
                print("Nenhum ciclo encontrado.")

        elif escolha == '3':
            conta_origem = int(input("Conta de origem: "))
            conta_destino = int(input("Conta de destino: "))
            instituicao_origem = input("Instituição de origem: ")
            instituicao_destino = input("Instituição de destino: ")
            rede.adicionar_transacao(conta_origem, conta_destino, instituicao_origem, instituicao_destino)
            print("Transação adicionada com sucesso!")

        elif escolha == '4':
            transacoes_multi_instituicoes = rede.priorizar_transacoes()
            if transacoes_multi_instituicoes:
                print("🚨 Transações Multi-Institucionais Priorizadas para Investigação:")
                for transacao in transacoes_multi_instituicoes:
                    print(f"  - Transação: {transacao}")
            else:
                print("✔️ Nenhuma transação multi-institucional encontrada.")

        elif escolha == '5':
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida, tente novamente.")

# Executando o Menu
menu_interativo()
