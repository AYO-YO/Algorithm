"""https://nanti.jisuanke.com/t/T1385"""
from math import ceil

f = float(input())
if f == 0.5:
    print(3)
else:
    print(ceil(3 + (f - 0.5) / 0.2))
