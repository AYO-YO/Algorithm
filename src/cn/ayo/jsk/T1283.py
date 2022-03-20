"""
@author: 赵春旭
@version: 1.0.0
"""

print(sum(map(int, input().split())).__format__(',d'))
c = 10000
c.__format__(',d')
format(c, ',d')
f'{c:,d}'
'{:,}'.format(c)
