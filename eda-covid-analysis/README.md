# 🦠 Análise de Dados COVID-19

Este projeto realiza uma Análise Exploratória de Dados (EDA) com dados públicos da pandemia de COVID-19, focando na evolução de casos e mortes ao redor do mundo.

## 📊 Ferramentas utilizadas

- **Python 3.9+**
- **Pandas** para manipulação de dados
- **Matplotlib & Seaborn** para visualização
- **Jupyter Notebook** para desenvolvimento interativo

## 📁 Estrutura

- `notebooks/`: Notebook com as análises
- `data/`: Dataset utilizado
- `images/`: Gráficos salvos

## 📈 Insights principais e Interpretações

### 🔹 1. Taxa de Mortalidade por País

> Analisando a relação entre casos confirmados e mortes, observamos que alguns países apresentam taxas de mortalidade significativamente superiores à média global. Essa métrica, conhecida como *case fatality rate*, pode refletir diferentes fatores, como estrutura de saúde, capacidade de testagem, idade da população e transparência nos dados.

**Principais observações:**
- Países com mais de 100 mil casos foram considerados para evitar distorções.
- A taxa de mortalidade varia bastante, ultrapassando 10% em alguns casos.
- Taxas elevadas podem indicar subnotificação de casos leves ou colapso hospitalar.

---

### 🔹 2. Mortes por 100 Mil Habitantes

> Para uma análise mais justa entre países com populações distintas, calculamos o número de mortes por 100 mil habitantes. Esse indicador destaca o impacto da pandemia de forma proporcional.

**Principais observações:**
- Pequenos países ou territórios com alta concentração de mortes se destacaram no topo do ranking.
- Países grandes como Brasil e Estados Unidos também apresentam valores altos, o que reforça a gravidade da crise sanitária.
- A métrica ajuda a contextualizar melhor os números brutos de mortes.

---

### 🔹 3. Heatmap de Mortes Mensais no Brasil

> O heatmap evidencia os períodos mais críticos da pandemia no Brasil, agregando o total de mortes por mês ao longo dos anos.

**Principais observações:**
- Os picos de mortalidade ocorreram em **junho de 2021** e **março de 2021**, refletindo as ondas mais severas.
- A redução gradativa observada a partir do segundo semestre de 2021 coincide com o avanço da vacinação.
- A sazonalidade fica clara: há ciclos de alta e baixa ao longo do tempo.

---

## 🧠 Conclusões

> A análise exploratória revelou como a pandemia de COVID-19 afetou o Brasil e o mundo de forma desigual. Ao combinar gráficos de evolução temporal, taxas normalizadas e comparações internacionais, conseguimos visualizar padrões de impacto, mortalidade e resposta. Além disso, a aplicação de indicadores como mortes por 100 mil habitantes e taxa de mortalidade permite uma interpretação mais justa dos dados, considerando o tamanho populacional e a estrutura de cada país. O Brasil, em especial, passou por momentos críticos, com destaque para o ano de 2021, onde os registros de mortes diárias atingiram patamares alarmantes.

---

## 📎 Fonte dos dados

[Our World In Data - COVID-19](https://ourworldindata.org/covid-deaths)

## 💡 Próximos passos

- Incluir análise de impacto da vacinação (quando disponível)
- Criar uma versão interativa com Streamlit ou Dash
- Publicar insights em artigos no Medium e LinkedIn
