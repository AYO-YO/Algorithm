# https://nanti.jisuanke.com/t/A1597

c = 0
# 蒜头君
for i in range(10, 101):
    # 花椰妹
    for j in range(10, 101):
        s = (int(str(j)[-1]) + int(str(j)[-2])) * 2 == i
        h = (int(str(i)[-1]) + int(str(i)[-2])) * 2 == j
        if s and h:
            c += 1
print(c)
