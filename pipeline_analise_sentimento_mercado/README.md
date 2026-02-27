# 🛒 ETL Pipeline: E-commerce Analytics (Olist Dataset)

Este projeto demonstra um pipeline de dados de nível intermediário utilizando **Apache Airflow**, **Python (Pandas)** e **PostgreSQL**. O objetivo é processar dados brutos de e-commerce, aplicando transformações de negócio e organizando-os em uma estrutura de banco de dados para análise.

## 🏗️ Arquitetura e Fluxo de Dados

O projeto segue a arquitetura de medalhão para garantir a organização e qualidade dos dados:
1.  **Extract (Bronze):** Coleta de CSVs brutos e conversão para formato Parquet (altamente performático).
2.  **Transform (Silver/Gold):** Limpeza de dados, conversão de tipos (Datetime), Joins complexos e criação de métricas de faturamento.
3.  **Load:** Carga automatizada no PostgreSQL utilizando SQLAlchemy.

## 🛠️ Tecnologias Utilizadas
* **Orquestração:** Apache Airflow 3.x (TaskFlow API)
* **Processamento:** Python 3.12, Pandas, PyArrow
* **Banco de Dados:** PostgreSQL & pgAdmin 4
* **Infraestrutura:** Docker & Docker Compose
* **Gerenciamento de Pacotes:** `uv`

## ⚙️ Configuração do Ambiente

### 1. Variáveis de Ambiente
Para que o pipeline conecte corretamente ao banco de dados, você deve configurar as credenciais. 

> **Importante:** Configure o arquivo na pasta `config/.env` com os campos de banco de dados, usuário e senha.

Exemplo de conteúdo para o `config/.env`:
```env
database=db_ecommerce
user=airflow
password=airflow
```
### 2. Inicialização com Docker
No diretório raiz, execute os comandos abaixo para configurar o UID do Airflow e subir os serviços:

```
echo "AIRFLOW_UID=$(id -u)" > .env
docker-compose up -d
```

📂 Estrutura do Repositório
dags/: Definição da DAG orquestradora.

src/: Scripts modulares de ETL (extract.py, transform.py, load.py).

data/: Volumes para persistência de arquivos (Raw, Processing, Gold).

config/: Arquivos de configuração e ambiente.

notebooks/: Exploração inicial e validação dos dados.

🚀 Como Executar
Certifique-se de que os arquivos CSV do Olist estão em data/bronze/.

Acesse o Airflow UI em http://localhost:8081.

Ative a DAG etl_ecommerce_olist_v1.

Monitore a execução e verifique os dados finais no pgAdmin ou via Notebook.
