"""https://nanti.jisuanke.com/t/T1341"""

a1, an, q = map(int, input().split())

n = (an - a1) // q + 1

print(n * (a1 + an) // 2)
