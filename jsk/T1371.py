"""https://nanti.jisuanke.com/t/T1371"""

m, k = map(int, input().split())
d = 0
while m > 0:
    m -= 1
    d += 1
    if d % k == 0:
        m += 1
print(d)
