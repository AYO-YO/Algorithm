"""https://nanti.jisuanke.com/t/T1196"""

n, m = map(int, input().split())
# 坑1：n有一个因子是其本身
for a in range(1, n + 1):
    if n % a == 0:
        # 坑2：m-a不能为0
        if m - a != 0 and n % (m - a) == 0:
            print(a)
            exit()
print(-1)
