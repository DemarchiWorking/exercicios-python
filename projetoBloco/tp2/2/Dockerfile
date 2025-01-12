# Use uma imagem base com Python
FROM fedora:latest

# Instale os pacotes necessários
RUN dnf update -y && dnf install -y \
    python3 \
    python3-pip \
    gcc \
    python3-devel \
    && dnf clean all

# Instale o setuptools, cython e numpy
RUN pip install setuptools cython numpy

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o container
COPY . /app

# Compile o módulo Cython
RUN python3 configuracao.py build_ext --inplace

# Define o comando padrão para iniciar a aplicação
CMD ["python3", "principal.py"]
