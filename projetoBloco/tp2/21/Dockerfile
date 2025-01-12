# Use uma imagem base do Fedora
FROM fedora:latest

# Instale os pacotes necessários
RUN dnf update -y && \
    dnf install -y python3 python3-pip && \
    dnf clean all

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o container
COPY . /app

# Instale as dependências Python diretamente
RUN pip3 install --no-cache-dir flask matplotlib

# Exponha a porta que o Flask usará
EXPOSE 5000

# Defina o comando padrão para iniciar a aplicação
CMD ["python3", "sequencia.py"]
