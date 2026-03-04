import os
import random
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp, year, month, to_date
from delta import *
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv("config/.env")

# Precisamos do driver JDBC do Postgres para o Spark
builder = SparkSession.builder.appName("Transform_Silver") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0,org.postgresql:postgresql:42.6.0") \
    .config("spark.jars", "./drivers/postgresql-42.6.0.jar") \

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# --- PROCESSAMENTO SILVER ---

# 1. Leitura da Bronze (Delta)
df_bronze = spark.read.format("delta").load("data/bronze/vendas_eventos")

# 2. Leitura dos Produtos (Postgres via JDBC)
DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = quote_plus(os.getenv('DB_PASSWORD'))
DB_NAME = os.getenv('DB_NAME')

url = f"jdbc:postgresql://{DB_HOST}:{DB_PORT}/{DB_NAME}"

df_produtos = spark.read.format("jdbc") \
    .option("url", url) \
    .option("dbtable", "produtos") \
    .option("user", DB_USER) \
    .option("password", DB_PASSWORD) \
    .option("driver", "org.postgresql.Driver") \
    .load()

# 3. Transformações (Limpando e Enriquecendo)
df_silver = df_bronze.alias("vendas") \
    .join(df_produtos.alias("prod"), col("vendas.produto_id") == col("prod.produto_id"), "left") \
    .select(
        "vendas.pedido_id",
        "vendas.cliente_id",
        "prod.nome_produto",
        "prod.categoria",
        "vendas.valor",
        to_date(col("vendas.data")).alias("data_venda"),
        year(col("vendas.data")).alias("ano"),
        month(col("vendas.data")).alias("mes")
    ) \
    .dropDuplicates(["pedido_id"])

# 4. Escrita com Particionamento (Tuning!)
# Particionar por ano e mes ajuda o dbt/duckdb a ler apenas o necessário no futuro
df_silver.show()

print("### Gravando arquivo delta para a camada SILVER")
df_silver.write.format("delta") \
    .mode("overwrite") \
    .partitionBy("ano", "mes") \
    .save("data/silver/vendas_enriquecidas")

print(f"✅ Camada Silver concluída com {df_silver.count()} registros e particionada por Ano/Mês!")