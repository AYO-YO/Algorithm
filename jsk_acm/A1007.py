code = input()
n = int(input())
lst = []
for i in range(n):
    s = input()
    for j in range(len(s)):
        if code[j] != '*':
            if code[j] != s[j]:
                break
    else:
        lst.append(s)
print(len(lst))
for i in lst:
    print(i)
