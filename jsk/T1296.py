"""
https://nanti.jisuanke.com/t/T1296
"""

from functools import reduce


def xc(n):
    s = str(n)
    x = reduce(lambda x, y: int(x) * int(y), s)
    return x


n = int(input())
for i in range(n):
    inp = int(input())
    print(xc(inp))
