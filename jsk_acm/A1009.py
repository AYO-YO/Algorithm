def is_run(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def month_add():
    global month, year
    month += 1
    if month > 12:
        month = 1
        year += 1


def day_add():
    global day, month, dc
    day += 1
    dc += 1
    if (day > 31 and month in {1, 3, 5, 7, 8, 10, 12}) or (day > 30 and month in {4, 6, 9, 11}) or (
            day > 29 and month == 2 and is_run(year)) or (day > 28 and month == 2 and not is_run(year)):
        day = 1
        month_add()


bh = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
num_bh = {str(k): bh[k] for k in range(10)}
n = int(input())
for i in range(n):
    start = input()
    end_bh = int(input())
    year = int(start[:4])
    month = int(start[4:6])
    day = int(start[6:])
    dc = 0
    while True:
        y = str(year)
        m = '0' + str(month) if month < 10 else str(month)
        d = '0' + str(day) if day < 10 else str(day)
        mix = y + m + d
        if mix == '30000101':
            print(-1)
            break
        c = 0
        for ch in mix:
            c += num_bh[ch]
        if c == end_bh:
            print(dc)
            break
        day_add()
