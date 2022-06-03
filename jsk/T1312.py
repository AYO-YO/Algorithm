"""https://nanti.jisuanke.com/t/T1312"""

s1 = input()
s2 = input()
l1 = len(s1)
l2 = len(s2)
lm = min(l1, l2)
for i in range(lm):
    if s1[i] == s2[i]:
        print(i + 1, end=' ')
