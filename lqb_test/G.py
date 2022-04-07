"""
1
1 1
1 2 1
1 3 3 1
"""


def yhsj(line):
    yield [1]
    yield [1, 1]
    yh = [[0 for _ in range(line)] for _ in range(line)]
    yh[0][0] = 1
    yh[1][0] = 1
    yh[1][1] = 1
    for i in range(2, line):
        yh[i][0] = 1
        for j in range(1, line):
            yh[i][j] = yh[i - 1][j - 1] + yh[i - 1][j]
        yield yh[i][:i + 1]


n = int(input())
c = 1
for i in yhsj(34):
    if n in i:
        print(c + i.index(n))
        break
    else:
        c += len(i)

# 1000000000
