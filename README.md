# 🎬 Databricks Movie Pipeline

This project demonstrates a complete **Data Engineering pipeline using Databricks and Delta Lake**, following the Medallion Architecture (Bronze, Silver, Gold).

## 💡 Project Overview

- **Source**: TMDB Movies Dataset (CSV)
- **Platform**: Databricks Community Edition
- **Technologies**: Apache Spark, Delta Lake, PySpark
- **Architecture**: Medallion (Bronze, Silver, Gold)

## 🧱 Pipeline Structure

1. **Bronze**: Raw ingestion from CSV into Delta table
2. **Silver**: Data cleaning and type transformation
3. **Gold**: Aggregated analytics for reporting

## 📊 Example Queries (Gold)
See [`docs/sample_queries.md`](docs/sample_queries.md) for sample SQL queries over the Gold and Silver tables.

- Top 10 highest-rated movies
- Average vote per year
- Total votes per language

## 🖼️ Architecture Diagram

<img width="279" height="395" alt="Image" src="https://github.com/user-attachments/assets/a88c61fa-681f-4ee5-93d1-e8b7ceac42e3" />

## 🧪 Screenshots

  **Gold Diplays:**
  
![Image](https://github.com/user-attachments/assets/9c581795-4b03-48a4-b54f-9ffb76799793)
![Image](https://github.com/user-attachments/assets/161adfaf-d41e-41b3-a585-ef494eb58ff8)
![Image](https://github.com/user-attachments/assets/d0ca23e9-29a1-4774-a337-71dbc7211976)

## 🚀 How to Run

> This project was built entirely in [Databricks Community Edition](https://community.cloud.databricks.com)

1. Clone this repository
2. Import notebooks into Databricks
3. Upload `tmdb-movies.csv` using "Add Data"
4. Attach a cluster and run step by step

## 📊 Dashboard Example

Below is a sample visualization built using the Databricks built-in dashboard tool, based on the Gold layer data.

This chart shows the **average movie rating per year**, using cleaned and transformed data from the Silver table.

![Gold Layer Dashboard Example](https://github.com/user-attachments/assets/22016b36-34f3-403a-9d1a-2e8847bc740c)


## 📂 Folder Structure

| Folder | Description |
|--------|-------------|
| `notebooks/` | Databricks notebooks (Bronze, Silver, Gold) |
| `datasets/` | Source CSV file |
| `docs/` | Diagram and notes |
| `images/` | Screenshots and visual assets |


