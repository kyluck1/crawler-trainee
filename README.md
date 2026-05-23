📌 Como rodar o scraper localmente

▶️ Sem Docker

O scraper pode ser executado localmente com Python:

git clone https://github.com/kyluck1/crawler-trainee
cd crawler-trainee

python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou .venv\Scripts\activate  # Windows

pip install -r requirements.txt
python main.py

🐳 Com Docker

Build da imagem
docker build -t crawler-trainee .
Execução
docker run --rm crawler-trainee

O container executa automaticamente o main.py ao iniciar.

📊 Estrutura dos dados extraídos

Os dados são exportados em dois formatos: JSON e CSV.

📦 Schema (JSON / CSV)

Cada livro segue a estrutura:

{
  "title": "A Light in the Attic",
  "price": 51.77,
  "availability": "In stock",
  "rating": 3
}

🧾 Campos
Campo	Tipo	Descrição
title	string	Nome do livro
price	float	Preço convertido para número
availability	string	Status de estoque
rating	int	Avaliação de 1 a 5

⚙️ Como o pipeline funciona

O pipeline de scraping é dividido em etapas:

1. Paginação automática
O scraper percorre as páginas do site incrementando o número da página até encontrar uma resposta inválida (status ≠ 200).

2. Extração de dados da listagem
Em cada página, os livros são extraídos diretamente dos cards HTML (article.product_pod), sem navegação para páginas de detalhe.

3. Parsing dos dados
Para cada livro são coletados:

título
preço
disponibilidade
rating

4. Normalização dos dados

preço convertido para float
rating convertido de texto para número via RATING_MAP

5. Persistência
Exportação dos dados para:

output/books.json
output/books.csv

🧠 Decisões técnicas e justificativas

🔹 Requests + BeautifulSoup

Escolhido por ser leve e suficiente para um site estático, evitando complexidade desnecessária.

🔹 Estratégia de scraping

O scraping foi realizado diretamente nas páginas de listagem, sem necessidade de requisições adicionais para páginas de detalhe. Essa abordagem foi escolhida para reduzir número de requisições e simplificar o fluxo de extração.
🔹 Conversão de dados

preço → float para permitir análises futuras
rating → int para padronização e possível uso em filtros

🔹 Estrutura modular

Separação em funções facilita:

manutenção
testes
escalabilidade

🔹 Docker com usuário não-root

Boa prática de segurança para evitar execução privilegiada no container.

🔹 CI/CD com GitLab

Pipeline automatizado garante:

qualidade do código (flake8)
validação (pytest)
build consistente

🚀 O que eu faria com mais tempo

📊 Observabilidade e confiabilidade
Implementar logging estruturado (JSON logs) para facilitar análise e monitoramento de execuções em ambientes de produção.
Adicionar métricas de execução (tempo por página, taxa de erro, volume de dados coletados) para melhorar visibilidade do pipeline.
🔁 Resiliência de rede
Implementar retry automático com backoff exponencial para falhas temporárias de rede ou bloqueios leves do servidor.
Adicionar controle de timeouts mais granular por requisição.
🧪 Testes
Expandir a cobertura de testes para incluir:
parsing de HTML (BeautifulSoup)
validação de schema dos dados extraídos
testes de regressão para garantir estabilidade do scraper
Simular respostas HTTP para testes mais previsíveis (mocking).
🗄️ Persistência de dados
Evoluir a exportação atual (JSON/CSV) para um banco de dados relacional ou NoSQL (ex: PostgreSQL ou MongoDB).
Permitir histórico de execuções do scraping, não apenas estado final.
☁️ Deploy e produção
Realizar deploy simulado para ambiente cloud (AWS ECS como referência)
Agendar execução do scraper com cron job ou workflow CI/CD programado.
Separar ambiente de desenvolvimento e produção.
⚡ Escalabilidade e performance
Implementar scraping concorrente (multithreading ou asyncio) para reduzir tempo de execução.
Criar fila de tarefas para controle de URLs (ex: RabbitMQ ou Redis Queue em versões futuras).
🧠 Evoluções futuras mais avançadas
Aplicar técnicas de detecção de mudanças no site (change detection).
Adicionar camada de validação inteligente de dados (data quality checks).
Explorar uso de IA para classificação automática ou enriquecimento dos dados coletados.

🤖 Como foi usado IA no desenvolvimento

A IA foi utilizada como ferramenta de apoio técnico nas seguintes etapas:

🔹 1. Estruturação inicial do projeto

Ajuda na definição de arquitetura simples e modular para o scraper.

🔹 2. Debug e troubleshooting

Uso para entender erros como:

problemas de encoding
falhas em parsing com BeautifulSoup
erros de ambiente virtual e dependências

🔹 3. Boas práticas

Sugestões para:

Dockerfile mais seguro (usuário não-root)
organização de testes com pytest
melhoria de pipeline CI/CD

🔹 4. Limitações observadas
Em alguns casos, sugestões genéricas exigiram adaptação manual
Necessidade de validação humana para decisões de scraping e arquitetura

🧾 Considerações finais

Este projeto foi bastante gratificante e instigante. Nele, consegui aplicar tecnologias que já fazia parte do meu conhecimento, ao mesmo tempo em que explorei novas ferramentas e conceitos durante o desenvolvimento.

A experiência de construir um crawler do zero, lidando com extração de dados, normalização e exportação em múltiplos formatos, reforçou meu interesse por áreas relacionadas a engenharia de dados, automação e backend.

Através deste desafio, tive ainda mais clareza de que esse é o tipo de trabalho que desejo seguir profissionalmente.

Também optei por utilizar Python por ser uma linguagem amplamente utilizada para automação e web scraping, além de oferecer um ecossistema maduro para esse tipo de tarefa, com bibliotecas como Requests, BeautifulSoup e Pandas, que simplificam a extração, tratamento e estruturação dos dados.
👨‍💻 Autor

Fernando Nogueira