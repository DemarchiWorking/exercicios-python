# Escolhe uma imagem base com Python
FROM fedora:latest

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . /app

# Atualiza o sistema e instala pacotes necessários
RUN dnf update -y && dnf install -y \
    python3 \
    python3-pip \
    gcc \
    python3-devel \
    && dnf clean all

# Instala as bibliotecas Python necessárias
RUN pip install --no-cache-dir \
    numpy \
    asyncio \
    multiprocess

# Expõe a porta (caso necessário para futuras extensões ou APIs)
EXPOSE 8000

# Define o comando padrão para iniciar um terminal Python interativo
CMD ["python3"]

#Instruções do arquivo docker para o fedora.
#1.	Alterar os diretórios dentro do arquivo docker
#2.	Construir a imagem:
#docker build -t tp5_docker .
#3.	Executar com o commando:
#docker run -it tp5_docker
#Quem estiver com o fedora configurado ou outro Sistema compatível pode executar os seus exercícios diretamente no sistema operacional.

###################################################