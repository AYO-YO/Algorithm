def remove_edge():
    global s
    rm = set()
    for i in range(1, len(s) - 1):
        if s[i] == s[i + 1] and s[i - 1] != s[i]:
            rm.add(i - 1)
            rm.add(i)
        if s[i] == s[i - 1] and s[i] != s[i + 1]:
            rm.add(i)
            rm.add(i + 1)
    for i in rm:
        s[i] = ''
    s = list(''.join(s))


s = list(input())
for i in range(2 ** 64):
    ls = s
    remove_edge()
    if ls == s:
        print(''.join(s))
        break
    if len(s) == 0:
        print('EMPTY')
        break
else:
    print(''.join(s))
