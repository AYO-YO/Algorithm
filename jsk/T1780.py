"""https://nanti.jisuanke.com/t/T1780"""

sec = int(input())
h = sec // 3600
m = (sec % 3600) // 60
s = sec % 60
print('%d:%d:%d' % (h, m, s))
