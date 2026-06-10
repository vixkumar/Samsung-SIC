import pandas as pd

s = pd.Series([1.0, 2.0, 3.0], index = ["a", "b", "c"])
s2 = pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"])

data = {"one":s,"two":s2 }
result = pd.DataFrame(data)
print(result)
