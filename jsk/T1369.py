"""https://nanti.jisuanke.com/t/T1369"""

n = int(input())
ans = 1
jc = 1
sm = 1
while sm < n:
    ans += 1
    jc *= ans
    sm += jc
print('m<=%d' % (ans - 1))
