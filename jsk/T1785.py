"""https://nanti.jisuanke.com/t/T1785"""

n = input()
ls = input().split()
s = []
for i in ls:
    if i not in s:
        s.append(i)
print(' '.join(s[::-1]))
