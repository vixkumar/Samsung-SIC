"""
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])


plt.show()
"""

"""
import matplotlib.pyplot as plt
x = range(100)
y = [value **2 for value in x]

plt.plot(x, y, linewidth = 5.0, color = "red")

plt.title("Hello bworld")
plt.ylabel("Y-some numbers: ")
plt.xlabel("X-some numbers: ")

plt.show()
"""

"""
import matplotlib.pyplot as plt
days_in_year = [88, 225, 365, 687, 4333, 30687, 60190, 90553]
plt.bar(range(len(days_in_year)), days_in_year)
plt.show()
"""

import pandas as pd
import matplotlib.pyplot as plt

pop_2020 = {"Germany" : 10000, "Switzer" : 5000, "Bolivia": 500, "Italy" : 800, "Slovenia": 4000}
pop_2021 = {"Germany" : 15000, "Switzer" : 5050, "Bolivia": 50089, "Italy" : 8690, "Slovenia": 423}

area = {"Germany" : 15000, "Switzer" : 50500, "Bolivia": 500890, "Italy" : 86900, "Slovenia": 42300}

pop = pd.Series(pop_2020)
ar = pd.Series(area)
pop_dens = (pop/ar) * 100

s1_data = pd.Series(pop_2020)
s2_data = pd.Series(pop_2021)

diff = s1_data - s2_data
print(diff)
x = diff.index
y = diff.values

plt.figure(figsize=(13, 16))
plt.barh(x, y)

plt.title("Population differences")
plt.xticks(rotation=90, size=10)
plt.xlabel("Population")
plt.ylabel("Country")
plt.show()

x = pop_dens.index
y = pop_dens.values
plt.figure(figsize=(13, 16))
plt.barh(x, y)
plt.title ("Population density: ")
plt.xticks(rotation = 90, size=10)
plt.xlabel("density")
plt.ylabel("Country")

plt.show()

print("Density avg is: ",pop_dens.mean())
print("Avg density is: ", pop_dens.max())






