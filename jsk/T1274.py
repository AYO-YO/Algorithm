"""
@author: 赵春旭
@version: 1.0.0
@website: https://nanti.jisuanke.com/t/T1274
"""
import math

m, n = map(int, input().split())
print(math.ceil(math.log(m, n + 1)))
