# 📊 Dashboard de Inteligência de Vendas e Previsão (Forecasting)

Este dashboard não é apenas uma ferramenta de visualização; é um ecossistema de **Business Intelligence (BI)** focado no setor de Varejo/Tecnologia. Ele resolve o desafio da fragmentação de dados, consolidando métricas históricas e projeções futuras em uma interface única e interativa.

O objetivo principal é permitir que gestores identifiquem **anomalias de mercado** (como a queda de participação da Apple em 2019) e antecipem a demanda futura para otimização de estoque e investimentos em marketing.

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

- **Linguagem:** [Python 3.9+](https://www.python.org/)
- **Interface:** [Streamlit](https://streamlit.io/)
- **Processamento de Dados:** [Pandas](https://pandas.pydata.org/)
- **Visualização:** [Plotly](https://plotly.com/python/) e [Matplotlib](https://matplotlib.org/)
- **Machine Learning:** [Prophet](https://facebook.github.io/prophet/)
- **Banco de Dados:** SQL Server Management Studio

---

## ⚙️ Configuração e Instalação

### 1. Clonar o Repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
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
 - Na raiz do seu projeto, crie uma pasta chamada config.
 - Dentro dessa pasta config, crie um arquivo chamado .env.
 - Abra o arquivo .env e configure seus dados conforme o modelo abaixo:

```Bash
# --- Configurações de Banco de Dados ---
DB_HOST=seu_servidor_ou_ip
DB_NAME=nome_do_seu_banco
DB_USER=seu_usuario_de_acesso
DB_PASS=sua_senha_secreta
```

⚠️ AVISO DE SEGURANÇA: O arquivo config/.env contém senhas reais. Ele não será enviado para o GitHub pois está devidamente configurado no arquivo .gitignore.

### 4. Configurar as Variáveis de Ambiente (.env)

Após concluir a configuração acima, basta rodar o comando:

```Bash
streamlit run app.py
```

### 📂 Estrutura do Projeto

├── app.py              # Arquivo principal que executa o Dashboard <br>
├── components/         # Módulos contendo as funções render_item (1 a 4)<br>
├── config/<br>
│   └── .env            # Configurações de Database, User e Password (Privado)<br>
├── data/               # Bases de dados (opcional)<br>
├── requirements.txt    # Lista de todas as bibliotecas necessárias<br>
└── .gitignore          # Arquivos protegidos que não vão para o servidor<br>

### 🛣️ Roadmap de Futuras Implementações

  [ ] Análise de Cohort: Entender a retenção de clientes por mês de entrada.

  [ ] Exportação de Relatórios: Gerar PDF/Excel dos insights filtrados.

  [ ] Integração de Preços: Analisar a correlação entre alteração de preço e volume de vendas (Elasticidade).

### 🤝 Contribuições

Contribuições são sempre bem-vindas!
- Faça um Fork do projeto.
- Crie uma Branch para sua modificação (git checkout -b feature/MinhaMelhoria).
- Faça o Commit das alterações (git commit -m 'Adicionando nova funcionalidade').
- Envie o Push (git push origin feature/MinhaMelhoria).
- Abra um Pull Request.