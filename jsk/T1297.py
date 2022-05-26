"""https://nanti.jisuanke.com/t/T1297"""


def calc(m, n):
    if m % 2 == 1:
        m += 1
    if n % 2 == 1:
        n -= 1
    s = (n - m) // 2 + 1
    return s * (n + m) // 2


m, n = map(int, input().split())
print(calc(m, n))
