from datetime import datetime, timezone, timedelta

print(1//2)
print(3//2)
print(5//2)

dt1 = datetime.now().replace(tzinfo=timezone(timedelta(hours=-2)))
dt2 = datetime.now().replace(tzinfo=timezone(timedelta(hours=-1)))

print(dt1.timestamp())
print(dt2.timestamp())

date_str = "19 Mar 2018"
dt = datetime.strptime(date_str,"%d %b %Y")
print(dt)
dt_str = dt.strftime("%Y-%m-%d")
print(dt_str)