"""https://nanti.jisuanke.com/t/T1194"""

p, e, i, d = map(int, input().split())
t = 0
ps, es, iss = [], [], []
for j in range(p, 21253, 23):
    ps.append(j)
for j in range(e, 21253, 28):
    es.append(j)
for j in range(i, 21253, 33):
    iss.append(j)
tmp = ps + es + iss
dic = {}
for i in tmp:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
        if dic[i] == 3:
            print(i - d)
            exit()
