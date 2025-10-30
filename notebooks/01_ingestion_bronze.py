# Databricks notebook: Bronze Layer Ingestion
# Author: Hugo Dias
# Description: Read raw CSV imported via UI and save it as a Delta Table (Bronze Layer)

# Read the raw data from the imported UI table
df_raw = spark.table("default.tmdb_movies")

# Show a preview and the schema
df_raw.display()
df_raw.printSchema()

# Write the raw data as a managed Delta table in the Bronze layer
df_raw.write.format("delta").mode("overwrite").saveAsTable("bronze_tmdb_movies")
