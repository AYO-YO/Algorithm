s = input()
ops = []
for i in s:
    if i == '(':
        ops.append('(')
    elif i == ')':
        if '(' in ops:
            ops.pop()
        else:
            print('NO')
            exit()
if len(ops) > 0:
    print('NO')
else:
    print('YES')
