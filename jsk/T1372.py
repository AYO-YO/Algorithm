"""https://nanti.jisuanke.com/t/T1372"""

n = int(input())
flag = False
for gj in range(0, n + 1):
    for mj in range(0, n + 1 - gj):
        xj = n - gj - mj
        if xj % 3 != 0:
            continue
        if gj * 5 + mj * 3 + xj // 3 == n:
            flag = True
            print(gj, mj, xj)
if not flag:
    print('No Answer.')
