# 第十三届蓝桥杯省赛 Python Ｂ组

## 试题A：排列字母

本题总分：5 分

【问题描述】

小蓝要把一个字符串中的字母按其在字母表中的顺序排列。 例如，`LANQIAO` 排列后为 `AAILNOQ`。 又如，`GOODGOODSTUDYDAYDAYUP` 排列后为 `AADDDDDGGOOOOPSTUUYYY` 。
请问对于以下字符串，排列之后字符串是什么？ `WHERETHEREISAWILLTHEREISAWAY`

【答案提交】

这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一 个由大写字母组成的字符串，在提交答案时只填写这个字符串，填写多余的内 容将无法得分。

---

【思路分析】

这个没啥难的，Python直接转为`list`再sorted即可，一行搞定

【完整代码】

```python
s = 'WHERETHEREISAWILLTHEREISAWAY'
print(''.join(sorted(list(s))))
```

【参考答案】

```
AAAEEEEEEHHHIIILLRRRSSTTWWWY
```

## 试题B：寻找整数

本题总分：5 分

【问题描述】

有一个不超过 $10^{17}$ 的正整数 $n$，知道这个数除以 $2$ 至 $49$ 后的余数如下表 所示，求这个正整数最小是多少。

|    a | n mod a |    a | n mod a |    a | n mod a |    a | n mod a |
| ---: | ------- | ---: | ------- | ---: | ------- | ---: | ------- |
|    2 | 1       |   14 | 11      |   26 | 23      |   38 | 37      |
|    3 | 2       |   15 | 14      |   27 | 20      |   39 | 23      |
|    4 | 1       |   16 | 9       |   28 | 25      |   40 | 9       |
|    5 | 4       |   17 | 0       |   29 | 16      |   41 | 1       |
|    6 | 5       |   18 | 11      |   30 | 29      |   42 | 11      |
|    7 | 4       |   19 | 18      |   31 | 27      |   43 | 11      |
|    8 | 1       |   20 | 9       |   32 | 25      |   44 | 33      |
|    9 | 2       |   21 | 11      |   33 | 11      |   45 | 29      |
|   10 | 9       |   22 | 11      |   34 | 17      |   46 | 15      |
|   11 | 0       |   23 | 15      |   35 | 4       |   47 | 5       |
|   12 | 5       |   24 | 17      |   36 | 29      |   48 | 41      |
|   13 | 10      |   25 | 9       |   37 | 22      |   49 | 46      |

【答案提交】

这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。

---

【思路分析】

这个题思路很直，直接爆。但爆也有爆的技巧，可以先算一部分，然后得到一组符合条件的，作为步长，再筛选一轮，这样步长比较大的时候，列表中的数量较少，爆起来速度不至于太慢。

至于为什么不直接写大循环，因为我每次生成的范围和结果不一样，如果筛选后剩余的列表元素过多，需要将取余的范围加大，需要实时动态调整。

① 先给一个初值：

```python
ls = [i for i in range(1, 10 ** 4)]
```

② 再进行一次筛选：

```python
for i in range(2, 10):
    ls = list(filter(lambda x: x % i == mp[i], ls))
```

③ 然后进行一次输出：

```python
[1649, 4169, 6689, 9209]
```

④ 然后以`ls[0]`作为初值，以`ls[1]-ls[0]`作为步长，再生成一组

```python
ls = [i for i in range(ls[0], 10 ** 9, ls[1] - ls[0])]
```

⑤ 再筛选，这个筛选的范围不是固定的，10\~20，\~15都可以，但要根据上边的`ls`的`end`值决定，如果太小，则筛选范围相应小一些，反之则大一些：

```python
for i in range(10, 20):
    ls = list(filter(lambda x: x % i == mp[i], ls))
```

⑥ 输出：

```python
[88209209, 321001769, 553794329, 786586889]
```

重复④⑤⑥执行

```python
...
```

直到即得出最终结果

```python
ls = [i for i in range(ls[0], 10 ** 17, ls[1] - ls[0])]
for i in range(30, 50):
    ls = list(filter(lambda x: x % i == mp[i], ls))
print(ls)
```

【完整代码】

