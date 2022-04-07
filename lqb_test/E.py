def ishz(m, n):
    if n > m: m, n = n, m
    for i in range(2, n):
        if n % i == 0 and m % i == 0: return False
    return True


print(ishz(5, 9))
