import os

def navegar_diretorios(caminho):
    try:
        with os.scandir(caminho) as entradas:
            for entrada in entradas:
                print(entrada.path)
                if entrada.is_dir(follow_symlinks=False):
                    navegar_diretorios(entrada.path)
    except PermissionError:
        print(f"Permissão negada para acessar {caminho}")


caminho_inicial = 'C:\\Users\\AntonioEduardoSilvei\\Pictures'
navegar_diretorios(caminho_inicial)
