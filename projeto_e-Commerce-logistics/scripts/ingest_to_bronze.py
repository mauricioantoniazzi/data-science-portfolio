import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp
from delta import *
from dotenv import load_dotenv
import random

# Carrega configs do .env
load_dotenv("config/.env")

# Configuração da Spark Session com suporte a Delta Lake
builder = SparkSession.builder.appName("Ingestão_Bronze") \
  .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
  .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
  .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# --- SIMULAÇÃO DE VOLUME NA BRONZE ---
print("Gerando volume de dados na Bronze...")
data_venda = "2026-02-27"
large_data = [
    {"pedido_id": i, "cliente_id": random.randint(1000, 5000), "produto_id": random.randint(1, 4), 
     "valor": random.uniform(10, 1000), "data": data_venda}
    for i in range(1, 10001) # 10 mil registros
]

# raw_data = [
#     {"pedido_id": 1, "cliente_id": 101, "valor": 250.50, "data": "2026-02-27"},
#     {"pedido_id": 2, "cliente_id": 102, "valor": 100.00, "data": "2026-02-27"}
# ]
# df = spark.createDataFrame(raw_data)
df_raw = spark.createDataFrame(large_data)

# 2. Adiciona Metadados (Data de processamento) - Boa prática de Bronze
df_bronze = df_raw.withColumn("_ingestion_at", current_timestamp())

# 3. Escrita em formato Delta
bronze_path = "data/bronze/vendas_eventos"
df_bronze.write.format("delta").mode("overwrite").save(bronze_path)

print(f"✅ Dados ingeridos na Bronze com sucesso em: {bronze_path}")

