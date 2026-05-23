# Imagem base 
FROM python:3.12-slim

# Evita criação de arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Garante logs imediatos no terminal
ENV PYTHONUNBUFFERED=1

# Cria usuário não-root
RUN useradd -m crawleruser

# Define diretório de trabalho
WORKDIR /app

# Copia dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos do projeto
COPY . .

# Cria pasta de output
RUN mkdir -p output

# Dá permissão ao usuário
RUN chown -R crawleruser:crawleruser /app

# Troca para usuário não-root
USER crawleruser

# Comando principal
CMD ["python", "main.py"]