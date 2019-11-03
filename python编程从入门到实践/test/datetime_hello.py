# 获取当前日期和时间

from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)

print(type(now))

# 获取指定日期和时间
dt = datetime(2016, 12, 11, 15, 30, 11)
print(dt)
# datetime转换为timestamp
print(dt.timestamp())
# timestamp转换为datetime
t = 1429417200
print(datetime.fromtimestamp(t))
# timestamp也可以直接被转换到UTC标准时区的时间：
print(datetime.utcfromtimestamp(t))

# str转换为datetime
# 字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式
cday = datetime.strptime("2017-8-11 18:20:55", "%Y-%m-%d %H:%M:%S")
print(cday)

# datetime转换为str
print(now.strftime("%a,%b %d %H:%M"))

# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime.需要导入timedelta这个类
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
new_dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00
print(new_dt)

#时区转换   我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
utc_dt = datetime.now().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokoyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokoyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokoyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokoyo_dt2)