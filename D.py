import re


def convertSize(byte):
    size = {'GB': 0, 'MB': 0, 'KB': 0, 'B': 0}
    if byte >= 1073741824:
        size['GB'] = byte // 1073741824
    byte %= 1073741824
    if byte >= 1048576:
        size['MB'] = byte // 1048576
    byte %= 1048576
    if byte >= 1024:
        size['KB'] = byte // 1024
    byte %= 1024
    size['B'] = byte
    return size


def printSize(l):
    size = convertSize(l)
    ans = ''
    # 正常情况下直接遍历字典即可，但我不太确定考试环境的3.8中的字典是否有序。3.9以后肯定是有序的了
    if size['GB'] > 0:
        ans += f'{size["GB"]}GB'
    if size['MB'] > 0:
        ans += f'{size["MB"]}MB'
    if size['KB'] > 0:
        ans += f'{size["KB"]}KB'
    if size['B'] > 0:
        ans += f'{size["B"]}B'
    print(ans)


typs = {'int': 4, 'long': 8, 'String': 1}

n = int(input())
l = 0
for i in range(n):
    op = input()
    os = op.split(maxsplit=1)  # 分割字符串
    typ = os[0]  # 取数据类型
    tmp = os[1]  # 取赋值式
    if '[]' in typ:
        tp = typ.replace('[]', '')
        zkh = re.compile('\[\d+?\]')
        ts = zkh.findall(tmp)
        for j in ts:
            lt = int(j[1:-1]) * typs[tp]
            l += lt
    else:
        if typ == 'String':
            sy = re.compile('”.+?”')
            ts = sy.findall(tmp)
            for j in ts:
                l += len(j) - 2
        else:
            dh = tmp.count(',') + 1
            l += typs[typ] * dh
printSize(l)
