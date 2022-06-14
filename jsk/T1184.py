"""https://nanti.jisuanke.com/t/T1184"""


def get_y(x):
    return 2 * x + 1, 3 * x + 1


k, x = map(int, input().split(','))


def dfs(k):
    global x
    if k == x:
        print('YES')
        exit()
    if k > x:
        return
    datas = get_y(k)
    for i in datas:
        dfs(i)


dfs(k)
print('NO')
