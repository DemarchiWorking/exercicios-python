def buscar_palavra(self, palavra):
    inicio = time.perf_counter_ns()  # Início do temporizador
    atual = self.raiz
    for letra in palavra:
        if letra not in atual.filhos:
            fim = time.perf_counter_ns()  # Fim do temporizador
            print(f"'{palavra}' não encontrada (tempo: {(fim - inicio) / 1_000_000:.6f} ms)")
            return False
        atual = atual.filhos[letra]
    fim = time.perf_counter_ns()  # Fim do temporizador
    if atual.fim_palavra:
        print(f"'{palavra}' encontrada em {(fim - inicio) / 1_000_000:.6f} ms")
        return True
    else:
        print(f"'{palavra}' não encontrada (tempo: {(fim - inicio) / 1_000_000:.6f} ms)")
        return False