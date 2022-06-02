"""https://nanti.jisuanke.com/t/T1307"""
import math


def isPrime(n):
    if n <= 3:
        return n >= 2
    if (n + 1) % 6 != 0 and (n - 1) % 6 != 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
for i in range(n):
    m = int(input())
    print('yes' if isPrime(m) else 'no')
