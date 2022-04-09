import copy


def isfdj(lst):
    return lst == sorted(lst)


n, k = map(int, input().split())
ls = list(map(int, input().split()))
l = []
for i in range(1, n - k):
    tmp = copy.deepcopy(ls)
    t = ls[i - 1]
    for j in range(i, i + k):
        tmp[j] = t
    ll = 0  # 当前子串长度
    low = 0
    high = 1
    while high < n:
        if isfdj(tmp[low:high]):
            ll += 1
        else:
            l.append(ll)
            ll = 0
            low = high
        high += 1
    l.append(ll)
print(max(l))
