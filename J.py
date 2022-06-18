st = list(input())
n = int(input())
for i in range(n):
    ops = input().split()
    for j in range(int(ops[0]) - 1, int(ops[1])):
        if st[j] == ops[2]:
            st[j] = ops[3]
print(''.join(st))
