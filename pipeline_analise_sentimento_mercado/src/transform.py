import pandas as pd
import os
import gc

def transform_data():
    silver_dir = "/opt/airflow/data/silver"
    gold_dir = "/opt/airflow/data/gold"
    os.makedirs(gold_dir, exist_ok=True)

    # 1. Leitura Seletiva (Otimização de Colunas)
    cols_orders = ['order_id', 'customer_id', 'order_status', 'order_purchase_timestamp']
    cols_items = ['order_id', 'product_id', 'price', 'freight_value']

    print("--- Carregando dados (Colunas Filtradas) ---")
    df_orders = pd.read_parquet(f"{silver_dir}/orders.parquet", columns=cols_orders)
    
    # 2. Filtragem Precoce (Reduzindo linhas antes do merge)
    df_orders = df_orders[df_orders['order_status'] == 'delivered'].copy()
    
    # 3. OTIMIZAÇÃO DE TIPOS (Downcasting)
    # Reduzindo float64 para float32 e int64 para int32
    df_items = pd.read_parquet(f"{silver_dir}/order_items.parquet", columns=cols_items)
    df_items['price'] = df_items['price'].astype('float32')
    df_items['freight_value'] = df_items['freight_value'].astype('float32')

    print("--- Realizando Merge ---")
    df_final = pd.merge(df_orders, df_items, on='order_id', how='inner')

    # Liberar RAM imediatamente das tabelas originais
    del df_orders
    del df_items
    gc.collect()

    # 4. Cálculo e Datas
    df_final['total_item_value'] = df_final['price'] + df_final['freight_value']
    df_final['order_purchase_timestamp'] = pd.to_datetime(df_final['order_purchase_timestamp'])

    # 5. Salvando e Retornando apenas a confirmação (Evita erro de Assinatura/Token)
    print(f"--- Salvando Tabela Ouro ({len(df_final)} linhas) ---")
    df_final.to_parquet(f"{gold_dir}/fact_orders.parquet", index=False)
    
    print("--- Transformação concluída com sucesso! ---")
    
    # IMPORTANTE: Retornar string, nunca o DataFrame
    return "Processamento Gold concluído"