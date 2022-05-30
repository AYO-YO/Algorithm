"""https://nanti.jisuanke.com/t/T1299"""

city = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'R', 'S', 'T']
n = int(input())
c = 0
for i in range(n):
    s = input()
    if s[0] not in city:
        c += 1
print(c)
