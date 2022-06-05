"""https://nanti.jisuanke.com/t/T1324"""
from functools import reduce


def xc(n: int) -> int:
    return reduce(lambda x, y: int(x) * int(y), str(n))


n = int(input())
while n > 9:
    print(n, end=' ')
    n = xc(n)
print(n)
