import math


# 已知两边及夹角，计算第三边
def dsb(a, b, deg=60):
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2) - 2 * a * b * math.cos(deg / 180 * math.pi))


# 已知两边夹角及斜边，计算两边
def lb(c, deg=120):
    pass


a = dsb(5, 3)
b = dsb(3, 2)

