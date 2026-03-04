📊 E-commerce Analytics Pipeline (Lakehouse & dbt)

Este projeto demonstra a construção de um pipeline de dados moderno seguindo a Arquitetura Medalhão, utilizando Apache Spark para o processamento de grandes volumes e dbt (Data Build Tool) para a modelagem analítica e governança.

🛠️ Tecnologias Utilizadas

 - Docker & Docker Compose: Orquestração do banco de dados de origem (PostgreSQL).

 - Apache Spark (PySpark): Extração e transformação nas camadas Bronze e Silver.

 - Delta Lake: Formato de armazenamento para garantir transações ACID.

 - dbt (Data Build Tool): Modelagem, testes e documentação na camada Gold.

 - DuckDB: Motor SQL OLAP de alta performance para a camada analítica.

 - Harlequin: IDE SQL de terminal para exploração de dados.


🏗️ Arquitetura de Dados

O pipeline está dividido em três estágios lógicos:

1 - Bronze: Dados brutos extraídos do PostgreSQL e armazenados em formato Delta.

2 - Silver: Limpeza, padronização e enriquecimento dos dados via Spark.

3 - Gold: Tabelas de negócio agregadas e validadas, modeladas no dbt sobre o DuckDB.

⚙️ Configuração e Instalação

1. Pré-requisitos
    - Docker instalado.

    - Python 3.10+ (recomendado usar uv ou venv).

2. Configuração de Variáveis de Ambiente

    Conforme a estrutura do projeto, as credenciais de acesso ao banco de dados devem ser configuradas manualmente.

    - Localize o arquivo config/.env.example.

    - Crie uma cópia chamada .env na pasta config/.

    - Preencha os seguintes campos:

        - DB_NAME: Nome do banco de dados.

        - DB_USER: Usuário do PostgreSQL.

        - DB_PASSWORD: Senha configurada no Docker.

3. Execução do Pipeline

```Bash
# 1. Subir o banco de dados de origem
docker-compose up -d

# 2. Executar o processamento Spark (Bronze -> Silver)
python scripts/transform_to_silver.py

# 3. Entrar na pasta do dbt e instalar dependências
cd dbt_project
dbt deps --profiles-dir .

# 4. Executar a modelagem Gold e os Testes
dbt run --profiles-dir .
dbt test --profiles-dir .
```

🔍 Qualidade e Documentação (dbt)

O projeto utiliza o dbt para garantir que os dados da camada Gold sejam confiáveis. Foram aplicados testes de integridade para garantir que métricas como qtd_pedidos não contenham valores negativos ou nulos.

Visualizar Linhagem e Dicionário de Dados
Para visualizar o gráfico de linhagem (Lineage Graph) e a documentação técnica:

```Bash
dbt docs generate --profiles-dir .
dbt docs serve --profiles-dir .
```

📁 Estrutura do Repositório
 - scripts/: Scripts PySpark para processamento de dados.

 - dbt_project/: Modelos SQL, testes e configurações do dbt.

 - data/: (Ignorado no Git) Local onde residem as camadas Bronze, Silver e Gold.

 - config/: Arquivos de configuração de ambiente e conexões.

🚀 Pontos de Destaque
 - Testes Automatizados: Uso do dbt_utils.accepted_range para validação de regras de negócio.

 - Versionamento: Pipeline 100% versionado, permitindo auditoria e rollback.

 - Exploração Rápida: Integração com Harlequin para consultas SQL rápidas no Lakehouse local.
