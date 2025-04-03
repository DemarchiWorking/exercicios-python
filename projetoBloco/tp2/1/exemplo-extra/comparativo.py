import matplotlib.pyplot as plt

methods = ["Síncrono", "Assíncrono (2)", "Assíncrono (4)", "Assíncrono (8)"]
times = [2.31, 1.08, 0.98, 0.84]  # em segundos

plt.figure(figsize=(10, 6))
plt.bar(methods, times, color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])
plt.title("Comparação de Tempo de Execução: Síncrono vs Assíncrono")
plt.xlabel("Método de Download")
plt.ylabel("Tempo (segundos)")
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

for i, v in enumerate(times):
    plt.text(i, v + 0.05, f"{v:.2f}s", ha='center', va='bottom')

# Ajustar layout e exibir
plt.tight_layout()
plt.show()