# 📊 Análise de Dados do Airbnb - Rio de Janeiro

Este projeto realiza uma análise exploratória de dados (EDA) utilizando o dataset público do [Inside Airbnb](http://insideairbnb.com/get-the-data.html), focado nas listagens de acomodações no Rio de Janeiro. O objetivo é identificar padrões, tendências e insights estratégicos sobre o mercado de hospedagem na cidade.

---

## 🗂️ Estrutura do Projeto

- `data/listings.csv` → Dados brutos da Inside Airbnb (não incluído neste repositório devido ao tamanho)
- `images/` → Gráficos gerados durante a análise
- `notebooks/airbnb.ipynb` → Notebook da análise exploratória
- `requirements.txt` → Dependências do projeto

---

## 🔍 Etapas da Análise

1. **Carregamento e entendimento dos dados**
2. **Limpeza e tratamento de colunas relevantes**
3. **Geração de insights a partir de variáveis como preço, avaliações, localização e tipo de propriedade**
4. **Criação de visualizações para suporte às conclusões**

---

## 📈 Principais Insights

### 1. Preço por tipo de quarto  
Apartamentos inteiros são mais caros, enquanto quartos compartilhados são as opções mais acessíveis.

### 2. Bairros com maior preço médio  
Leblon, Ipanema e Joá lideram o ranking de bairros mais caros.

### 3. Popularidade por bairro  
Copacabana e Ipanema são os bairros com maior número de avaliações, indicando forte demanda.

### 4. Relação entre preço e nota média  
Não há correlação significativa entre preço alto e melhores avaliações.

### 5. Tipos de propriedade e preço médio  
Lofts, casas e apartamentos de serviço têm preços mais elevados que apartamentos comuns.

---

## ✅ Conclusão

A análise dos dados do Airbnb no Rio de Janeiro permitiu identificar padrões importantes sobre o mercado de hospedagem na cidade. Observamos que regiões como Copacabana, Ipanema e Barra da Tijuca concentram a maior parte das avaliações, indicando forte procura turística.

A distribuição de preços varia de acordo com o tipo de quarto e o tipo de propriedade, sendo apartamentos inteiros e imóveis como lofts ou casas os mais valorizados. Curiosamente, não há uma relação direta entre o preço cobrado e a nota de avaliação: imóveis com preços moderados podem ter excelentes avaliações, sugerindo que fatores como limpeza, localização e atendimento são mais decisivos na experiência do hóspede.

Além disso, identificamos uma possível sazonalidade implícita ao observar que imóveis disponíveis por poucos dias no ano tendem a praticar preços mais altos — uma possível indicação de uso estratégico em períodos de alta demanda.

Essa análise oferece uma visão estratégica tanto para hóspedes, que buscam o melhor custo-benefício, quanto para anfitriões e investidores, que podem ajustar suas ofertas com base em padrões reais do mercado local.

---

## 🛠️ Como Executar

```bash
git clone https://github.com/seu-usuario/eda-airbnb-analysis.git
cd eda-airbnb-analysis
pip install -r requirements.txt
jupyter notebook notebooks/eda_airbnb_analysis.ipynb
