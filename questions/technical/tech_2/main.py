# main.py – Task 2: Biggest Contributor & Top Roles Q1-2024 (Pandas + comments bantuan)

import os, json
import pandas as pd  # familiar using DataFrame

# Using path relatif ke CSV
BASE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.normpath(
    os.path.join(BASE, "..", "..", "..", "source_data", "technical_test_2.csv")
)

def load_dataframe(path=CSV_PATH) -> pd.DataFrame:
    """
    1) Baca CSV → DataFrame
    2) Extract email dari '_meta'
    3) Parse date
    """
    df = pd.read_csv(path)
    # JSON parse: saya minta bantuan ChatGPT untuk syntax df.apply(lambda ...)
    df["email"] = df["_meta"].apply(lambda s: json.loads(s)["email"])
    df["date"]  = pd.to_datetime(df["date"])  # Google: cara convert str→datetime
    return df

def compute_top_contributors(df: pd.DataFrame):
    """
    - Top by project count  (groupby.size() saya googling)
    - Top by total salary   (groupby.max() saya googling)
    """
    proj_counts   = df.groupby("email").size()  # # Google: .size() vs .count()
    top_by_projects = proj_counts.idxmax()

    max_salary    = df.groupby("email")["total_earnings_idr"].max()
    top_by_salary   = max_salary.idxmax()

    return top_by_projects, top_by_salary

def compute_top_roles_q1(df: pd.DataFrame):
    """
    1) Filter Q1-2024
    2) groupby + agg(sum, mean) :: syntax saya cek di Google
    3) sort & head(10)
    """
    q1 = df[(df["date"] >= "2024-01-01") & (df["date"] <= "2024-03-31")]

    agg = (
        q1.groupby(["client_company_id", "project_role"])
          .agg(
            earnings    = ("total_earnings_idr", "sum"),   # Google: sum agg
            avg_hourly  = ("hourly_rate_idr",    "mean")   # Google: mean agg
          )
          .reset_index()
          .sort_values("earnings", ascending=False)
          .head(10)
    )
    return agg

if __name__ == "__main__":
    df = load_dataframe()

    tp, ts = compute_top_contributors(df)
    print("Top by projects   :", tp)
    print("Top by total salary:", ts, "\n")

    print("Top 10 earning roles in Q1-2024:")
    print(compute_top_roles_q1(df).to_string(index=False))
