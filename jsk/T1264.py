"""
https://nanti.jisuanke.com/t/T1264
"""


def is_run_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


month = {k: v for v, k in enumerate(
    ["", "January", "February", "March", "April", "May", "June", "July", "August", "September",
     "October", "November", "December"])}


def calc_2_29(m, d, y, n_m, n_d, n_y):
    c = 0
    rn = [i for i in range(y, n_y + 1) if is_run_year(i)]
    if len(rn) == 0:
        return c
    for i in rn:
        if i != y and i != n_y:
            c += 1
            continue
        if i == y:
            if month[m] == 1 or (month[m] == 2 and d <= 29):
                c += 1
                continue
        if i == n_y:
            if month[n_m] > 2:
                c += 1
    return c


n = int(input())
ans = []
for i in range(1, n + 1):
    inp = input()
    y = int(inp[-4:])
    m = str(inp.split(',')[0].split(' ')[0])
    d = int(inp.split(',')[0].split(' ')[1])
    inp = input()
    n_y = int(inp[-4:])
    n_m = str(inp.split(',')[0].split(' ')[0])
    n_d = int(inp.split(',')[0].split(' ')[1])
    c = calc_2_29(m, d, y, n_m, n_d, n_y)
    ans.append('Case #%d: %d' % (i, c))

for i in ans:
    print(i)
