"""https://nanti.jisuanke.com/t/T1368"""
import math

m, n = map(int, input().split())
for i in range(m, n + 1):
    print('%4d' % i, '%8.4f' % math.log(i), sep='')
