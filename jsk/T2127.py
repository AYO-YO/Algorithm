"""https://nanti.jisuanke.com/t/T2127"""

ls = list(map(int, input().split()))
h = int(input()) + 30
print(len(list(filter(lambda x: x <= h, ls))))
