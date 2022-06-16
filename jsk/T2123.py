"""https://nanti.jisuanke.com/t/T2123"""

day = []
for i in range(7):
    a, b = map(int, input().split())
    s = a + b
    day.append(s)
m = max(day)
if m < 8:
    print(0)
else:
    print(day.index(m) + 1)
