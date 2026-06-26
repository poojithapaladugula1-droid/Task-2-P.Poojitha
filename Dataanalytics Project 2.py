# ==========================================
# PROJECT 2 : EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================

# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Display all columns
pd.set_option('display.max_columns', None)

# Step 2: Load Dataset
df = pd.read_excel("C:/Users/poojitha/Downloads/Cleaned_Data_Analytics_Dataset.xlsx")

print("="*60)
print("DATASET LOADED SUCCESSFULLY")
print("="*60)

# Step 3: View Dataset
print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

# Step 4: Dataset Information
print("\nDataset Information")
print(df.info())

print("\nShape of Dataset")
print(df.shape)

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

# Step 5: Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Step 6: Duplicate Values
print("\nDuplicate Rows")
print(df.duplicated().sum())

# Step 7: Descriptive Statistics
print("\nDescriptive Statistics")
print(df.describe())

# Step 8: Mean
print("\nMean")
print(df.mean(numeric_only=True))

# Step 9: Median
print("\nMedian")
print(df.median(numeric_only=True))

# Step 10: Count
print("\nCount")
print(df.count())

# Step 11: Correlation Matrix
correlation = df.corr(numeric_only=True)

print("\nCorrelation Matrix")
print(correlation)

plt.figure(figsize=(10,8))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Step 12: Histograms
df.hist(figsize=(15,12))
plt.suptitle("Histogram of Numerical Columns")
plt.show()

# Step 13: Boxplots (Outlier Detection)
numeric_columns = df.select_dtypes(include=['number']).columns

for column in numeric_columns:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}")
    plt.show()

# Step 14: Countplots for Categorical Columns
categorical_columns = df.select_dtypes(include=['object']).columns

for column in categorical_columns:
    plt.figure(figsize=(8,5))
    sns.countplot(x=df[column])
    plt.xticks(rotation=45)
    plt.title(f"Countplot of {column}")
    plt.show()

# Step 15: Pair Plot
if len(numeric_columns) <= 6:
    sns.pairplot(df[numeric_columns])
    plt.show()

# Step 16: Value Counts
print("\nCategorical Value Counts")

for column in categorical_columns:
    print("\n")
    print(column)
    print(df[column].value_counts())

# Step 17: Unique Values
print("\nUnique Values")

for column in categorical_columns:
    print(column,":",df[column].nunique())

print("\nEDA COMPLETED SUCCESSFULLY")