import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv(r"C:\Users\Lenovo\Desktop\samsung sic\Dataset\train.csv", header=2)    # type r before pasting to get rid of delimitters
print(titanic.head(5))
print(titanic.info())

df= sns.load_dataset("titanic", cache=True)
print(df)
df.describe()
df.info()

print(df["deck"].value_counts(dropna = True))
print(df["deck"].value_counts(dropna = False))

df.isnull()
df.notnull()

df.isnull().sum()
df.isnull().sum().sum()

(len(df) - df.count()).sum()
new_df = df.dropna(axis = 1, thresh = 500)
new_df.head()
print(new_df)

age_df = df.dropna(axis = 0, how = "any", subset = ["age"])
len(age_df)
no = df.dropna()
no.isnull().sum()

df = sns.load_dataset("titanic")
avg_age = df["age"].mean()
df["age"] = df["age"].fillna(avg_age)

print(df.head(11))

most = df["embark_town"].mode()[0]
df["embark_town"] = df["embark_town"].fillna(most)












