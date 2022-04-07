"""
@author: 赵春旭
@version: 1.0.0
"""
# https://nanti.jisuanke.com/t/T1287
d1, d2 = map(int, input().split())
if d1 < d2:
    z = d2 - d1
    f = 360 - d2 + d1
else:
    z = 360 - d1 + d2
    f = d1 - d2
f *= -1
if abs(z) <= abs(f):
    print(z)
else:
    print(f)
