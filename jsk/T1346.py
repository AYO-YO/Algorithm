"""https://nanti.jisuanke.com/t/T1346"""
import math

x1, y1, x2, y2 = map(int, input().split())
distance = math.sqrt((math.pow(x1 - x2, 2)) + math.pow(y1 - y2, 2))
print('%.2f' % distance)
