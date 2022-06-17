"""https://nanti.jisuanke.com/t/T1830"""


def square(n):
    for i in range(n):
        print('*' * n)


def diamond(n):
    sj = []
    for i in range(1, n + 1):
        sj.append(((n - i) * ' ') + ('*' * ((2 * i) - 1)))
    sj.extend(sj[:-1][::-1])
    for i in sj:
        print(i)


m = input()
n = int(input())
if m == 'Z':
    square(n)
else:
    diamond(n)
