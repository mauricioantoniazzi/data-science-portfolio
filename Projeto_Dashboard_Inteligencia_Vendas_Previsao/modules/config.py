# ==============================================================================
# CONFIGURAÇÕES DO DASHBOARD
# ==============================================================================
# Este arquivo centraliza todas as constantes e configurações do dashboard

# Medidas disponíveis para análise
MEDIDAS_KPI = [
    'Faturamento Bruto', 
    'Receita Bruta', 
    'Receita Líquida', 
    'Margem',
    'Desconto',
    'Tributos Total', 
    'Custos', 
    'Quantidade'
]

# Dimensões disponíveis para decomposição (Treemap)
DIMENSIONS_TREEMAP = [
    'UF', 
    'Cidade', 
    'Descricao_Produto', 
    'Subcategoria', 
    'Categoria', 
    'Descricao_Canal', 
    'Marca'
]

# KPIs fixos para o Item 1
KPI_FIXED_DISCOUNT = 'Desconto'
KPI_FIXED_MARGIN = 'Margem'

# Configurações de página
PAGE_CONFIG = {
    "page_title": "Dashboard de Análise de Vendas",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# CSS para estilização dos cards
CUSTOM_CSS = """
<style>
[data-testid="stColumn"] {
    height: 100%;
    background-color: #424751;
    margin-top: 24px;
    padding: 16px;
}
</style>
"""

# Mensagens padrão
MESSAGES = {
    "no_data": "Não foi possível carregar os dados. Verifique a conexão com o SQL Server.",
    "no_years": "Selecione pelo menos um ano para visualizar o Treemap.",
    "insufficient_data": "Dados insuficientes (menos de 24 meses) para uma previsão robusta com sazonalidade anual.",
    "completion_success": "Previsões concluídas para todas as categorias com dados suficientes!"
}
