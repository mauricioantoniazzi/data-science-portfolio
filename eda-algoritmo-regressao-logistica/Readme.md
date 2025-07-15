# 📊 Análise de Dados Imobiliária

Este projeto realiza uma análise exploratória de dados (EDA) utilizando o dataset com dados de clientes coletados em uma imobiliária, contendo informações sobre renda, o tipo de renda e se o mesmo possui imóvel.

---

## 🗂️ Estrutura do Projeto

- `data/BaseDados_RegressaoLogistica.xlsx` → Dados brutos de clientes cadastrados em uma imobiliária
- `images/` → Gráficos gerados durante a análise
- `notebooks/airbnb.ipynb` → Notebook da análise exploratória

---

## 🔍 Etapas da Análise

1. **Carregamento e entendimento dos dados**
2. **Geração de insights a partir de variáveis como renda, Tipo de renda e se possui imovel**
3. **Criação de visualizações para suporte às conclusões**
3. **Aplicação do algoritmo de regressão logistica para prever vendas futuras**

---

## 📈 Passos

### 1. Representação gráfica da distribuição dos dados  
Permite que você visualize como os valores estão distribuídos ao longo de um intervalo.

### 2. Representação gráfica utilizando boxplot visualizando a distribuição dos dados  
 Tipo de renda em relação a renda.
 Possui imóvel relação a renda.
 Comprou? em relação a renda
 
 O boxplot é especialmente útil para identificar a presença de outliers (valores atípicos) e para resumir informações estatísticas importantes sobre os dados. Vamos explorar em detalhes as principais características e utilidades do boxplot.

### 3. Gráfico de Dispersão  
 Foi aplicado o scatterplot para visualização de dados que representa a relação entre as variáveis Renda e se o comprou?, permitindo entender a correlação entre essas variáveis.


### 3. Aplicando algoritmo de regressao logistica  
 Foi realizado a separação da base entre as caracteristicas do cliente e a variavel previsor que defini se o cliente comprou ou não o imóvel.
 Foi separado a base entre treinamento e teste, tanto para as caracteristicas quando para a variável previsor em 20% para teste
 Depois de aplicar a regressão logistica foi aplicado o fit para treinar o modelo
 Em seguida foi utilizado o predict no x_teste para validar as previsoes
 Foi utilizado a metrica classification_report para identificar a precisão, recall e acurracy do modelo. Neste modelo tivemos uma acuracia de 0.85, o que significa que 85% das previsões do modelo estavam corretas
 Para testar o modelo foi criado uma nova previsão com valores ficticios e o modelo pode prever se o cliente vai ou não comprar o imóvel

---

## ✅ Conclusão

A análise dos dados nos permite visualizar através da entrada de novos clientes, com base nos dados de entrada, se este cliente compraria ou não o imóvel.

Melhoria na tomada de decisão:
 - Segmentação de Clientes: O modelo pode ajudar a identificar quais clientes têm maior probabilidade de comprar um imóvel. Isso permite que a imobiliária concentre seus esforços de marketing e vendas em leads mais promissores, aumentando a eficiência das campanhas.

 - Personalização de Ofertas: Com base nas previsões do modelo, a imobiliária pode personalizar as ofertas de imóveis para os clientes, apresentando opções que atendam melhor às suas necessidades e preferências.

 Aumento das vendas:
  - Taxa de Conversão: Ao focar em clientes com maior probabilidade de compra, a imobiliária pode aumentar a taxa de conversão, resultando em mais vendas efetivas.

  - Redução do Ciclo de Vendas: O modelo pode ajudar a identificar rapidamente quais imóveis são mais atraentes para determinados perfis de clientes, acelerando o processo de venda.

 Otimização de recursos:
  - Alocação Eficiente de Recursos: Com informações mais precisas sobre quais clientes são mais propensos a comprar, a imobiliária pode otimizar a alocação de recursos, como tempo de agentes de vendas e orçamento de marketing.

  - Redução de Custos: Focar em leads qualificados pode reduzir os custos associados a campanhas de marketing e vendas, pois menos recursos serão desperdiçados em clientes que não estão interessados.

 Melhoria na satisfação do cliente:
  - Atendimento Personalizado: Compreender melhor as necessidades e preferências dos clientes permite que a imobiliária ofereça um atendimento mais personalizado, aumentando a satisfação do cliente.

  - Construção de Relacionamentos: A personalização e a atenção às necessidades dos clientes podem levar a relacionamentos mais fortes e duradouros, resultando em recomendações e negócios repetidos.

A adoção de um modelo de aprendizado de máquina para prever a probabilidade de compra de imóveis pode trazer ganhos substanciais para uma imobiliária, incluindo aumento nas vendas, otimização de recursos, melhoria na satisfação do cliente e insights valiosos sobre o mercado. Esses benefícios não apenas ajudam a imobiliária a se destacar em um mercado competitivo, mas também a construir uma base de clientes mais leal e satisfeita.

---

## 🛠️ Como Executar

```bash
git clone https://github.com/seu-usuario/eda-algoritmo-regressao-logistica.git
cd eda-algoritmo-regressao-logistica
jupyter notebook notebooks/eda_regressao_logistica.ipynb
