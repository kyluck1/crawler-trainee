# Imagem base leve do Python
FROM python:3.12-slim

# Evita criação de arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Garante logs imediatos no terminal
ENV PYTHONUNBUFFERED=1

# Cria usuário não-root
RUN useradd -m crawleruser

# Diretório principal da aplicação
WORKDIR /app

# Copia arquivo de dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos do projeto
COPY . .

# Cria pasta de saída
RUN mkdir -p output

# Ajusta permissões
RUN chown -R crawleruser:crawleruser /app

# Usa usuário não-root
USER crawleruser

# Comando principal
CMD ["python", "main.py"]