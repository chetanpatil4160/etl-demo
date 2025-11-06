import pandas as pd 

df = pd.read_csv("data/delivery_data.csv")

print("the first five rows is ")
print(df.head())

print(f"\ntotal Number of rows : {len(df)}")