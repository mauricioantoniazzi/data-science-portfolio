# 📊 Análise de Dados - Limite de Crédito

Este projeto realiza uma análise exploratória de dados (EDA) utilizando o dataset com dados de clientes para uma empresa que realiza emprestimos, contendo neste dataset somente informações sobre o salário e o Limite de emprestimo. Queremos fazer uma previsão para saber com base em um determinado salário qual seria o limite de emprestimo liberado para o cliente

---

## 🗂️ Estrutura do Projeto

- `data/BaseDados_RegressaoLinear.xlsx` → Dados do salario e limite de emprestimo dos clientes
- `images/` → Gráficos gerados durante a análise
- `notebooks/eda_regressao_linear.ipynb` → Notebook da análise exploratória

---

## 🔍 Etapas da Análise

1. **Carregamento e entendimento dos dados**
2. **Geração de insights a partir das variáveis salario e limite de emprestimo**
3. **Criação de visualizações para suporte às conclusões**
3. **Aplicação do algoritmo de regressão linear para prever qual será o limite liberado**

---

## 📈 Passos

### 1. Verificando os dados da tabela para ver a necessidade de tratar os dados  
Neste passo como é uma base de teste com dados limpos, não tem a necessidade de tratar os dados. Executando o comando Base_Dados.info() podemos perceber que não existe valores nulos e o Dtype está de acordo com o que precisamos

### 2. Gráfico de dispersão que mostra a relação entre o "salário" no eixo horizontal (x) e "limite_credito" no eixo vertical (y).  
Há uma clara e forte relação positiva entre salário e limite de crédito. Isso significa que, à medida que o salário de uma pessoa aumenta, o limite de crédito que ela possui também tende a aumentar. Os pontos no gráfico tendem a seguir uma linha ascendente da esquerda para a direita

### 3. Mapa de calor (headmap)  
Dado que todo o heatmap está preenchido com a mesma cor escura (rosa/vermelho escuro), e assumindo a convenção usual de heatmaps de dados nulos onde cores escuras indicam a ausência de valores nulos: Não há dados nulos nas colunas "salario" e "limite_credito" para todas as observações (linhas) do seu conjunto de dados

### 4. Gráfico de pares (pair plot)  
Permite visualizar as distribuições univariadas e as relações bivariadas entre múltiplos pares de variáveis em um conjunto de dados. O pair plot reforça a observação anterior de que existe uma relação robusta e direta entre o salário e o limite de crédito neste conjunto de dados. Indivíduos com salários mais altos tendem a receber limites de crédito correspondentemente mais altos. As distribuições individuais de cada variável também fornecem insights sobre a forma como os salários e os limites de crédito estão espalhados dentro da população analisada

### 5. Mapa de calor (headmap de uma matriz de correlação)   
Este heatmap de correlação quantifica a forte relação positiva que já havia sido observada visualmente nos gráficos de dispersão anteriores. Um coeficiente de correlação de 0.94 é extremamente alto, confirmando que o salário e o limite de crédito são variáveis altamente correlacionadas neste conjunto de dados. Isso implica que o salário é um fator determinante muito influente no limite de crédito concedido

### 6. Aplicando algoritmo de regressao linear  
 Foi realizado a separação da base entre o eixo X e o eixo Y que defini o limite de empresitmo.
 Foi separado a base entre treinamento e teste, tanto para o eixo X quando para eixo Y em 30% para teste
 Depois de aplicar a regressão loinear foi aplicado o fit para treinar o modelo
 Em seguida foi calcular o quanto as variaveis se explicaram, usando o metodo score
 Depois foi feito um scatterplot da base novamente mas aplicando o predict sobre o X_teste
 Foi feito o calculo do Erro Quadrático Médio (MSE) - Um valor de RMSE mais baixo indica que o modelo está fazendo previsões mais precisas:
  - Comparando as previsões do modelo com os valores reais do conjunto de teste
  - Calculando a Raiz do Erro Quadrático Médio (RMSE) a partir do MSE, que é uma medida da magnitude média dos erros do seu modelo, expressa na mesma unidade da variável que você está tentando prever
 Para testar o modelo foi criado uma nova previsão com valor ficticio e o modelo pode prever o limite de credito disponível

---

## ✅ Conclusão

A análise dos dados nos permite visualizar através da entrada de um novo salario, qual será o valor do emprestimo.

 Integridade dos Dados (Heatmap de Dados Nulos):
  - O heatmap de dados nulos mostra que não há valores ausentes (nulos) nas colunas 'salario' e 'limite_credito'. Isso é excelente, pois significa que o dataset está completo e não há necessidade de técnicas de tratamento de dados faltantes (como imputação) antes da análise ou modelagem.

 Distribuição das Variáveis Individuais (Pair Plot - Histogramas):
  - Salário: O histograma do salário no pair plot revela que a distribuição não é normal ou simétrica. Há concentrações de salários em faixas específicas, o que pode indicar diferentes níveis de renda dentro da população ou segmentos de empregos. Por exemplo, observam-se picos em torno de R$ 5.000, R$ 10.000-12.500, R$ 15.000-17.500 e perto de R$ 20.000. Isso sugere que os dados podem vir de categorias ou grupos salariais distintos.

  - Limite de Crédito: Da mesma forma, o histograma do limite de crédito exibe uma distribuição não-normal, com múltiplos picos (por exemplo, em torno de R$ 10.000-15.000, R$ 20.000-25.000 e, mais proeminente, R$ 40.000-45.000). Isso sugere que os limites de crédito podem ser atribuídos em "degraus" ou categorias, o que é comum em políticas de crédito de instituições financeiras.

 Relação entre Salário e Limite de Crédito (Gráfico de Dispersão e Correlação):
  - Visualização (Gráfico de Dispersão e Pair Plot): Os gráficos de dispersão mostram uma relação linear e extremamente forte entre salário e limite de crédito. Os pontos se agrupam fortemente ao redor de uma linha reta ascendente. Isso indica que, à medida que o salário aumenta, o limite de crédito concedido também aumenta de forma muito consistente.

  - Quantificação (Heatmap de Correlação): O heatmap de correlação quantifica essa relação com um coeficiente de correlação de Pearson de 0.94. Um valor tão próximo de 1.0 confirma uma correlação positiva quase perfeita. Isso significa que a variação no salário explica uma grande parte da variação no limite de crédito.

 Implicações para Modelagem (RMSE):
  - O fato de ter calculado o RMS E (Root Mean Squared Error) após usar modelo.predict(x_teste) indica que um modelo de regressão foi construído para prever o limite_credito com base no salario.

  - Dada a forte correlação (0.94), espera-se que um modelo simples de regressão (como regressão linear) seja capaz de prever o limite de crédito com alta precisão a partir do salário. Um RMSE baixo confirmaria essa capacidade preditiva. A forte correlação sugere que o salário é, de fato, a variável explicativa mais relevante para o limite de crédito neste dataset.

Em resumo, as análises revelam um dataset limpo, sem valores ausentes, e uma relação extremamente forte, positiva e linear entre o salário e o limite de crédito. O salário é um preditor muito poderoso do limite de crédito, o que torna este dataset ideal para construir um modelo de regressão para prever o limite de crédito com base no salário.

---

## 🛠️ Como Executar

```bash
git clone https://github.com/seu-usuario/eda-algoritmo-regressao-linear.git
cd eda-algoritmo-regressao-linear
jupyter notebook notebooks/eda_regressao_linear.ipynb
