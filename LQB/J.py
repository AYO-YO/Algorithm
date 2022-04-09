n, k = map(int, input().split())
lst = list(map(int, input().split()))
red = lambda x: x - 1
i = 0
c = 0
while True:
    r = i + k
    if r <= n:
        if 0 not in lst[i:r]:
            lst[i: r] = map(red, lst[i:r])
            c += 1
        else:
            i = lst[i: r].index(0) + i + 1
    else:
        break
c += sum(lst)
print(c)
