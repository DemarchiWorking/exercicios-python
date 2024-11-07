def inverter_fila(fila):
    pilha_auxiliar = []

    while fila:
        pilha_auxiliar.append(fila.pop(0))

    while pilha_auxiliar:
        fila.append(pilha_auxiliar.pop())

    return fila

fila_de_pacientes = ["Paciente 1", "Paciente 2","Paciente 3", "Paciente 4"]
print("Fila original:", fila_de_pacientes)
fila_invertida = inverter_fila(fila_de_pacientes)
print("Fila invertida:", fila_invertida)
