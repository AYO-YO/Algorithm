def generate_prime(n):
    ls = [i for i in range(n + 1)]
    ls[0] = 0
    ls[1] = 0
    for i in range(2, n + 1):
        if ls[i] != 0:
            for j in range(2 * i, n + 1, i):
                ls[j] = 0
    return set(filter(lambda x: x != 0, ls))


n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
ma = max(m)
primes = generate_prime(ma)
for i in range(n):
    print('yes' if m[i] in primes else 'no')
