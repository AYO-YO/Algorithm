import math
import random


def getprimes(n):
    ls = [i if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 else 0 for i in range(n + 1)]
    ls[1], ls[2], ls[3], ls[5] = 0, 2, 3, 5
    for i in range(6, n + 1, 6):
        f = i - 1
        if f != 0:
            for j in range(2 * f, n + 1, f):
                ls[j] = 0
            continue
        f = i + 1
        if f != 0:
            for j in range(2 * f, n + 1, f):
                ls[j] = 0
    return filter(lambda x: x != 0, ls)


# 获取10^8以内的质数并计算个数。
l = set(getprimes(10 ** 8))
zs = 0
big_num = []
with open('primes.txt') as f:
    nums = list(map(int, f.read().strip().split()))
for n in nums:
    if n > 10 ** 8:
        big_num.append(n)
        continue
    if n in l:
        zs += 1
print(zs)
print(big_num)


def runFermatPower(a, b, n):
    """
    计算(a**b)%n
    :param a: 底数
    :param b: 指数
    :param n: 取余
    :return: (a**b)%n
    """
    res = 1
    while b > 0:
        if (b & 1) == 1:
            res = (res * a) % n
        b >>= 1
        a = (a * a) % n
    return res


c = 506733
for p in big_num:
    K = 100
    k = 0
    while k < K:  # 这里用while是后续判定随机完成率是否是100%
        b = int(random.random() * (p - 1) + 1)  # 生成一个1~p-1之间的随机整数
        factor = math.gcd(b, p)  # 计算b,p的最大公约数
        r = runFermatPower(b, p, p)  # 计算b^p mod p
        print(f"第{k + 1}次取随机数, 随机数b={b}, {b}和{p}的最大公约数为{factor}, r=({b}^{p})mod p={r}", end=', ')
        if factor > 1:
            print(f"因b={b}与p={p}的最大公约数为{factor}，不为互质数，故p={p}为合数")
            break
        elif r != b:
            print(f"因r={r},({b}^{p}) mod p ={r}!={b}, 故p={p}为合数")
            break
        else:
            print(f"故p={p}可能为素数")
            k += 1
    if k == K:
        print(f"经过{K}次循环验证, p={p}可能为素数, n为素数的概率为{(1 - 1 / (2 ** k)) * 100}%")
        c += 1
print(f'最终结果{c}')
