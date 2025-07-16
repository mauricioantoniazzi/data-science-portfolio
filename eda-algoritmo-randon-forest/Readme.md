# 📊 Análise de Dados - Uso de serviços contratado por preço do seguro X idade

Este projeto realiza uma análise exploratória de dados (EDA) utilizando o dataset com dados de clientes coletados em uma empresa de seguros, contendo informações sobre a idade do cliente, preço do seguro, CEP e tipo de serviço utilizado:
 - 1: Não utilizou
 - 2: Usou o serviço
 - 3: Furto

---

## 🗂️ Estrutura do Projeto

- `data/BaseDados_FlorestaDeDecisão.xlsx` → Dados brutos de clientes cadastrados em uma empresa de seguros. O arquivo contem as planilhas Plan1 (dados para treinamento) e a Plan2 (novos dados para prever serviço a ser utilizado)
- `images/` → Gráficos gerados durante a análise
- `notebooks/eda_algoritmo_randon_forest.ipynb` → Notebook da análise exploratória

---

## 🔍 Etapas da Análise

1. **Carregamento e entendimento dos dados**
2. **Geração de insights a partir de variáveis como idade, preço do seguro e CEP**
3. **Criação de visualizações para suporte às conclusões**
3. **Aplicação do algoritmo de floresta aleatória para prever qual tipo de serviço o cliente será o mais provavel utilizado pelo cliente**

---

## 📈 Passos

### 1. Representação gráfica através de um histograma  
Em resumo, o gráfico fornece uma visão geral das características demográficas (Idade, CEP) e do comportamento (Preço Seguro, Serviço) dos clientes, revelando padrões e tendências importantes em cada variável.

### 2. Representação gráfica utilizando boxplot visualizando a distribuição dos dados (serviço X cep)
 Apresenta um gráfico boxplot que mostra a relação entre a variável "Serviço" (que parece ser categórica, com três categorias: 1, 2 e 3) e a variável "CEP". Cada caixa (boxplot) representa a distribuição dos CEPs para cada tipo de serviço

### 3. Representação gráfica utilizando boxplot visualizando a distribuição dos dados (serviço X idade)  
 Apresenta um gráfico boxplot que ilustra a relação entre a variável categórica "Serviço" (com as categorias 1, 2 e 3) e a variável numérica "Idade". Ele nos permite comparar a distribuição das idades dos clientes para cada um dos tipos de serviço

### 4. Representação gráfica utilizando boxplot visualizando a distribuição dos dados (serviço X preço do seguro)  
 Apresenta um gráfico boxplot que mostra a relação entre a variável categórica "Serviço" (com as categorias 1, 2 e 3) e a variável numérica "Preço Seguro". Ele nos permite comparar a distribuição dos preços do seguro para cada um dos tipos de serviço
 
### 5. Aplicando algoritmo de floresta aleatória  
 Foi realizado a separação da base entre as caracteristicas do cliente e a variavel previsor que defini o serviço a ser utilizado.
 Foi separado a base entre treinamento e teste, tanto para as caracteristicas quando para a variável previsor em 30% para teste.
 Depois de aplicar o algoritmo de floresta aleatória foi aplicado o fit para treinar o modelo.
 Em seguida foi utilizado o predict no x_teste para validar as previsoes.
 Foi utilizado a métrica confusion_matrix para descrever o desempenho de um modelo. Neste modelo tivemos uma acuracia de 0.88, o que significa que 88% das previsões do modelo estavam corretas.
 Para testar o modelo foi criado uma nova previsão com valores ficticios e o modelo pode prever qual tipo de serviço o cliente utilizará.
 
### 6. Mapa de calor  
 Apresenta um mapa de calor que nos permite visualizar uma Matriz de Confusão. Uma Matriz de Confusão é uma tabela usada para descrever o desempenho de um modelo de classificação em um conjunto de dados onde os valores verdadeiros são conhecidos.

---

## ✅ Conclusão

A análise dos dados nos permite visualizar através da entrada de novos clientes, com base nos dados de entrada, qual o tipo de serviço o cliente utilizará.

A empresa possui uma clara segmentação de serviços por perfil de cliente, diferenciando-se por faixas etárias, preços e, em certa medida, localização. O Serviço 1 é para o público mais jovem e consciente do preço, o Serviço 2 para idosos com uma gama variada de preços, e o Serviço 3 é um serviço premium para um público maduro e de regiões mais abastadas.

O modelo de classificação (representado pela matriz de confusão) demonstra eficiência na identificação dos clientes do Serviço 1 e do Serviço 3, mas enfrenta dificuldades em classificar corretamente os clientes do Serviço 2. Para melhorar a performance do modelo, seria crucial investigar as características dos clientes do Serviço 2 que estão sendo confundidas com os outros serviços. Isso pode envolver:
 - Engenharia de features: Criar novas variáveis que ajudem a diferenciar melhor o Serviço 2.

 - Coleta de mais dados: Obter dados adicionais para a Classe 1 que possam ter características mais distintivas.

 - Otimização do modelo: Ajustar os parâmetros do modelo ou tentar algoritmos diferentes que lidem melhor com a sobreposição de classes.

Em suma, a empresa parece ter uma estratégia de produto e segmentação de mercado bem definida, e a análise preditiva inicial mostra potencial, mas com um ponto de melhoria claro na identificação de um dos segmentos de serviço.

---

## 🛠️ Como Executar

```bash
git clone https://github.com/seu-usuario/eda-algoritmo-randon-forest.git
cd eda-algoritmo-randon-forest
jupyter notebook notebooks/eda_algoritmo_randon_forest.ipynb
