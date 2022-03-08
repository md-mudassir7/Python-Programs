import datetime

a='20 september 2000'
b=datetime.datetime.strptime(a,'%d %B %Y') #d for days,B for months,Y for years
print(b)
now=datetime.datetime.now()
print(now)
years=now.strftime('%Y')
print(years)
years1=now.year #both are same
print(years1)
months=now.strftime('%m')
print(now.month)
days=now.strftime('%d')
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
