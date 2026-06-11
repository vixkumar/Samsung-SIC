import pandas as pd
import requests
import datetime
from datetime import datetime, timezone
import matplotlib.pyplot as plt

# Fetch the data.
df = pd.read_csv("https://ourworldindata.org/grapher/capture-fisheries-vs-aquaculture.csv?v=1&csvType=full&useColumnShortNames=true", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})

# Fetch the metadata
metadata = requests.get("https://ourworldindata.org/grapher/capture-fisheries-vs-aquaculture.metadata.json?v=1&csvType=full&useColumnShortNames=true").json()

print(df.head())
print(df.info())
print(df.columns)

df.drop(["Code"], axis = 1, inplace = True, errors = "ignore")
df.head()

df.isnull().sum()
change_value = 0
df.fillna(change_value, inplace = True)
df.isnull().sum()

print("Columns are:")
for col in df.columns:
    print(col)


df["new_Year"] = pd.to_datetime(df["year"].astype(str), format = "%Y")
df.set_index("new_Year", inplace=True)
df.drop(["year"], axis = 1, inplace= True)

df.head()
df.info()

new_df = df.sort_index()
new_df.head()

new_df["entity"] = new_df["entity"].astype("category")
new_df.info()
new_df["entity"].value_counts()
g = new_df.groupby(["new_Year"])
g.head()

for key, group in g:
    print("+key: ", key)
    print("+number: ", len(group))
    print(group.head())
    print("\n")

world_total = g.sum(numeric_only = True)
world_total.head()

plt.style.use("ggplot")
world_total.plot (
    kind = "area", alpha = 0.2, stacked = False, figsize = (20,10))
plt.legend()
plt.show()

country = new_df["entity"].value_counts()
print(country)
print("Data type =>", type(country))

s = new_df.loc[new_df["entity"] == "South Korea"]
c = new_df.loc[new_df["entity"] == "China"]
a = new_df.loc[new_df["entity"] == "Afghanistan"]

s_y = s[['Aquaculture production (metric tons)', 'Capture fisheries production (metric tons)']]
s_x = s.index

c_y = c[['Aquaculture production (metric tons)', 'Capture fisheries production (metric tons)']]
c_x = c.index

a_y = a[['Aquaculture production (metric tons)', 'Capture fisheries production (metric tons)']]
a_x = a.index

fig, axs = plt.subplots(1, 3, figsize= (15, 5))
axs[0].plot(s_x, s_y)
axs[1].plot(c_x, c_y)
axs[2].plot(a_x, a_y)

fig.suptitle('Fish Production')

