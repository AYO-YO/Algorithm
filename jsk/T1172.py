"""https://nanti.jisuanke.com/t/T1172"""


def get_primes(n):
    ls = [i for i in range(n + 1)]
    ls[0], ls[1] = 0, 0
    for i in range(2, n + 1):
        if ls[i] != 0:
            for j in range(2 * i, n + 1, i):
                ls[j] = 0
    return filter(lambda x: x != 0, ls)


m, n = map(int, input().split())
primes = list(get_primes(n))
ans = []
for i in range(m, n + 1):
    zyz = []
    c = 0
    while True:
        if c == len(primes):
            break
        if i % primes[c] == 0:
            i //= primes[c]
            zyz.append(primes[c])
        else:
            c += 1
    ans.append(max(zyz))
print(','.join(map(str, ans)))
