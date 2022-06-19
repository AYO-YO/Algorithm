import functools

import numpy as np


@functools.lru_cache()
def fib(n):
    if n <= 2:
        return 1
    return np.mod(np.add(fib(n - 1), fib(n - 2)), 10)


def calc(n):
    s = str(n)
    if s[0] == '1':
        return int('1' + (len(s) - 3) * '3' + '4')
    elif s[0] == '2':
        return int('2' + (len(s) - 3) * '6' + '7')
    else:
        return 0


m = str(202202011200)
ans = 0
for i in range(len(m)):
    t = int(m[i:])
    ans += calc(t)
print(ans)
