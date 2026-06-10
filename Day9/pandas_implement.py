import pandas as pd
s = pd.Series([1.0, 2.0, 3.0], index =["a", "b", "c"])
s1 = pd.Series([10.0, 11.0, 12.0], index =["a", "b", "c"])

dic_data = {"One" : s, "Two" : s1}

type(dic_data)
pd.DataFrame(dic_data)

print(pd.DataFrame.from_dict(dic_data, orient="columns"))


