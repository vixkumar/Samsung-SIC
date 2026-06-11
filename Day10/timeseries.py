import datetime
from datetime import date, datetime, time, timezone
import pandas as pd

"""
print(datetime(2023, 7, 7))
d = date(2021, 7, 7)
t = time(13, 26, 10)
print(datetime.combine(d,t))
"""

my_birth = datetime(1973, 7, 7)
today = datetime.today()
tomorrow = today + pd.Timedelta(days = 1)

print(tomorrow - my_birth)




