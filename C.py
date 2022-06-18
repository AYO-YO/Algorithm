l = int(input())
for i in range(l):
    n, m = map(int, input().split())
    for x in range(1, m):
        flag = False
        for y in range(x + 1, m + 1):
            if n % x == n % y:
                print('Yes')
                flag = True
                break
        if flag:
            break
        else:
            print('No')
