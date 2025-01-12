# Use uma imagem base com Python
FROM fedora:latest

# Instale os pacotes necessários
RUN dnf update -y && dnf install -y \
    python3 \
    python3-pip \
    gcc \
    python3-devel \
    && dnf clean all

# Instale o setuptools, cython, numpy, pillow, matplotlib e flask
RUN pip install setuptools cython numpy pillow matplotlib flask

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o container
COPY . /app

# Exponha a porta 5000 para o servidor Flask
EXPOSE 5000

# Defina o comando padrão para iniciar a aplicação
CMD ["python3", "processamento_imagens.py"]
