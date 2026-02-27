# 🚀 Pipeline de Automação: Google Sheets → Airflow → Postgres → n8n → Telegram

Este projeto estabelece um ecossistema completo de **Engenharia de Dados e Automação**, focado na captura, processamento e notificação inteligente de leads qualificados em tempo real.

## 📋 Sobre o Projeto
O objetivo é transformar dados brutos de uma planilha em ações imediatas para o time de marketing/vendas. O pipeline monitora novas entradas, armazena no banco de dados com lógica de deduplicação e dispara notificações personalizadas via Telegram para leads com alto potencial (*Lead Scoring*).

## 🛠️ Tecnologias Utilizadas
* **Python**: Scripting e ingestão de dados.
* **Apache Airflow**: Orquestração e agendamento dos jobs.
* **PostgreSQL**: Banco de dados relacional (Camadas Bronze e Silver).
* **n8n**: Plataforma de automação de fluxo de trabalho (Workflow Automation).
* **Docker & Docker Compose**: Containerização de todo o ambiente.
* **Telegram Bot**: Canal de saída para notificações em tempo real.

## ⚙️ Configuração do Ambiente

### 1. Pré-requisitos
* Docker e Docker Compose instalados.

### 2. Variáveis de Ambiente [IMPORTANTE]
Para que o sistema conecte corretamente ao seu banco de dados, você **deve** configurar as credenciais.

1.  Navegue até a pasta `config/`.
2.  Crie ou edite o arquivo `.env`.
3.  Preencha os seguintes campos com suas informações:

```env
# config/.env
DATABASE=nome_do_seu_banco
USER=seu_usuario_postgres
PASSWORD=sua_senha_segura
```
### 3. Executando o projeto
Para subir todo o ecossistema (Airflow, Postgres, n8n e pgAdmin), execute:

```
docker-compose up -d
```

🏗️ Arquitetura do Pipeline

Ingestão: O Airflow dispara um script Python que consome a API do Google Sheets.

Carga (Load): Os dados são inseridos no Postgres usando a lógica ON CONFLICT (Upsert), evitando duplicidade.

Processamento: Uma DAG monitora a integridade e prepara os dados na camada Silver.

Gatilho (Webhook): O Airflow envia um sinal para o n8n.

Filtro & Notificação: O n8n executa uma query SQL incremental, identifica os novos leads qualificados do dia e envia o resumo para o Telegram.

🧠 Desafios Superados

Persistência de Dados: Configuração de volumes Docker para garantir que workflows do n8n e conexões do pgAdmin não fossem perdidos em reinicializações.

Otimização de Recursos: Uso de queries SQL (COUNT) para processar dados no banco, aliviando o uso de memória do n8n em hardware limitado.

Filtro Incremental: Implementação de lógica de data de criação para evitar notificações repetidas de leads antigos.

🔮 Próximos Passos

[ ] Criar um nó no n8n para limpeza automática de leads com score baixo após X dias.

[ ] Conectar o banco de dados ao Metabase ou Looker Studio para criação de dashboards de performance.
