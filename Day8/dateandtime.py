from datetime import datetime, timedelta
    
d = datetime(2000, 5, 3)
delta = timedelta(days=30)
print(d + delta)

now = datetime.now()
print(now)
replace_time=now.replace(month=12, day=30)
print(replace_time)
