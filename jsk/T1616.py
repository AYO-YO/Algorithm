"""https://nanti.jisuanke.com/t/T1616"""


def elec(w):
    if w <= 150:
        return w * 0.4463
    elif w <= 400:
        return elec(150) + (w - 150) * 0.4663
    else:
        return elec(400) + (w - 400) * 0.5663


n = int(input())
print('%.1f' % elec(n))
