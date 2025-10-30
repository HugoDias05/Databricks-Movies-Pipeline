# Databricks notebook: Silver Layer Transformation
# Author: Hugo Dias
# Description: Clean and transform raw data, convert types, and save cleaned dataset to Delta (Silver Layer)

from pyspark.sql.functions import col, to_date

# Read raw data from Bronze table
df_bronze = spark.table("bronze_tmdb_movies")

# Clean and transform data
df_silver = (
    df_bronze
    .select(
        col("title"),
        to_date(col("release_date"), "yyyy-MM-dd").alias("release_date"),
        col("vote_average").cast("float"),
        col("vote_count").cast("int"),
        col("popularity").cast("float"),
        col("original_language")
    )
    .na.drop(subset=["title", "release_date"])
)

# Save transformed data to Silver table
df_silver.write.format("delta").mode("overwrite").saveAsTable("silver_tmdb_movies")
