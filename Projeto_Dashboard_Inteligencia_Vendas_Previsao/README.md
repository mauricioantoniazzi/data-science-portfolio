# 📊 Dashboard de Inteligência de Vendas e Previsão (Forecasting)

Este dashboard não é apenas uma ferramenta de visualização; é um ecossistema de **Business Intelligence (BI)** focado no setor de Varejo/Tecnologia. Ele resolve o desafio da fragmentação de dados, consolidando métricas históricas e projeções futuras em uma interface única e interativa.

O objetivo principal é permitir que gestores identifiquem **anomalias de mercado** (como a queda de participação da Apple em 2019) e antecipem a demanda futura para otimização de estoque e investimentos em marketing.

Este projeto utiliza **dbt** para transformação de dados no SQL Server e **Streamlit** para visualização estratégica.

---

## 🚀 Funcionalidades Principais

O dashboard está dividido em quatro módulos principais de análise:

### 1. Principais Indicadores e Análise Temporal
- Visualização de KPIs críticos (Receita Líquida, Volume, Ticket Médio).
- Comparativo Ano a Ano (YoY) para identificar crescimento ou retração.
- Gráficos de evolução mensal para análise de sazonalidade histórica.

### 2. Visão Geográfica (Mapas)
- Distribuição de vendas por região e estado.
- Identificação de clusters de desempenho geográfico.

### 3. Decomposição Dinâmica (Treemap Multi-Ano)
- Análise de hierarquia de dados (Canal -> Marca -> Produto).
- **Recurso Exclusivo:** Comparação lado a lado de múltiplos anos para validar migração de *market share*.
- Drill-down interativo para identificar drivers de queda ou sucesso.

### 4. Previsão de Vendas (Forecasting com Prophet)
- Utilização do modelo **Prophet (Facebook)** para prever tendências futuras.
- Decomposição de componentes: visualização clara da **Tendência de Longo Prazo** e **Sazonalidade Anual**.
- Suporte para análise de cenários (*What-If*) e ajuste de horizonte de previsão.

