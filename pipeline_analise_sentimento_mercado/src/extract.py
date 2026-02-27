import pandas as pd
import os

def extract_data(file_name, target_name):
    """
    Lê um CSV da pasta raw e salva em parquet na pasta processing.
    """
    bronze_path = f"data/bronze/{file_name}"
    silver_dir = "data/silver"
    target_path = f"{silver_dir}/{target_name}.parquet"

    # Garante que a pasta de destino existe
    os.makedirs(silver_dir, exist_ok=True)

    print(f"--- Lendo arquivo: {bronze_path} ---")
    
    # Usando chunks para não estourar a RAM
    # Mesmo que o arquivo seja pequeno agora, essa prática é essencial
    df = pd.read_csv(bronze_path)
    
    print(f"--- Salvando {target_name} em Parquet ---")
    df.to_parquet(target_path, index=False, engine='pyarrow')
    print(f"--- {target_name} concluído! ---")
    return target_path # Retornar o caminho ajuda a próxima Task a saber onde ler

# # Essa linha para baixo será comentada quando criar a pipeline
# if __name__ == "__main__":
#     # Teste local (sem precisar de Airflow/Docker)
#     extract_data("olist_orders_dataset.csv", "orders")
#     extract_data("olist_order_items_dataset.csv", "order_items")