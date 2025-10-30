# Databricks notebook: Gold Layer - Analytics
# Author: Hugo Dias
# Description: Generate analytical tables from cleaned data (Silver) and save them as Delta Tables (Gold)

from pyspark.sql.functions import col, year, avg, sum

# Read data from Silver table
df_silver = spark.table("silver_tmdb_movies")

# Top 10 highest-rated movies (with at least 100 votes)
df_top_rated = (
    df_silver
    .filter(col("vote_count") >= 100)
    .orderBy(col("vote_average").desc())
    .limit(10)
)
df_top_rated.write.format("delta").mode("overwrite").saveAsTable("gold_top_rated_movies")

# Average vote by release year
df_avg_rating_year = (
    df_silver
    .withColumn("year", year("release_date"))
    .groupBy("year")
    .agg(avg("vote_average").alias("avg_vote"))
    .orderBy("year")
)
df_avg_rating_year.write.format("delta").mode("overwrite").saveAsTable("gold_avg_rating_by_year")

# Total votes by original language
df_votes_by_lang = (
    df_silver
    .groupBy("original_language")
    .agg(sum("vote_count").alias("total_votes"))
    .orderBy(col("total_votes").desc())
)
df_votes_by_lang.write.format("delta").mode("overwrite").saveAsTable("gold_votes_by_language")
