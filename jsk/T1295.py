"""
https://nanti.jisuanke.com/t/T1295
"""

while True:
    n = int(input())
    if n == 0:
        break
    print(' '.join([str(i) for i in range(n) if i % 7 != 0]))
