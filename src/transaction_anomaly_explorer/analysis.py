import pandas as pd

df = pd.read_csv("data/transactions.csv")

print(df)
print(df["amount"].mean())

high_value = df[df["amount"] > 5000]

print(high_value)