```python
mp = {2: 1, 3: 2, 4: 1, 5: 4, 6: 5, 7: 4, 8: 1, 9: 2, 10: 9, 11: 0, 12: 5, 13: 10, 14: 11, 15: 14, 16: 9, 17: 0, 18: 11,
      19: 18, 20: 9, 21: 11, 22: 11, 23: 15, 24: 17, 25: 9, 26: 23, 27: 20, 28: 25, 29: 16, 30: 29, 31: 27, 32: 25,
      33: 11, 34: 17, 35: 4, 36: 29, 37: 22, 38: 37, 39: 23, 40: 9, 41: 1, 42: 11, 43: 11, 44: 33, 45: 29, 46: 15,
      47: 5, 48: 41, 49: 46}

ls = [i for i in range(1, 10 ** 4)]
for i in range(2, 10):
    ls = list(filter(lambda x: x % i == mp[i], ls))
print(ls)
ls = [i for i in range(ls[0], 10 ** 9, ls[1] - ls[0])]
for i in range(10, 20):
    ls = list(filter(lambda x: x % i == mp[i], ls))
print(ls)
ls = [i for i in range(ls[0], 10 ** 13, ls[1] - ls[0])]
for i in range(20, 30):
    ls = list(filter(lambda x: x % i == mp[i], ls))
print(ls)
ls = [i for i in range(ls[0], 10 ** 17, ls[1] - ls[0])]
for i in range(30, 50):
    ls = list(filter(lambda x: x % i == mp[i], ls))
print(ls)
```

【参考答案】

```python
2022040920220409
```

## 试题C: 纸张尺寸

时间限制: 1.0s 内存限制: 512.0MB 本题总分：10 分

【问题描述】

在 ISO 国际标准中定义了 A0 纸张的大小为 1189mm × 841mm，将 A0 纸沿长边对折后为 A1 纸，大小为 841mm × 594mm，在对折的过程中长度直接取下整（实际裁剪时可能有损耗）。将 A1 纸沿长边对折后为 A2
纸，依此类推。

输入纸张的名称，请输出纸张的大小。

【输入格式】

输入一行包含一个字符串表示纸张的名称，该名称一定是 A0、A1、A2、 A3、A4、A5、A6、A7、A8、A9 之一。

【输出格式】

输出两行，每行包含一个整数，依次表示长边和短边的长度。

【样例输入 **1**】

A0

【样例输出 **1**】

1189

841

【样例输入 **2**】

A1

【样例输出 **2**】

841

594

---

【思路分析】

这个题没啥难度，找到长边然后除以2就行。

注意一个坑：不是长宽同时除以2，而是长边。折叠之后长边会变成短边，所以要进行交换

【完整代码】

```python
paper = input()
width = 1189
height = 841
count = int(paper[1])
while count > 0:
    if width < height:
        width, height = height, width
    width //= 2
    count -= 1
if width < height:
    width, height = height, width
print(width)
print(height)
```

## 试题D：数位排序

时间限制: 1.0s 内存限制: 512.0MB 本题总分：10 分

【问题描述】

小蓝对一个数的数位之和很感兴趣，今天他要按照数位之和给数排序。当两个数各个数位之和不同时，将数位和较小的排在前面，当数位之和相等时，将数值小的排在前面。

例如，2022 排在 409 前面，因为 2022 的数位之和是 6，小于 409 的数位之和 13。

又如，6 排在 2022 前面，因为它们的数位之和相同，而 6 小于 2022。

给定正整数 n，m，请问对 1 到 n 采用这种方法排序时，排在第 m 个的元素是多少？

【输入格式】

输入第一行包含一个正整数 n。第二行包含一个正整数 m。

【输出格式】

输出一行包含一个整数，表示答案。

【样例输入】

```
13
5
```

【样例输出】

```
3
```

【样例说明】

1 到 13 的排序为：1, 10, 2, 11, 3, 12, 4, 13, 5, 6, 7, 8, 9。第 5 个数为 3。

【评测用例规模与约定】

对于 30% 的评测用例，1 ≤ *m* ≤ *n* ≤ 300。

对于 50% 的评测用例，1 ≤ *m* ≤ *n* ≤ 1000。

对于所有评测用例，1 ≤ *m* ≤ *n* ≤ 106。

---

【思路分析】

这个题也不难，首先是计算数位和，直接拆成列表，然后逐个取`int()`，再求列表的和即可

```python
def swh(n):
    n = map(int, list(str(n)))
    return sum(n)
```

然后用字典生成式生成字典然后排序后按要求取值即可。

【完整代码】

```python
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
```

## 试题E：蜂巢

时间限制: 1.0s 内存限制: 512.0MB 本题总分：15 分

【问题描述】

蜂巢由大量的六边形拼接而成，定义蜂巢中的方向为：0 表示正西方向，1表示西偏北60◦，2 表示东偏北60◦，3 表示正东，4 表示东偏南60◦，5 表示西偏南60。

