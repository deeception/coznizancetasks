import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/cognizance-amrita/AI-Tasks/main/Task-1/Q2-Dataset.csv")

# replace missing values with the mean of the column
df.fillna(df.mean(), inplace=True)

# replace missing values with 0
# df.fillna(0, inplace=True)

print(df.head())
