"""https://nanti.jisuanke.com/t/T1195"""

n = input()
ls = sorted(map(int, input().split()))
c = 0
# 储存结果
ops = []
for i in range(len(ls) - 1):
    for j in range(i + 1, len(ls)):
        if i != j:
            k = ls[j] + ls[i]
            if k in ls:
                if k not in ops:
                    # 将相加后的所有值计入
                    c += ls.count(k)
                # 避免重复计算
                ops.append(k)
print(c)
