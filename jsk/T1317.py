"""https://nanti.jisuanke.com/t/T1317"""

from functools import lru_cache


@lru_cache()
def pell(n):
    if n <= 2:
        return n
    a, b, c = 0, 1, 2
    for i in range(3, n + 1):
        a = (2 * c + b) % 32767
        b, c = c, a
    return a


n = int(input())
for i in range(n):
    m = int(input())
    print(pell(m) % 32767)
