"""https://nanti.jisuanke.com/t/T1460"""


def bike(m: int) -> float:
    s = 27 + 23
    return m / 3 + s


def walk(m: int) -> float:
    return m / 1.2


m = int(input())
b = bike(m)
w = walk(m)
if b < w:
    print('Bike')
elif b > w:
    print('Walk')
else:
    print('All')
