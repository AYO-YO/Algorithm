s = input()
ops = []
for i in s:
    if i == '(':
        # 入栈
        ops.append('(')
    elif i == ')':
        # 若有匹配的的左括号，则出栈
        if '(' in ops:
            ops.pop()
        else:
            # 否则，为不匹配
            print('NO')
            exit()
# 表达式全部完成以后，看栈内是否还有剩余括号
# 若有，则不匹配
if len(ops) > 0:
    print('NO')
else:
    print('YES')
