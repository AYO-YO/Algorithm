"""https://nanti.jisuanke.com/t/T1399"""

from math import gcd


def my_gcd(m: int, n: int) -> int:
    return gcd(m, n)


def zzxc(m: int, n: int) -> int:
    r = m % n
    while r != 0:
        m, n = n, r
        r = m % n
    return n


l = int(input())
for i in range(l):
    m, n = map(int, input().split())
    print(gcd(m, n))
