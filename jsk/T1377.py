"""https://nanti.jisuanke.com/t/T1377"""

n = int(input())

ans = []
ans.append(' ' * (n - 1) + '*')
for i in range(2, n + 1):
    ans.append(' ' * (n - i) + '*' + (2 * (i - 1) - 1) * ' ' + '*')

ans.extend(ans[:-1][::-1])
for i in ans:
    print(i)
