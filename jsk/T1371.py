"""https://nanti.jisuanke.com/t/T1371"""

m, k = map(int, input().split())
t = m
m //= k
sy = m % k
t += m
m += sy
while m > k:
    m //= k
    t += m
    if m % k != 0:
        sy = m % k
        m += sy
print(t)
