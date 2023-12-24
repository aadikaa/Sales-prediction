import pandas as pd
train_df = pd.read_csv("train.csv")
print(train_df.head())
print(len(train_df))
print(train_df.info())
