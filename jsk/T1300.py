"""https://nanti.jisuanke.com/t/T1300"""

s1 = input()
s2 = input()
ans = 0
if len(s1) != len(s2):
    ans = 1
elif s1 == s2:
    ans = 2
elif s1.upper() == s2.upper():
    ans = 3
else:
    ans = 4
print(ans)
