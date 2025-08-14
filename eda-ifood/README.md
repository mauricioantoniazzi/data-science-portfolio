# 📊 Case de Analista de Dados de CRM do iFood

O iFood é o aplicativo líder de entrega de comida no Brasil, presente em mais de mil cidades. Manter um alto engajamento do cliente é fundamental para o crescimento e a consolidação da posição da empresa como líder de mercado.

Os Analistas de Dados que trabalham na equipe de dados são constantemente desafiados a fornecer insights e valor para a empresa por meio de projetos de escopo aberto. Este case tem a intenção de simular essa situação.

Neste case, é apresentado a você um conjunto de dados de amostra que simula metainformações sobre o cliente e sobre as interações das campanhas do iFood com esse cliente.

Seu desafio é entender os dados, encontrar oportunidades de negócio e insights, e propor qualquer ação orientada por dados para otimizar os resultados das campanhas e gerar valor para a empresa.

---

## 🗂️ Estrutura do Projeto

- `data/ifood_df-csv` → Dados de amostra que simula metainformações sobre o cliente e sobre as interações das campanhas do iFood com esse cliente
- `images/` → Gráficos gerados durante a análise
- `notebooks/ifood.ipynb` → Notebook da análise exploratória

---

## 🔍 Etapas da Análise

1. **Carregamento e entendimento dos dados**
2. **Geração de insights a partir dos dados da base**
3. **Criação de visualizações para suporte às conclusões**

---

## 📈 Passos

### 1. Endendimento da base  
 Em resumo, há um entendimento da base, validando campos nulos, o que cada campo representa e identificando qual será nosso Fato a ser analisado.

### 2. Calcular o número de clientes que representam 20% - Técnica de Pareto
 Considerando a técnica de Pareto separei a base base em 20% do total considerando os clientes que mais gastaram no IFood

### 3. Criar novo atributo para representar os intervalos de idade 
 Como o campo Age, que representa a idade é granular e essa informação é importante para atingir o objetivo, foi necessário criar um novo atributo para que represente as faixas de idade

### 4. Plotar graficos para visualizar a distribuição dos 20% dos clientes por faixa etária  
 Considerando a faixa de idade criada em relação ao total de clientes foi gerado um gráfico de barras para visualizar entre os clientes X a faixa etária qual compra mais dentro do IFood
 
### 5. Criar novo atributo para representar o estado civil dos clientes 
 Para o estado civil, como existe um atributo para cada tipo de estado civil foi criado um novo atributo que representa para cada cliente seu estado civil.

 ### 6. Plotar graficos para visualizar a distribuição dos 20% dos clientes por estado civil  
 Considerando o estado civil do cliente foi gerado um gráfico de barras para visualizar entre os clientes X o estado civil qual compra mais dentro do IFood.
 
### 7. Criar novo atributo para representar os valores gastos com vinhos por cada cliente  
 Como no campo Age, o valor gasto com vinhos também é muito granular e essa informação é importante para atingir o objetivo, foi necessário criar um novo atributo para que represente os valores gastos por cada cliente.
 
### 8. Plotar graficos para visualizar a distribuição dos gastos com vinho  
Considerando o gasto com vinhos por cliente foi gerado um gráfico de barras para visualizar entre os clientes X faixa de valor gasto qual a faixa de valor foi mais consideravel.

---

## ✅ Conclusão

A análise dos dados nos permite visualizar através dos gráficos que clientes com a cima de 40-50 anos tendem a gastar mais no aplicativo. Mostra também que clientes muito mais velhos ou muito novos não tendem a comprar muito.

No gráfico que mostra o percentual conseguimos observar que 26.53% dos clientes estão entre essa faixa de 40-50 anos.

E quando consideramos o estado civil podemos obserar que os casados compram mais no aplicativo. Em uma média de 88.20% os casados chegam a mais de 160 clientes do total, mesmo sabendo que solteiros e que vivem juntos tem uma boa relevancia eles somam bem próximos da média.

Se pegarmos desse total de clientes e observar os produtos comprados, nessa nossa abordagem os vinhos, podemos perceber que eles tendem a comprar vinhos que estão na faixa de 771-R$1500.

Em suma, para que as próximas campanhas possam ser mais bem aproveitadas, podemos considerar fazer campanhas voltada para clientes que possuam esse perfil e garantir também que os produtos não faltem já que estamos buscando aumentar o numero de clientes para que o faturamento aumente na sua proporção.

---

## 🛠️ Como Executar

```bash
git clone https://github.com/seu-usuario/eda-ifood.git
cd eda-ifood
jupyter notebook notebooks/ifood.ipynb