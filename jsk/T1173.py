"""https://nanti.jisuanke.com/t/T1173"""


def get_primes(n):
    ls = [i if i % 2 != 0 else 0 for i in range(n + 1)]
    ls[1], ls[2] = 0, 2

    for i in range(3, n + 1, 2):
        if ls[i] != 0:
            for j in range(2 * i, n + 1, i):
                ls[j] = 0
    return filter(lambda x: x != 0, ls)


n = int(input())
ps = list(get_primes(n))
if n == [ps[-1]]:
    print(n)
    exit()
ans = {}
c = 0
while True:
    if n == 1:
        break
    if n % ps[c] == 0:
        n //= ps[c]
        if c in ans:
            ans[c] += 1
        else:
            ans[c] = 1
        c = 0
    else:
        c += 1
nums = []
for i in ans:
    if ans[i] > 1:
        nums.append('%d^%d' % (ps[i], ans[i]))
    else:
        nums.append('%d' % ps[i])
print('*'.join(nums))
