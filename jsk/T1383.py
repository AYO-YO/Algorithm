"""https://nanti.jisuanke.com/t/T1383"""

s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
m, n = map(int, input().split())
for i in range(m):
    print(s[1:i + 1][::-1] + s[:n - i])
