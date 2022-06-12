"""https://nanti.jisuanke.com/t/T1175"""

import datetime

start = map(int, input().split())
st = datetime.date(*start)
end = map(int, input().split())
ed = datetime.date(*end)
print((ed - st).days)
