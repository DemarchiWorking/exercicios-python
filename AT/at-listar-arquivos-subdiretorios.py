import os

def listar_arquivos(diretorio):
    arquivos = []

    for item in os.listdir(diretorio):
        caminho = os.path.join(diretorio, item)

        if os.path.isdir(caminho):
            arquivos.extend(listar_arquivos(caminho))
        else:
            if diretorio != diretorio_principal:
                arquivos.append(caminho)

    return arquivos

# subdiretorios
diretorio_principal = "C:\\Users\\AntonioEduardoSilvei\\Pictures"
arquivos = listar_arquivos(diretorio_principal)
for arquivo in arquivos:
    print(arquivo)

# todos arquivos
#def listar_arquivos(diretorio):
#    arquivos = []
#
#    for item in os.listdir(diretorio):
#        caminho_completo = os.path.join(diretorio, item)
#
#        if os.path.isdir(caminho_completo):
#            arquivos.extend(listar_arquivos(caminho_completo))
#        else:
#            arquivos.append(caminho_completo)

#    return arquivos