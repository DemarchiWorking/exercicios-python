import re


class NoTrie:
    def __init__(self):
        # Dicionário de filhos
        self.filhos = {}
        # Atributo para armazenar o telefone (se o nó for o final de um contato)
        self.numero_telefone = None


class Trie:
    def __init__(self):
        self.raiz = NoTrie()

    def validar_nome(self, nome):
        """Valida se o nome do contato é válido (apenas letras e espaços)."""
        return bool(re.match("^[a-zA-ZáéíóúãõçÀ-ú\s]+$", nome))

    def validar_telefone(self, telefone):
        """Valida se o número de telefone tem o formato válido (ex: 1234-5678 ou (12) 3456-7890)."""
        return bool(re.match(r"^(\(\d{2}\)\s?)?\d{4}-\d{4}$", telefone))

    def adicionar_contato(self, nome, numero_telefone):
        """Adiciona um contato à Trie, validando a entrada primeiro."""
        if not self.validar_nome(nome):
            print(f"Erro: O nome '{nome}' não é válido. Somente letras e espaços são permitidos.")
            return
        if not self.validar_telefone(numero_telefone):
            print(
                f"Erro: O telefone '{numero_telefone}' não é válido. O formato esperado é '1234-5678' ou '(12) 3456-7890'.")
            return

        atual = self.raiz

        # Para cada caractere no nome do contato
        for caractere in nome:
            # Se o caractere não existir, criamos um novo nó
            if caractere not in atual.filhos:
                atual.filhos[caractere] = NoTrie()
            # Movemos para o nó correspondente ao caractere
            atual = atual.filhos[caractere]

        # Após percorrer todos os caracteres, definimos o telefone
        atual.numero_telefone = numero_telefone
        print(f"Contato '{nome}' adicionado com sucesso.")

    def buscar_contato(self, nome):
        """Busca um contato na Trie e retorna o número de telefone associado."""
        atual = self.raiz

        # Para cada caractere no nome do contato
        for caractere in nome:
            # Se o caractere não existir, o contato não está presente
            if caractere not in atual.filhos:
                return None
            # Movemos para o próximo nó
            atual = atual.filhos[caractere]

        # Retornamos o telefone se o nó de final de string estiver presente
        return atual.numero_telefone if atual.numero_telefone is not None else None

    def remover_contato(self, nome):
        """Remove um contato da Trie."""
        self._remover_recursivo(self.raiz, nome, 0)

    def _remover_recursivo(self, no_atual, nome, indice):
        """Função auxiliar recursiva para remover um contato."""
        if indice == len(nome):
            if no_atual.numero_telefone is not None:
                no_atual.numero_telefone = None
                print(f"Contato '{nome}' removido com sucesso.")
            else:
                print(f"Erro: O contato '{nome}' não existe.")
            return True

        caractere = nome[indice]
        if caractere in no_atual.filhos:
            if self._remover_recursivo(no_atual.filhos[caractere], nome, indice + 1):
                # Se o nó não tiver filhos, podemos removê-lo
                if not no_atual.filhos[caractere].filhos and no_atual.filhos[caractere].numero_telefone is None:
                    del no_atual.filhos[caractere]
                return True
        return False


def executar_testes():
    trie = Trie()


    trie.adicionar_contato("Antonio Demarchi", "2465-3211")
    trie.adicionar_contato("Marcelo Denis", "2465-5432")
    trie.adicionar_contato("Daniel Rodrigues", "2465-1182")
    trie.adicionar_contato("Maria Julia", "2465-9473")
    trie.adicionar_contato("Roberto Zema", "2465-5182")

    print("Busca Antonio Demarchi:", trie.buscar_contato("Antonio Demarchi"))
    print("Busca Marcelo Denis:", trie.buscar_contato("Marcelo Denis"))
    print("Busca Daniel Rodrigues:", trie.buscar_contato("Daniel Rodrigues"))
    print("Busca Maria Julia:", trie.buscar_contato("Maria Julia"))

    trie.remover_contato("Maria Julia")
    print("Busca Maria Julia após remoção:", trie.buscar_contato("Maria Julia"))
    print("Busca Ant após remoção:", trie.buscar_contato("Ant"))


    trie.adicionar_contato("Evelin Lucia", "abc123")


if __name__ == "__main__":
    executar_testes()
