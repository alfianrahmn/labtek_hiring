# Task 2 – Biggest Contributor & Top Roles Q1-2024

## Pendekatan Singkat
1. **Load CSV:** `pd.read_csv()`  
2. **Parse Email:**  
   - `df["_meta"].apply(lambda …)` → JSON parse (bantuan ChatGPT)  
3. **Convert Date:** `pd.to_datetime()` (Google)

## Top Contributors
- `df.groupby("email").size()`  → hitung jumlah proyek (Google)  
- `df.groupby("email")["total_earnings_idr"].max()` → peak earnings (bantuan ChatGPT)  

## Top Roles Q1-2024
1. Filter `2024-01-01` s.d. `2024-03-31`  
2. `groupby(["client_company_id","project_role"])`  
3. `agg(sum, mean)` → total earnings & avg hourly (bantuan ChatGPT)  
4. `sort_values("earnings", asc=False).head(10)`

## Bonus: Data Terlalu Besar
- **Dask:** `dd.read_csv().groupby().agg()`  
- **Database:** COPY → Postgres → `SELECT … GROUP BY`  

> **Catatan Bantuan:**  
> - Banyak fungsi `.groupby().agg()` & `.mean()` saya temukan lewat **Google**.  
> - JSON parsing di Pandas saya minta **ChatGPT** dengan similiar case.  
