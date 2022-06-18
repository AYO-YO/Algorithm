n, g = map(int, input().split())
nums = list(map(int, input().split()))
c = 0
for i in range(2, n):
    for j in range(n - i + 1):
        tmp = nums[j:j + i]
        t = 0
        for k in tmp:
            if k % g == 0:
                t += 1
        if i - t <= 1:
            c += 1
print(c)
