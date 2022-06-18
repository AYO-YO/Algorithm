import itertools
import re

ore = re.compile('owo')


def getNums(owo):
    owo = owo.replace('o', 'oo')
    return len(ore.findall(owo))


n = int(input())
sts = []
for i in range(n):
    sts.append(input())
    rdm_lst = itertools.permutations(sts)
    m = 0
    for j in rdm_lst:
        ls = getNums(''.join(j))
        if ls > m:
            m = ls
    print(m)
