"""https://nanti.jisuanke.com/t/T1376"""
import math

high, up, down = map(int, input().split())
d = 1
high -= up
d += math.ceil(high / (up - down))
print(d)
