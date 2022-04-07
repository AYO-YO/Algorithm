one = 2021
res = 1
while True:
    s = str(res).count('1')
    if one >= s:
        one -= s
        res += 1
    else:
        print(res - 1)
        break
