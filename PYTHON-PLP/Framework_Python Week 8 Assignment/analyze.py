# analyze.py
import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.helpers import load_metadata, basic_explore, clean_metadata, top_journals, papers_by_year, title_word_freq

# Ensure output folders exist
Path("reports/figures").mkdir(parents=True, exist_ok=True)
Path("data").mkdir(parents=True, exist_ok=True)

# 1) Load
print("Loading data...")
df = load_metadata("data/metadata.csv")
print("Loaded")

# 2) Basic exploration (prints to console)
basic_explore(df)

# 3) Clean & prepare
df_clean = clean_metadata(df)
df_clean.to_csv("data/clean_metadata.csv", index=False)
print("Saved cleaned dataset to data/clean_metadata.csv")

# 4) Publications by year (plot)
print("Plotting publications by year...")
year_counts = papers_by_year(df_clean)
plt.figure(figsize=(8,4))
plt.bar(year_counts.index, year_counts.values)
plt.xlabel("Year")
plt.ylabel("Number of papers")
plt.title("Publications by Year")
plt.tight_layout()
plt.savefig("reports/figures/publications_by_year.png")
plt.close()
print("Saved reports/figures/publications_by_year.png")

# 5) Top journals bar chart
print("Plotting top journals...")
top_j = top_journals(df_clean, 15)
plt.figure(figsize=(10,6))
sns.barplot(x=top_j.values, y=top_j.index)
plt.xlabel("Number of papers")
plt.title("Top 15 Journals")
plt.tight_layout()
plt.savefig("reports/figures/top_journals.png")
plt.close()
print("Saved reports/figures/top_journals.png")

# 6) Title word frequency (print top 20)
print("Computing title word frequencies...")
freq = title_word_freq(df_clean, top_n=50)
print("Top title words (top 20):")
for w, c in freq[:20]:
    print(f"{w}: {c}")

# 7) Optional: save a small sample csv for quick inspection
df_clean[['title','authors','journal','publish_time','abstract']].head(200).to_csv("reports/sample_head200.csv", index=False)
print("Saved reports/sample_head200.csv")
print("Analysis complete.")