"""https://nanti.jisuanke.com/t/T1298"""

n = input()
ls = input().split()
c = 1
m = c
for i in range(1, len(ls)):
    if ls[i] == ls[i - 1]:
        c += 1
    else:
        m = max(m, c)
        c = 1
m = max(m, c)
c = 1
print(m)
