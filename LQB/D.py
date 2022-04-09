def swh(n):
    n = map(int, list(str(n)))
    return sum(n)


def lst(end, start=1):
    ls = [i for i in range(start, end + 1)]
    sw = {i: swh(i) for i in ls}
    s = sorted(sw.items(), key=lambda x: x[1])
    return s


end = int(input())
i = int(input()) - 1
print(lst(end)[i][0])
