import functools
import math
import time


@functools.lru_cache(10 ** 6)
def jc(n):
    if n <= 1:
        return 1
    return n * jc(n - 1)


n = int(input())


def run1():
    start = time.time()
    v = [0, 1]
    for i in range(1, n + 1):
        m = i - 1
        jcc = jc(m)
        l = (m * i) // 2
        v[1] = ((v[0] * i + l * jcc) % 998244353)
        v[0] = v[1]
    print(v[1])
    end = time.time()
    print(end - start)


# run1()
# print()


def run2():
    start = time.time()
    print((sum(range(n)) * math.factorial(n) // 2) % 998244353)
    end = time.time()
    print('run2:', end - start)


run2()
