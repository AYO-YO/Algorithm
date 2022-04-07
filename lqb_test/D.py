import math


def gbs(m: int, n: int) -> int:
    return m * n // math.gcd(m, n)


n = 2021
dp = [float('inf') for i in range(2022)]
for i in range(1, 22):
    dp[i] = i
for i in range(22, n + 1):
    for j in range(1, 22):
        dp[i] = min(dp[i], dp[i - j] + gbs(i - j, i))
print(dp)
