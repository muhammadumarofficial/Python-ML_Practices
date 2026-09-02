import pandas as pd
import matplotlib as plt
import numpy as np

#part1
#1.
df = pd.read_csv(r"C:\Users\umarc\Desktop\ML-Lab Practice\clean_churn.csv")
print(df.shape)
print(df.info())
print(df['Churn'].value_counts())

#2.
y = df['Churn'].map({'Yes': 1, 'No': 0})
X = df.drop(columns=['Churn'])
if 'customerID' in X.columns:
    X = X.drop(columns=['customerID'])
#4.
categorical_columns = X.select_dtypes(include='object').columns

X = pd.get_dummies(
    X,
    columns=categorical_columns,
    dtype=int
)
#5.
print("X shape:", X.shape)
print("y shape:", y.shape)

print("\nMissing values in X:")
print(X.isnull().sum())

print("\nData types in X:")
print(X.dtypes)

print("\nTotal missing values:", X.isnull().sum().sum())
print("All columns numeric:",
      X.select_dtypes(exclude='number').shape[1] == 0)