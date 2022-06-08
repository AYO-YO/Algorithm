"""https://nanti.jisuanke.com/t/T1380"""

t = int(input())

for i in range(t):
    x, n = input().split()
    x = x.split('.')[1]
    try:
        print(x[int(n) - 1])
    except IndexError:
        print(0)
