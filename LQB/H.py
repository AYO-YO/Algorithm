n, m = map(int, input().split())
add = []
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    add.append([a, b])
while m > 0:
    add = sorted(add, key=lambda x: x[0], reverse=True)
    ans += add[0][0]
    add[0][0] -= add[0][1]
    m -= 1
print(ans)
