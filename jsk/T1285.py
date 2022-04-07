"""
@author: 赵春旭
@version: 1.0.0
"""
# https://nanti.jisuanke.com/t/T1285
n = int(input())
m = int(input())
guest = input().split()
while True:
    if guest[m - 1] == '0':
        print(m)
        exit(0)
    m = m % n + 1
