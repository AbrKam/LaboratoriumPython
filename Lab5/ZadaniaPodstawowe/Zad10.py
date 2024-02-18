import time as t
import datetime as dt

d = int(input('Podaj dzień: '))
m = int(input('Podaj miesiąc: '))
r = int(input('Podaj rok: '))

data = dt.datetime(r,m,d)

print(f'a) Dzień: {data:%d}')
print(f'')