---
## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python 3.12](https://www.python.org/)
- **Interface:** [Streamlit](https://streamlit.io/)
- **Processamento de Dados:** [Pandas](https://pandas.pydata.org/)
- **Visualização:** [Plotly](https://plotly.com/python/) e [Matplotlib](https://matplotlib.org/)
- **Machine Learning:** [Prophet](https://facebook.github.io/prophet/)
- **Banco de Dados:** SQL Server Management Studio (Instância: Antoniazzi)
- **Driver SQL Server:** ODBC Driver 17 for SQL Server

---

## ⚙️ Configuração e Instalação

### 1. Clonar o Repositório
```bash
git clone <repositorio no github>
cd seu-repositorio
```

### 2.Configurar o Ambiente Virtual (Python venv)

O ambiente virtual garante que as bibliotecas deste projeto não entrem em conflito com outras versões no seu computador.

No Windows:
```Bash
python -m venv venv
venv\Scripts\activate
```

No Linux ou macOS:
```Bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências

Com o ambiente virtual ativado, instale todos os pacotes necessários de uma só vez:

```Bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente (.env)

Este projeto utiliza um arquivo oculto para proteger suas credenciais de banco de dados.
 - Dentro dessa pasta config, crie um arquivo chamado .env conforme o modelo de exemplo.
 - Abra o arquivo .env e configure seus dados conforme o modelo abaixo:

```Bash
# --- Configurações de Banco de Dados ---
DB_HOST=seu_servidor_ou_ip
DB_NAME=nome_do_seu_banco
DB_USER=seu_usuario_de_acesso
DB_PASS=sua_senha_secreta
```

### Carga e Transformação de Dados (IMPORTANTE)

Antes de iniciar o Dashboard, você deve rodar o dbt para criar a camada de "Analytics" no seu banco:

```Bash
cd transformacao
python -m dbt.cli.main run
```

### Perguntas de Negócio respondidas nesta etapa:

    -   Curva ABC: Classificação de produtos por relevância de faturamento (80/20).
    -   Segmentação RF: Identificação de clientes "Campeões", "Em Risco" ou "Novos" baseada em Recência e Frequência
    -   Mix por Canal: Análise comparativa de comportamento entre Loja Física e Online

⚠️ AVISO DE SEGURANÇA: O arquivo config/.env contém senhas reais. Ele não será enviado para o GitHub pois está devidamente configurado no arquivo .gitignore.

### 5. Execução do Dashboard

Após concluir a configuração acima, basta rodar o comando:

```Bash
streamlit run app.py
```
---
### 📂 Estrutura do Projeto

├── app.py              # Arquivo principal que executa o Dashboard <br>
├── modules/            # Arquivos referente ao projeto (devo organizar essa parte ainda)<br>
|   └── pages           # Módulos contendo as funções render_item (1 a 4)<br>
├── config/<br>
│   └── .env            # Configurações de Database, User e Password (Privado)<br>
├── database/           # Schema do banco de dados para criação das tabelas<br>
|-- transformacao       # Projeto DBT com a construção dos SQL
├── requirements.txt    # Lista de todas as bibliotecas necessárias<br>
└── .gitignore          # Arquivos protegidos que não vão para o servidor<br>

---
### Amadurecendo o Raciocínio Analítico (SQL + Negócio)

Para "amadurecer" na resposta às perguntas, não olhamos para a tabela, olhamos para o **processo de decisão**. Vamos analisar três perguntas complexas sob a ótica de negócio:

#### A. O "Pareto" de Produtos: "80% do meu faturamento vem de quais produtos?"
* **Por trás do SQL:** O negócio quer saber se a operação é dependente de poucos itens ("risco de portfólio") ou se é diversificada.
* **Como chegamos lá:** 1.  Calculamos o faturamento total por produto.
    2.  Ordenamos do maior para o menor.
    3.  Calculamos a **Soma Acumulada** (Running Total) desse faturamento.
    4.  Vemos quais produtos, somados, atingem 80% do valor total da empresa.
* **Raciocínio:** Se apenas 5 produtos fazem 80% da venda, qualquer falta de estoque neles é catastrófica.

#### B. Churn de Clientes: "Quem são os clientes que pararam de comprar?"
* **Por trás do SQL:** Retenção é mais barata que aquisição. O negócio quer uma lista para o time de vendas ligar e oferecer desconto.
* **Como chegamos lá:**
    1.  Identificamos a `MAX(Data_Venda)` de cada cliente.
    2.  Calculamos a diferença (DATEDIFF) entre a última venda dele e a data de **hoje**.
    3.  Filtramos clientes onde essa diferença é maior que a "média de recompra" (ex: > 90 dias).
* **Raciocínio:** Não é apenas "quem não comprou", mas "quem costumava comprar e sumiu".

#### C. Cross-Sell (Venda Cruzada): "Quem compra o Produto A, também leva o B?"
* **Por trás do SQL:** O negócio quer criar "combos" ou sugestões no carrinho de compras.
* **Como chegamos lá:**
    1.  Fazemos um **Self-Join** na tabela de vendas usando o `ID_Pedido`.
    2.  Buscamos produtos diferentes que compartilham o mesmo ID de pedido.
    3.  Contamos a frequência dessas combinações.
* **Raciocínio:** Se Cerveja e Carvão saem juntos 70% das vezes, eles devem estar próximos na gôndola ou no site.

---

### 🚀 Desafio para você:
Escolha uma dessas três análises (Pareto, Churn ou Cross-Sell) ou traga uma dor específica que você imagina no cenário da **Antoniazzi**.

---

### 🛣️ Roadmap de Futuras Implementações

  [ ] Análise de Cohort: Entender a retenção de clientes por mês de entrada.

  [ ] Exportação de Relatórios: Gerar PDF/Excel dos insights filtrados.

  [ ] Integração de Preços: Analisar a correlação entre alteração de preço e volume de vendas (Elasticidade).

---
### 🤝 Contribuições

Contribuições são sempre bem-vindas!
- Faça um Fork do projeto.
- Crie uma Branch para sua modificação (git checkout -b feature/MinhaMelhoria).
- Faça o Commit das alterações (git commit -m 'Adicionando nova funcionalidade').
- Envie o Push (git push origin feature/MinhaMelhoria).
- Abra um Pull Request.