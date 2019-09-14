import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/greenteabiscuit/pycon_sprint/master/sleep_prefectures.csv')


# for col in df.columns:
#     print(col + ': '+str(df.iloc[1][col]))

# for col in df.columns:
print(df.loc[1,'2016'])