import datetime

today = datetime.date.today()
print(today)

diff_days = datetime.timedelta(days=1)
print(diff_days)

print(diff_days + today)
print(today - diff_days)