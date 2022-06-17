"""https://nanti.jisuanke.com/t/T1186"""

import datetime

n = int(input())
for i in range(n):
    y, m1, m2 = map(int, input().split())
    st = datetime.date(y, m1, 1)
    ed = datetime.date(y, m2, 1)
    print("YES" if abs((ed - st).days) % 7 == 0 else "NO")
