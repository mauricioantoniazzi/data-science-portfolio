🌦️ Pipeline de Dados Meteorológicos (ETL)

Este projeto demonstra um fluxo completo de ETL (Extract, Transform, Load) orquestrado pelo Apache Airflow, utilizando a API da OpenWeatherMap para coletar dados meteorológicos e armazená-los em um banco de dados relacional Postgres.

Toda a infraestrutura é provisionada via Docker, garantindo isolamento e facilidade na replicação do ambiente.

🚀 Tecnologias Utilizadas
Linguagem: Python 3.x

Orquestração: Apache Airflow

Banco de Dados: PostgreSQL 16

Gerenciamento de Banco: pgAdmin 4

Infraestrutura: Docker & Docker Compose

API de Dados: OpenWeatherMap

🏗️ Arquitetura do Projeto
O pipeline foi modularizado seguindo as melhores práticas de engenharia, separando as responsabilidades em scripts Python distintos:

extract_data.py: Responsável por realizar as requisições HTTP para a API, autenticar e obter os dados brutos em formato JSON.

transform_data.py: Processa os dados brutos, realiza limpeza, normalização e prepara o schema final para o banco de dados.

load_data.py: Gerencia a conexão com o banco Postgres e realiza a inserção (ou atualização) dos dados transformados.

Airflow DAG: O maestro do projeto, que define a ordem de execução, gerencia retentativas em caso de falha e monitora o status de cada etapa.

🛠️ Como Executar o Projeto
Pré-requisitos
Docker e Docker Compose instalados.

Uma chave de API (API Key) do OpenWeatherMap.

Passo a Passo
Clonar o repositório:

Bash
git clone <repositorio>.git
cd <caminho>
Configurar as credenciais:

Crie um arquivo .env ou configure as variáveis de ambiente no docker-compose.yaml com suas credenciais do Postgres e sua API Key.
API_KEY
database
user
password

Subir os containers:

Bash
docker-compose up -d
Acessar as interfaces:

Airflow: http://localhost:8080 (User: airflow / Pass: airflow)

pgAdmin: http://localhost:5050 (User: admin@admin.com / Pass: admin)

📊 Estrutura de Pastas
Plaintext
pipeline_weather/
├── dags/
│   └── weather_dag.py        # Definição da DAG
├── src/
│   ├── extract_data.py       # Extração da API
│   ├── transform_data.py     # Transformação dos dados
│   └── load_data.py          # Carga no Postgres
├── docker-compose.yaml       # Configuração da infraestrutura
└── README.md                 # Documentação

📌 Próximos Passos
[ ] Implementar notificações de falha via Slack/E-mail.

[ ] Criar um dashboard no Power BI ou Metabase conectado ao Postgres.

[ ] Adicionar testes unitários para a etapa de transformação.
