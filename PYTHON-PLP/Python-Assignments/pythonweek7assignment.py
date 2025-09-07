# ----------------------------------------
# Assignment: Analyzing Data with Pandas and Visualizing Results with Matplotlib
# ----------------------------------------

# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ----------------------------------------
# Task 1: Load and Explore the Dataset
# ----------------------------------------

try:
    # Load iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # Pandas DataFrame
    df['species'] = df['target'].map(dict(enumerate(iris.target_names)))  # Add species name column
    
    print("✅ Dataset loaded successfully!\n")
    
    # Display first few rows
    print("First 5 rows of the dataset:")
    print(df.head(), "\n")
    
    # Explore structure
    print("Dataset Info:")
    print(df.info(), "\n")
    
    # Check missing values
    print("Missing values per column:")
    print(df.isnull().sum(), "\n")
    
    # Clean dataset (here, iris has no missing values)
    # But if there were, we could fill or drop them:
    # df = df.dropna()  # or df.fillna(df.mean(), inplace=True)
    
except FileNotFoundError:
    print("Error: Dataset file not found.")
except Exception as e:
    print(f"Error loading dataset: {e}")

# ----------------------------------------
# Task 2: Basic Data Analysis
# ----------------------------------------

print("\nBasic Statistics (Numerical Columns):")
print(df.describe(), "\n")

# Grouping by species and calculating mean values
species_grouped = df.groupby("species").mean()
print("Mean of numerical columns grouped by species:")
print(species_grouped, "\n")

# Identify patterns
print("🔍 Observation: Setosa tends to have smaller sepal and petal sizes compared to Virginica.")

# ----------------------------------------
# Task 3: Data Visualization
# ----------------------------------------

# Line Chart (example: petal length across samples)
plt.figure(figsize=(8, 5))
plt.plot(df.index, df["petal length (cm)"], label="Petal Length", color="blue")
plt.title("Line Chart: Petal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# Bar Chart (average petal length per species)
plt.figure(figsize=(8, 5))
species_grouped["petal length (cm)"].plot(kind="bar", color=["green", "orange", "purple"])
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# Histogram (distribution of sepal length)
plt.figure(figsize=(8, 5))
plt.hist(df["sepal length (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot (Sepal length vs Petal length)
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species", palette="Set1")
plt.title("Scatter Plot: Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
