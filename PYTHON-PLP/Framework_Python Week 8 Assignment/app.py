# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from src.helpers import load_metadata, clean_metadata, papers_by_year

st.set_page_config(layout="wide")
st.title("CORD-19 Data Explorer (metadata.csv)")
st.write("Simple exploration of COVID-19 research papers")

@st.cache_data
def get_data():
    df = load_metadata("data/metadata.csv")
    return clean_metadata(df)

df = get_data()

# Year slider
years = df['year'].dropna().astype(int)
if not years.empty:
    min_year, max_year = int(years.min()), int(years.max())
else:
    min_year, max_year = 2019, 2022

year_range = st.slider("Select year range", min_year, max_year, (min_year, max_year))

filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.subheader(f"Papers in selected range: {len(filtered)}")

# Publications by year
counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(counts.index, counts.values)
ax.set_xlabel("Year")
ax.set_ylabel("Number of papers")
ax.set_title("Publications by Year")
st.pyplot(fig)

# Top journals
st.subheader("Top journals")
top_n = st.slider("Top N journals", 5, 30, 10)
top_j = filtered['journal'].fillna("Unknown").value_counts().head(top_n)
fig2, ax2 = plt.subplots(figsize=(8, max(3, top_n*0.3)))
sns.barplot(x=top_j.values, y=top_j.index, ax=ax2)
ax2.set_xlabel("Number of papers")
st.pyplot(fig2)

# Title word cloud
if st.checkbox("Show title word cloud"):
    text = " ".join(filtered['title'].fillna('').astype(str).tolist())
    if text.strip():
        wc = WordCloud(width=800, height=400, background_color='white').generate(text)
        fig3, ax3 = plt.subplots(figsize=(10,5))
        ax3.imshow(wc, interpolation='bilinear')
        ax3.axis('off')
        st.pyplot(fig3)
    else:
        st.info("No titles available for the selection.")

# Sample table
if st.checkbox("Show sample rows (first 200)"):
    st.dataframe(filtered[['title','authors','journal','publish_time','abstract']].head(200))
