from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
import pandas as pd


gold_path = "data/gold/fact_orders.parquet"
table_name = 'sp_weather'
print(f"--- Lendo dados da Gold: {gold_path} ---")
df = pd.read_parquet(gold_path)

def pipeline():
    try:
        print("ETAPA 1: EXTRACT")
        extract_data("olist_orders_dataset.csv", "orders")
        extract_data("olist_order_items_dataset.csv", "order_items")
        
        print("ETAPA 2: TRANSFORM")
        transform_data()
        
        print("ETAPA 3: LOAD")
        load_data(table_name, df)
        
        print("\n" + "="*60)
        print("✅ Pipeline concluído com sucesso!")
        print("="*60)
        
    except Exception as e:
        print(f"❌ ERRO no Pipeline: {e}")
        import traceback
        traceback.print_exc()
    
pipeline()