"""
@author: 赵春旭
@version: 1.0.0
@website: https://nanti.jisuanke.com/t/T1279
"""
a = input()
b = input()
c = input()
l = len(a)
ct = 0
for i in range(l):
    if a[i] != b[i] and a[i] != c[i] and b[i] != c[i]:
        ct += 2
    if a[i] == b[i] == c[i]:
        continue
    if a[i] == b[i] or b[i] == c[i] or a[i] == c[i]:
        ct += 1
print(ct)
