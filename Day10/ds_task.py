import pandas as pd
import seaborn as sns

a = pd.read_csv(r"C:\Users\Lenovo\Desktop\samsung sic\Dataset\universities_ranking.csv")

print(a.isnull().sum())
print(a.notnull().sum())

a_drop = a.dropna()
a_drop = a.dropna(axis = 1)

print(a_drop)
