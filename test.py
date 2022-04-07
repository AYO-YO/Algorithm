def essx(n):
    ls = [i for i in range(0, n + 1)]
    ls[0] = ls[1] = 0
    for i in range(2, n + 1):
        if ls[i] != 0:
            for j in range(2 * i, n + 1, i):
                ls[j] = 0
    return list(filter(lambda x: x != 0, ls))


print(len(essx(110000)))
