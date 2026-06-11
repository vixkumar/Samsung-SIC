
import pandas as pd
import datetime
from datetime import date, datetime, time, timezone

wti = pd.read_csv(r"C:\Users\Lenovo\Desktop\samsung sic\Dataset\DCOILWTICO.csv")
print(wti.head())
print(wti.columns)


import pandas as pd
pd.date_range(start = "2021-01-01", end = None, periods=5, freq = "M", tz = None)






