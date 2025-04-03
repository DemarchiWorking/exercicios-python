# Use uma imagem base com Python
FROM fedora:latest

# Instale os pacotes necessários
RUN dnf update -y && dnf install -y python3 python3-pip && dnf clean all

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o container
COPY . /app

# Defina o comando padrão para iniciar a aplicação
CMD ["python3", "hanoi.py"]
