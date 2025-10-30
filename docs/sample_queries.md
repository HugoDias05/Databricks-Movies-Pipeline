# 🧪 Sample Queries

This file contains example queries that can be run directly in Databricks to explore the final dataset.

---

## 🎬 Top 10 Movies by Vote Average (at least 100 votes)

```sql
SELECT title, vote_average, vote_count
FROM gold_top_rated_movies
ORDER BY vote_average DESC
LIMIT 10;
```


---

## 🎬 Average Vote Per Year

```sql
SELECT year, ROUND(avg_vote, 2) AS avg_vote
FROM gold_avg_rating_by_year
ORDER BY year;
```