对于给定的一点*O*，我们以*O* 为原点定义坐标系，如果一个点*A* 由*O* 点先向*d* 方向走*p* 步再向(*d* + 2) mod 6 方向（*d* 的顺时针120◦ 方向）走*q* 步到达，则这个点的坐标定义为(*d*; *
p*; *q*)。在蜂窝中，一个点的坐标可能有多种。下图给出了点*B*(0; 5; 3) 和点*C*(2; 3; 2) 的示意。

![image-20220409181717855](https://img.2fanbaby.cn/img/202204091817026.png)

给定点 (*d*1, *p*1, *q*1) 和点 (*d*2, *p*2, *q*2)，请问他们之间最少走多少步可以到达？

【输入格式】

输入一行包含 6 个整数 *d*1, *p*1, *q*1, *d*2, *p*2, *q*2 表示两个点的坐标，相邻两个整数之间使用一个空格分隔。

【输出格式】

输出一行包含一个整数表示两点之间最少走多少步可以到达。

【样例输入】

0 5 3 2 3 2

【样例输出】

7

【评测用例规模与约定】

对于 25% 的评测用例，*p*1, *p*2 ≤ 103 ；

对于 50% 的评测用例，*p*1, *p*2 ≤ 105 ；

对于 75% 的评测用例，*p*1, *p*2 ≤ 107 ；

对于所有评测用例，0 ≤ *d*1, *d*2 ≤ 5，0 ≤ *q*1 < *p*1 ≤ 109，0 ≤ *q*2 < *p*2 ≤ 109 。

---

【思路分析】

这个题，我不会，但我觉得，将路径看成三角形，已知角度，已知两边和，求出第三边的长，然后得到两点的斜边长，然后再根据夹角算两边的长度。

但是我也不知道对不对，说来惭愧，鄙人三角形学的非常辣鸡，不知道怎么求非直角三角形的第三边长，所以只有这么个想法，并没有实现。。。

如果思路不对，还请大佬赐教，如果思路对的话，麻烦大佬实现:joy:

## 试题F：消除游戏

时间限制: 3.0s 内存限制: 512.0MB 本题总分：15 分

【问题描述】

在一个字符串 S 中，如果 S i = S i−₁ 且 S i * S i₊₁ ，则称 S i 和 S i₊₁ 为边缘字符。如果 S i * S i−₁ 且 S i = S i₊₁，则 S

i−₁ 和 S i 也称为边缘字符。其它的字符都不是边缘字符。

对于一个给定的串 S ，一次操作可以一次性删除该串中的所有边缘字符

（操作后可能产生新的边缘字符）。

请问经过 2⁶⁴ 次操作后，字符串 S 变成了怎样的字符串，如果结果为空则输出 EMPTY。

【输入格式】

输入一行包含一个字符串 S 。

【输出格式】

输出一行包含一个字符串表示答案，如果结果为空则输出 EMPTY。

【样例输入 1】

edda

【样例输出 1】

EMPTY

【样例输入 2】

sdfhhhhcvhhxcxnnnnshh

【样例输出 2】

s

【评测用例规模与约定】

对于 25% 的评测用例，|S | ≤ 10³ ，其中 |S | 表示 S 的长度；对于 50% 的评测用例，|S | ≤ 10⁴ ；

对于 75% 的评测用例，|S | ≤ 10⁵ ；

对于所有评测用例，|S | ≤ 10⁶，S 中仅含小写字母。

---

【思路分析】

这个题没有好的思路，只能暴力模拟了:joy:

需要留意几个地方：

- 不能直接删除项目中边缘字符，如果直接删除会导致越界
- 也不能直接将待删除的边缘字符替换成其他字符，因为这样会导致判断出问题，比如`xxv`中`xv`待删除，将其替换为0，变为`x00`，则执行下一步的时候就会将`x0`作为边缘字符删掉`x`。
- 其实循环不了$2^{64}$次，如果化到最简，则可以比较处理前和处理后的结果，如果相同，则已经是最简了，直接跳出循环即可

两个解决办法，一个是先判断逆向字符，比如`xxv`，再判断正向字符：`xvv`。

另一个是使用一个集合将待删除的下标保存，然后循环结束后统一删除。

【完整代码】

```python
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
```

## 试题G：全排列的价值

时间限制: 1.0s 内存限制: 512.0MB 本题总分：20 分

【问题描述】

对于一个排列 $A = (a_1, a_2,..., a_n)$，定义价值 $c_i$ 为 $a_1$ 至 $a_{i-1}$ 中小于 $a_i$ 的数的个数，即 $b_i = |\{a_j| j < i, a_j < a_i\}|$。定义
$A$ 的价值为$\sum^n_{i=1}c_i$。

给定 n，求 1 至 n 的全排列中所有排列的价值之和。

【输入格式】

输入一行包含一个整数 n 。

【输出格式】

输出一行包含一个整数表示答案，由于所有排列的价值之和可能很大，请输出这个数除以 $998244353$ 的余数。

【样例输入 1】

3

【样例输出 1】

9

【样例输入 2】

2022

【样例输出 2】

593300958

【样例说明】

1 至 3 构成的所有排列的价值如下:

(1, 2, 3) : 0 + 1 + 2 = 3 ；

(1, 3, 2) : 0 + 1 + 1 = 2 ；

(2, 1, 3) : 0 + 0 + 2 = 2 ；

(2, 3, 1) : 0 + 1 + 0 = 1 ；

(3, 1, 2) : 0 + 0 + 1 = 1 ；

(3, 2, 1) : 0 + 0 + 0 = 0 ；

故总和为 3 + 2 + 2 + 1 + 1 = 9。

【评测用例规模与约定】

对于 40% 的评测用例，n ≤ 20 ；

对于 70% 的评测用例，n ≤ 5000 ；对于所有评测用例，2 ≤ n ≤ 10⁶ 。

---

【思路分析】

这道题比较有意思，暴力肯定不行。

首先，试想一下，2和1的价值，只有在[1, 2]的情况下才有价值为1.

在(1, 2, 3)的组合里边，2在1前边有三种情况，分别是：

```python
(1, 2, 3)
(1, 3, 2)
(3, 1, 2)
```

这三种的情况，也就是2产生的值为`3*1`，然后再考虑`3`的位置和价值，3是当前组合里边最大的数，当3置于最后边，可以产生的价值为：`2*2`，当3的价值置于中间，所产生的价值为`1*2`。

所以`(1, 2, 3)`全排列的值为：$3*1+2*2+1*2$。数据量太小，还看不出什么规律。我们再做一下`(1, 2, 3, 4)`的排列。

首先`(1, 2, 3)`的全排列为`9`，然后有4个位置可以插入4，所以`(1, 2, 3, 4)`的全排列中，`(1, 2, 3)`产生的价值为：$9*4=36$，当4置于末尾时，`(1, 2, 3)`
每一种排列方式都能给4带来3的价值，所以即当4置于末尾时即为$3*A_3^3$，当4置于第3位，则`(1, 2, 3)`每一种排列，都能给4带来2的价值，即为$3*A_2^2$。然后是第二位…第一位…

由此可以推得，某一位数的全排列值，等于他本身乘以前一个数的全排列值，然后再加上$\sum_{i=1}^{n-1}iA_{n-1}^{n-1}$，$A_n^n$即$n!$，即可得公式

$$c_n=n*(n-1)+\sum_{i=1}^{n-1}i*(n-1)!$$

$\sum_{i=1}^{n-1}i*(n-1)!$可以进一步化简为$\frac{(n-1)*(1+n-1)}{2}*(n-1)!$，即$\frac{(n-1)*n}{2}*(n-1)!$

故可以得出递归函数

```python
@functools.lru_cache(10 ** 6)
def get_value(n):
    m = n - 1
    jcc = jc(m) # jc()，自定义函数，求阶乘
    v = m * n // 2
    return (n * get_value(n - 1) + jcc * v) % 998244353
```

- 这个递归很好理解，但是实际跑的时候数据稍大就会栈溢出，所以得给他改成循环。
- 这里阶乘要用自定义函数加缓存，因为每一个数得价值，都会求一次阶乘，反复求的话自定义的函数加缓存在效率上相比于`math.factorial()`提升会非常明显，例如样例的`2022`，缓存求递归仅需要`0.01s`
  ，而用`math.factorial()`则需要`0.1s`
- 跑了一下，5000没啥问题，能过70%的样例，但是跑不了$10^6$，估计把阶乘的求法再优化优化能跑通

【完整代码】

```python
import functools
import math


@functools.lru_cache(10 ** 6)
def jc(n):
    if n <= 1:
        return 1
    return n * jc(n - 1)


n = int(input())
v = [0, 1]
for i in range(1, n + 1):
    m = i - 1
    jcc = jc(m)
    l = (m * i) // 2
    v[1] = ((v[0] * i + l * jcc) % 998244353)
    v[0] = v[1]
print(v[1])
```

