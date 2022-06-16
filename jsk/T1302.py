"""https://nanti.jisuanke.com/t/T1302"""


def w_p(w):
    if w <= 10:
        return w * 0.8
    elif w <= 20:
        return 8 + (w - 10) * 0.75
    else:
        return 15.5 + (w - 20) * 0.7


w = float(input())
if w > 30:
    print('Fail')
else:
    print('%.2f' % (w_p(w) + 0.2))
