# 📈 Mini-Projeto ETL: Orquestração de Cotações (USD/BRL)

Este repositório apresenta um pipeline de dados automatizado para extração, transformação e carga (ETL) de cotações de moedas. O projeto utiliza o **Apache Airflow** para orquestração, rodando em um ambiente totalmente conteinerizado via **Docker** no **WSL2**.



## 🛠️ Stack Tecnológica

* **Orquestrador:** Apache Airflow 2.7.1 (TaskFlow API)
* **Linguagem:** Python 3.9
* **Banco de Dados:** PostgreSQL 13 (Camada de Staging)
* **Interface de Dados:** pgAdmin 4
* **Infraestrutura:** Docker & Docker Compose
* **Sistema Operacional:** Windows Subsystem for Linux (WSL2)

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o Docker Desktop instalado e configurado com a integração WSL2 ativa.

### 2. Configuração de Ambiente (WSL)
No terminal do seu WSL, prepare as permissões e as variáveis de ambiente necessárias para o Airflow:

```bash
# Criar pastas de volume local
mkdir -p dags logs plugins

# Configurar o ID do usuário para evitar erros de permissão no Docker
echo "AIRFLOW_UID=$(id -u)" > .env

# Ajustar permissões (necessário para escrita de logs no WSL)
chmod -R 777 dags logs plugins
```
### 3. Subir a Infraestrutura
Execute o comando abaixo para iniciar os containers em segundo plano:

```bash
docker compose up -d
```

### 4. Configuração da Conexão (Airflow UI)

Para que o pipeline funcione, é necessário configurar a conexão com o banco de dados:

1. Acesse `http://localhost:8080`  
   **Usuário/Senha:** `airflow`

2. Vá em:  
   **Admin → Connections → Add New**

3. Preencha os campos:

   - **Conn Id:** `postgres_default`
   - **Conn Type:** `Postgres`
   - **Host:** `postgres` *(nome do serviço definido no docker-compose)*
   - **Schema/Database:** `airflow`
   - **Login/Password:** `airflow`
   - **Port:** `5432`

## 🏗️ Estrutura do Pipeline (DAG)

A DAG `mini_projeto_cotacao_v1` segue o seguinte fluxo:

1. **Extrair**
   - Consome a API **AwesomeAPI** para buscar o último valor de USD/BRL.

2. **Transformar**
   - Converte os tipos de dados.
   - Limpa o JSON de resposta.
   - Utiliza **Python Decorators**.

3. **Carregar**
   - Insere os dados na tabela `staging_cotacoes` no PostgreSQL.
   - Utiliza o `PostgresHook`.

## 🔧 Troubleshooting (Lições Aprendidas)

Durante o desenvolvimento deste laboratório no WSL2, foram superados desafios técnicos que demonstram maturidade em Engenharia de Dados:

1. **Resolução de Nomes (DNS Docker)**
   - Configuração da comunicação entre containers utilizando o nome do serviço (`postgres`) como host.
   - Correção de erros de tradução de nome de rede.

2. **Persistência de Dados**
   - Implementação de **Docker Volumes nomeados**.
   - Garantia de que:
     - Metadados do Airflow
     - Tabelas do Postgres
     - Registros do pgAdmin  
     sobrevivam ao comando `docker-compose down`.

3. **Evolução da API Airflow**
   - Atualização de parâmetros depreciados da versão 2.4+.
   - Substituição de `schedule_interval` por `schedule`.

4. **Gestão de Permissões Linux/Docker**
   - Ajuste dinâmico de UID via arquivo `.env`.
   - Garantia de:
     - Escrita correta de logs
     - Leitura de DAGs em volumes montados

## 📊 Visualização de Dados

Você pode acompanhar os dados inseridos acessando o **pgAdmin**:

1. Acesse: `http://localhost:5050`  
   **Login:** `admin@admin.com`  
   **Senha:** `admin`

2. Conecte-se ao banco PostgreSQL.

3. Execute a query:

   ```sql
   SELECT * FROM staging_cotacoes;

## 📝 Notas de Configuração

- O arquivo `init.sql` na raiz do projeto é mapeado para o diretório de inicialização do PostgreSQL.
  - Responsável por criar automaticamente a estrutura de tabelas no primeiro boot.

- Para alterar credenciais de banco ou portas:
  - Edite o arquivo `docker-compose.yaml`
  - Atualize também as variáveis no painel do Airflow