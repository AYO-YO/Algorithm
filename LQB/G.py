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
    print('run1:', end - start)


# run1()


# print()


def run2():
    start = time.time()
    print((sum(range(n)) * math.factorial(n) // 2) % 998244353)
    end = time.time()
    print('run2:', end - start)


# run2()


def run3():
    start = time.time()
    m = 998244353
    fact = 1
    ans = [0]
    for i in range(2, n + 3):
        fact *= i - 1
        fact %= m
        ans.append((ans[-1] * i + fact * (i - 1) * i // 2) % m)
    print(ans[n - 1])
    end = time.time()
    print('run3:', end - start)


run3()


def run4():
    start = time.time()
    v = [0, 1]
    fact = 1
    for i in range(2, n + 1):
        fact *= i - 1
        fact %= 998244353
        m = i - 1
        l = (m * i) // 2
        v[1] = ((v[0] * i + l * fact) % 998244353)
        v[0] = v[1]
    print(v[1])
    end = time.time()
    print('run4:', end - start)


run4()
