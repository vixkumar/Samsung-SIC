"""
import pandas as pd
import matplotlib.pyplot as plt

url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=GS10"
df = pd.read_csv(url)

plt.plot(df["GS10"])
plt.show()
"""

"""
import wbdata
import pandas as pd

indicators = wbdata.get_indicators()
df = pd.DataFrame(indicators)
print(df.iloc[:5, :2])

life_exp = df[df["name"].str.contains("life expectancy", case=False, na=False)]
print(life_exp.iloc[:5, :2])
"""

"""
import wbdata
import pandas as pd

data = wbdata.get_data(
    indicator="SP.DYN.LE00.IN",
    country="all"
)

df = pd.json_normalize(data)

df["date"] = df["date"].astype(int)

df = df[(df["date"] >= 1980) & (df["date"] <= 1999)]

df["country"] = df["country.value"]

pivot_result = df.pivot_table(
    index="country",
    columns="date",
    values="value"
)


print(pivot_result)
"""

"""
import pandas as pd
rank = pd.read_json(r"C:\Users\Lenovo\Desktop\samsung sic\Dataset\universities_ranking.json", orient = "records")

index_position = rank.iloc[1:10]

a = index_position.title
b = index_position.title

print(a)
print("\n")
print(b)

c = index_position[["title", "location", "students staff ratio", "gender ratio"]]
print("\n")
print(c)








