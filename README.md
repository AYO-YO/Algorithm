# 蓝桥杯第十三届国赛PythonB组题解

【写在前边】

这次的题还是比较难的，只做出来7道，交上去6道，还有一半是暴力做的😂。只求国三了😭

开局两道填空题用了快两个小时，直接搞崩了心态。。淦！

本题解仅代表个人观点及思路，不代表标准答案。欢迎各位巨佬指导交流😊。

## 试题A：斐波那契与7（5分）

【问题描述】
斐波那契数列的递推公式为：$F_n = F_{n-1} + F_{n-2}$，其中 $F_1 = F_2 = 1$。
请问，斐波那契数列的第 $1 $至$ 202202011200$ 项（含）中，有多少项的个位是 $7$。

【答案提交】
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。

---

【思路分析】

这道题又是一个超大数，斐波那契本来就是指数级增长，直接爆肯定是不行的。

1. 首先就是采取对斐波那契数列的优化，这道题问的是个位数是7，跟十位以上的数没有关系，所有得出一项可以直接%10取个位数。增加计算效率。

2. 但题目要求的项数仍然是一个非常巨大的数，题目中的数字仅有1、2、0这3个数字组成，要考虑一下找规律，先找前1000项，2000项的数量：前1000项为134，1000~2000项为133，和为267.

   ```pycon
   In [4]: s=0
   
   In [5]: for i in range(1,1000):
      ...:     if fib(i)%10==7: s+=1
      ...:
   
   In [6]: s
   Out[6]: 134
   
   In [7]: s=0
   
   In [8]: for i in range(1,2000):
      ...:     if fib(i)%10==7: s+=1
   
   In [9]: s
   Out[9]: 267
   ```

3. 再观察前10000项和前20000项中个位是7的数量：前10000项为1334，前20000项为2667.

4. 再观察前100000项和前200000项中个位数是7的数量：前100000项为13334，前20000项为26667.

5. 找到规律：

   前10^n项：`'1'+'3'*(n-3)+'4'`个7

   前2*10^n项：`'2'+'6'*(n-3)+'7'`个7

6. 编写代码：

   ```python
   def calc(n):
       s = str(n)
       if s[0] == '1':
           return int('1' + (len(s) - 3) * '3' + '4')
       else:
           return int('2' + (len(s) - 3) * '6' + '7')
   
   
   m = str(202202011200)
   ans = 0
   for i in range(len(m)):
       t = int(m[i:])
       ans += calc(t)
   print(ans)
   ```

【参考答案】

```python
27227202885
```

【完整代码】

[A.py · AYO/Algorithm - Gitee.com](https://gitee.com/ayo_yo/Algorithm/blob/蓝桥杯_国赛/A.py)

## 试题B: 小蓝做实验（5分）

【问题描述】
小蓝很喜欢科研，他最近做了一个实验得到了一批实验数据，一共是两百万个正整数。如果按照预期，所有的实验数据 x 都应该满足 10⁷ ≤ x ≤ 10⁸。但是做实验都会有一些误差，会导致出现一些预期外的数据，这种误差数据 y 的范围是 10³
≤ y ≤ 10¹² 。由于小蓝做实验很可靠，所以他所有的实验数据中 99.99% 以上都是符合预期的。小蓝的所有实验数据都在 primes.txt 中，现在他想统计这两百万个正整数中有多少个是质数，你能告诉他吗？

【答案提交】
这是一道结果填空的题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。

---

【思路分析】

这个题有200w个数，直接暴力找肯定不行。我一开始走了弯路子，多线程，素数判断优化都用上了。最后才发现我想多了，比赛结束前1分钟才把数爆出来，也没时间写针对大数的素性测试了。。思路如下：

1. 首先观察数据，均以1、3、5、7结尾。大于1000且结尾为5的数，肯定能被5整除，于是先利用编辑器正则替换所有以5结尾的数，此时剩下约150w多个数：

   ```regex
   \d+?5
   
   ```

2.
使用埃氏筛选法，获得10^8以内的所有质数，这里注意，利用埃氏筛选法需要进行优化，不然也是跑的头大。我在之前博客里也写过直接判断质数的优化方法，除了2、3，所有质数均位于6n左右。因此可以直接将埃氏筛选法的步长拉到6，这样速度能进一步提升，然后影响埃氏筛选法速度的大头主要是2、3、5，需要进行多次循环才能筛掉后边的合数，因此预处理在生成列表时直接将2、3、5的倍数归0。理论上直接归零的质数倍数越多，生成素数就越快。

> [计数质数 Python 埃氏筛选法_AYO_YO的博客-CSDN博客](https://blog.csdn.net/weixin_44289959/article/details/117461733)
>
> [判断质数 Python Java C++_AYO_YO的博客-CSDN博客](https://blog.csdn.net/weixin_44289959/article/details/111240159)

```python
def getprimes(n):
    ls = [i if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 else 0 for i in range(n + 1)]
    ls[1], ls[2], ls[3], ls[5] = 0, 2, 3, 5
    for i in range(6, n + 1, 6):
        f = i - 1
        if f != 0:
            for j in range(2 * f, n + 1, f):
                ls[j] = 0
            continue
        f = i + 1
        if f != 0:
            for j in range(2 * f, n + 1, f):
                ls[j] = 0
    return filter(lambda x: x != 0, ls)
```

3. 埃氏筛选法筛选$10^8$以内的质数大概需要2分钟左右，再大恐怕就难以承受了。于是先将 $10^8$的质数统计出来，并把大于$10^8$的质数拎出来。得到结果$10^8$以内的质数有506733个。大数有约130个。

   ```python
   506733
   [542693491967, 142787902577, 452440529173, 663634895869, 71242929179, 999870483413, 441673697183, 895134836909, 59008094959, 812048153483, 153230177243, 5986461211, 825268545161, 85386152959, 305669636917, 176618331487, 627185459239, 517233054923, 347714268719, 75380450897, 652349118967, 746710276723, 887316078643, 55623754253, 726602124691, 63723051253, 11944000489, 14326008041, 995344474081, 127374806651, 101228446879, 782792370337, 7616731547, 672817895497, 309261587441, 993510068537, 898280626321, 691250724803, 436362423451, 135244424501, 873959450791, 404517752423, 803431472291, 890481756773, 299729772337, 993254812121, 939705423281, 928689411767, 950796808643, 925182899009, 867933942403, 177084914339, 374154056921, 195931411013, 636268614181, 845966263637, 669349089677, 279219681547, 116772294307, 458677064359, 414099720659, 553029935971, 225122592047, 523383194647, 291752440213, 29190046721, 756126896941, 400963923179, 807339716593, 666619632839, 792597812483, 157223341237, 515677221383, 869902952023, 277744493561, 279840195947, 12066121523, 659914745389, 796743912131, 973038777059, 856703807231, 66169702601, 987064845247, 916671221021, 884623305749, 504935549881, 232438712231, 701919604183, 542037833447, 521942095081, 726449610001, 840499018589, 492469281101, 757165962919, 437417377471, 903288533789, 254110134101, 265121359891, 776841707227, 854559132599, 325401328397, 675731682791, 730947154187, 280786162939, 670729451441, 48996391291, 286681507897, 847973529401, 166381727761, 568868879153, 56085663143, 417414542761, 666771906149, 857635614683, 188918440631, 490214446741, 82741563491, 411523187461, 304024439243, 912661149107, 556591023551, 934801057481, 828742723319, 814141769183, 528476615281, 560425065263, 224638484077, 610321268093, 655599334577, 624348698849]
   ```

4.
这些大数直接判断是否是质数也是相当恐怖的，于是判断特大数是否是质数，就要用另一个方法——费马素性测试。这个是我之前算法课期末作业研究过的一个算法，就是利用随机数随机对大数取余，如果能整除，就不是质数；加入了一个优化，加入了一个互质判断，大大提升了算法效率以及准确率。

```python
for p in bigNum:
    K = 100 # 取随机数验证的次数，该次数越大，准确率越高。实测K=10就能得到准确结果了
    k = 0
    while k < K:  # 这里用while是后续判定随机完成率是否是100%
        b = int(random.random() * (p - 1) + 1)  # 生成一个1~p-1之间的随机整数
        factor = math.gcd(b, p)  # 计算b,p的最大公约数
        r = runFermatPower(b, p, p)  # 计算b^p mod p
        print(f"第{k + 1}次取随机数, 随机数b={b}, {b}和{p}的最大公约数为{factor}, r=({b}^{p})mod p={r}", end=', ')
        if factor > 1:
            print(f"因b={b}与p={p}的最大公约数为{factor}，不为互质数，故p={p}为合数")
            break
        elif r != b:
            print(f"因r={r},({b}^{p}) mod p ={r}!={b}, 故p={p}为合数")
            break
        else:
            print(f"故p={p}可能为素数")
            k += 1
    if k == K:
        print(f"经过{K}次循环验证, p={p}可能为素数, n为素数的概率为{(1 - 1 / (2 ** k)) * 100}%")
```

5. 得到最终结果：

   ```python
   506753
   ```

【完整代码】

比赛过程中的代码是分步骤的，一步步写，然后得到结果后再计算下一步，这个代码是优化过的完整版代码，直接运行就能得到最终结果。

[B.py · AYO/Algorithm - 码云 - 开源中国 (gitee.com)](https://gitee.com/ayo_yo/Algorithm/blob/蓝桥杯_国赛/B.py)

## 试题C：取模（10分，10s，512MB）

【问题描述】

给定 $n, m$ ，问是否存在两个不同的数 $x, y$ 使得 $1 ≤ x < y ≤ m$ 且$n$ mod $x$ = $n$ mod $y$ 。

【输入格式】

输入包含多组独立的询问。

第一行包含一个整数 T 表示询问的组数。

接下来 $T$ 行每行包含两个整数 $n, m$，用一个空格分隔，表示一组询问。

【输出格式】

输出 $T$ 行，每行依次对应一组询问的结果。如果存在，输出单词 `Yes`；如果不存在，输出单词 `No`。

【样例输入】

```
3
1 2
5 2
999 99
```

【样例输出】

```
No 
No 
Yes
```

【评测用例规模与约定】

对于 $20\%$ 的评测用例，$T ≤ 100 ，n, m ≤ 1000$；

对于 $50\%$ 的评测用例，$T ≤ 10000 ，n, m ≤ 10^5$；

对于所有评测用例，$1 ≤ T ≤ 10^5 ，1 ≤ n ≤ 10^9 ，2 ≤ m ≤ 10^9$。

---

【思路分析】

没啥巧妙的解法，直接暴力做，通关估计够呛。

【参考代码】

[C.py · AYO/Algorithm - Gitee.com](https://gitee.com/ayo_yo/Algorithm/blob/蓝桥杯_国赛/C.py)

## 试题D：内存空间（10分，10s，512MB）

【问题描述】

小蓝最近总喜欢计算自己的代码中定义的变量占用了多少内存空间。为了简化问题，变量的类型只有以下三种：

`int`：整型变量，一个 `int` 型变量占用 `4 Byte` 的内存空间。

`long`：长整型变量，一个 `long` 型变量占用 `8 Byte` 的内存空间。

`String`：字符串变量，占用空间和字符串长度有关，设字符串长度为 L，则字符串占用 `L Byte` 的内存空间，如果字符串长度为 `0` 则占用 `0 Byte` 的内存空间。

定义变量的语句只有两种形式，第一种形式为：

`type var1=value1,var2=value2…;`

定义了若干个 type 类型变量 var1、var2、…，并且用 value1、value2…初始化，多个变量之间用`,`  分隔，语句以`;` 结尾，type 可能是 `int`、`long `或 `String`
。例如 `int a=1,b=5,c=6;` 占用空间为 `12 Byte`；`long a=1,b=5;`占用空间为 `16  Byte`；`String s1=””,s2=”hello”,s3=”world”;`
占用空间为 `10 Byte`。

第二种形式为：

`type[] arr1=new type[size1],arr2=new type[size2]…;`

定义了若干 type 类型的一维数组变量 arr1、arr2…，且数组的大小为 size1、size2…，多个变量之间用`,` 进行分隔，语句以`;` 结尾，type 只可能是 `int` 或 `long`
。例如 `int[] a1=new int[10];` 占用的内存空间为 `40 Byte`；`long[] a1=new long[10],a2=new long[10];` 占用的内存空间为`160 Byte`。

已知小蓝有 T 条定义变量的语句，请你帮他统计下一共占用了多少内存空间。结果的表示方式为：a`GB`b`MB`c`KB`d`B`，其中 a、b、c、d 为统计的结果，`GB`、`MB`、`KB`、`B `
为单位。优先用大的单位来表示，`1GB=1024MB`， `1MB=1024KB`，`1KB=1024B`，其中 B 表示 Byte。如果 a、b、c、d 中的某几个数字为
0，那么不必输出这几个数字及其单位。题目保证一行中只有一句定义变量的语句，且每条语句都满足题干中描述的定义格式，所有的变量名都是合法的且均不重复。题目中的数据很规整，和上述给出的例子类似，除了类型后面有一个空格，以及定义数组时 new
后面的一个空格之外，不会出现多余的空格。

【输入格式】

输入的第一行包含一个整数 $T$，表示有 $T$ 句变量定义的语句。接下来 $T$ 行，每行包含一句变量定义语句。

【输出格式】

输出一行包含一个字符串，表示所有语句所占用空间的总大小。

【样例输入 1】

```
1

long[] nums=new long[131072];
```

【样例输出 1】

```
1MB
```

【样例输入 2】

```
4
int a=0,b=0; long x=0,y=0;
String s1=”hello”,s2=”world”;
long[] arr1=new long[100000],arr2=new long[100000];
```

【样例输出 2】

```
1MB538KB546B
```

【样例说明】

样例 1，占用的空间为 $131072 × 8 = 1048576 B$，换算过后正好是 `1MB`，其它三个单位 `GB`、`KB`、`B` 前面的数字都为 `0` ，所以不用输出。

样例 2，占用的空间为 $4 × 2 + 8 × 2 + 10 + 8 × 100000 × 2 B$，换算后是`1MB538KB546B`。

【评测用例规模与约定】

对于所有评测用例，$1 ≤ T ≤ 10$，每条变量定义语句的长度不会超过 $1000$。所有的变量名称长度不会超过 $10$，且都由小写字母和数字组成。对于整型变量，初始化的值均是在其表示范围内的十进制整数，初始化的值不会是变量。对于 `String` 类型的变量，初始化的内容长度不会超过 $50$，且内容仅包含小写字母和数字，初始化的值不会是变量。对于数组类型变量，数组的长度为一个整数，范围为：$[0, 2^{30}]$，数组的长度不会是变量。$T$ 条语句定义的变量所占的内存空间总大小不会超过 `1 GB`，且大于 `0 B`。

【思路分析】

这个题乍一看还挺唬人的，占了足足3页，因为我前两道填空题占用了非常多的时间，已经开始慌了，到这题时一看题，心想凉了，这才第二道编程题就这么难了吗😂但仔细读了一下题目，发现并不难，跟着题目做就行，得益于Python操作字符串非常方便，所以能给这道题省下不少功夫。

思路如下：

- 首先应该计算当前表达式占用了多少`Byte`，而且表达式中变量名、`=`、关键字`new`这些都属于无关变量，直接忽略即可

- 获取输入的单行表达式后，使用`input().split(maxsplit=1)`获取输入并以第一个空格分隔，主要是用于判断最左侧的数据类型`if '[]' in typ`

- 如果类型为数组，注意数组只有`int`和`long`：

    - 获取数组的类型以后，直接正则匹配赋值式中的中括号（初始化数组的长度信息在这里，例如`int[] arr = new int[3];`取3）乘以对应变量长度相加即可

- 如果类型为普通类型，则需要额外判断是不是`String`：

    - 若为`String`：直接正则`”.+?”`匹配`”`，注意题目样例里这是一个**中文字符**。匹配到所有值以后直接计算长度相加即可。
    - 若不为`String`：直接`.count(',')`计算`,`的长度，变量数量比`,`数量多1，然后乘以对应长度相加即可。

- 把总长度按要求格式输出即可：

  ```python
  def convertSize(byte):
      size = {'GB': 0, 'MB': 0, 'KB': 0, 'B': 0}
      if byte >= 1073741824:
          size['GB'] = byte // 1073741824
      byte %= 1073741824
      if byte >= 1048576:
          size['MB'] = byte // 1048576
      byte %= 1048576
      if byte >= 1024:
          size['KB'] = byte // 1024
      byte %= 1024
      size['B'] = byte
      return size
  
  
  def printSize(l):
      size = convertSize(l)
      ans = ''
      # 正常情况下直接遍历字典即可，但我不太确定考试环境的3.8中的字典是否有序。3.9以后肯定是有序的了
      if size['GB'] > 0:
          ans += f'{size["GB"]}GB'
      if size['MB'] > 0:
          ans += f'{size["MB"]}MB'
      if size['KB'] > 0:
          ans += f'{size["KB"]}KB'
      if size['B'] > 0:
          ans += f'{size["B"]}B'
      print(ans)
  ```

【参考代码】

[D.py · AYO/Algorithm - Gitee.com](https://gitee.com/ayo_yo/Algorithm/blob/蓝桥杯_国赛/D.py)

## 试题E：近似GCD（15分，10s，512MB）

【问题描述】

小蓝有一个长度为 $n$ 的数组$ A = (a_1, a_2, · · · , a_n)
$，数组的子数组被定义为从原数组中选出连续的一个或多个元素组成的数组。数组的最大公约数指的是数组中所有元素的最大公约数。如果最多更改数组中的一个元素之后，数组的最大公约数为 g，那么称 g 为这个数组的近似 GCD。一个数组的近似 GCD
可能有多种取值。

具体的，判断 g 是否为一个子数组的近似 GCD 如下：

1. 如果这个子数组的最大公约数就是 g，那么说明 g 是其近似 GCD。
2. 在修改这个子数组中的一个元素之后（可以改成想要的任何值），子数组的最大公约数为 g，那么说明 g 是这个子数组的近似 GCD。

小蓝想知道，数组 A 有多少个长度大于等于 2 的子数组满足近似 GCD 的值为 g。

【输入格式】

输入的第一行包含两个整数 n, g，用一个空格分隔，分别表示数组 A 的长度和 g 的值。

第二行包含 n 个整数$ a_1, a_2, · · · , a_n$，相邻两个整数之间用一个空格分隔。

【输出格式】

输出一行包含一个整数表示数组 A 有多少个长度大于等于 2 的子数组的近似 GCD 的值为 g 。

【样例输入】

```
5 3
1 3 6 4 10
```

【样例输出】

```
5
```

【样例说明】

满足条件的子数组有 5 个：

$[1, 3]$：将 1 修改为 3 后，这个子数组的最大公约数为 3 ，满足条件。

$[1, 3, 6]$：将 1 修改为 3 后，这个子数组的最大公约数为 3 ，满足条件。

$[3, 6]$：这个子数组的最大公约数就是 3 ，满足条件。

$[3, 6, 4]$：将 4 修改为 3 后，这个子数组的最大公约数为 3 ，满足条件。

$[6, 4]$：将 4 修改为 3 后，这个子数组的最大公约数为 3，满足条件。

【评测用例规模与约定】

对于 $20\%$ 的评测用例，$2 ≤ n ≤ 10^2$；

对于 $40\%$ 的评测用例，$2 ≤ n ≤ 10^3$；

对于所有评测用例，$2 ≤ n ≤ 10^5 ，1 ≤ g, a_i ≤ 10^9$。

---

【思路分析】

这道题虽然说是gcd，但和gcd其实没有什么关系。。。

主要是划分子数组，如果子数组中只有至多 1 个数不是 g 的因子。那么这个子数组就是满足条件的，因为可以任意修改，无需关注修改为什么值。

【参考代码】

[E.py · AYO/Algorithm - Gitee.com](https://gitee.com/ayo_yo/Algorithm/blob/蓝桥杯_国赛/E.py)

## 试题I：owo（25分，10s，512MB）

【问题描述】

小蓝很喜欢 owo ，他现在有一些字符串，他想将这些字符串拼接起来，使得最终得到的字符串中出现尽可能多的 owo 。

在计算数量时，允许字符重叠，即 owowo 计算为 2 个，owowowo 计算为3 个。

请算出最优情况下得到的字符串中有多少个 owo。

【输入格式】

输入的第一行包含一个整数 n ，表示小蓝拥有的字符串的数量。接下来 n 行，每行包含一个由小写英文字母组成的字符串 si 。

【输出格式】

输出 n 行，每行包含一个整数，表示前 i 个字符串在最优拼接方案中可以得到的 owo 的数量。

【样例输入】

```
3
owo w ow
```

【样例输出】

```
1
1
2
```

【评测用例规模与约定】

对于 $10\%$ 的评测用例，$n ≤ 10$；

对于 $40\%$ 的评测用例，$n ≤ 300$；

对于 $60\%$ 的评测用例，$n ≤ 5000$；

对于所有评测用例，$1 ≤ n ≤ 10^6 ，1 ≤ |s_i| ， |s_i| ≤ 10^6$，其中 $|s_i|$ 表示字符串 $s_i$的长度。

---

【思路分析】

这个题虽然是25分的题，但用Python来做，不算难，，盲猜应该用动规，但时间不多了，来不及细推，我选择的是直接暴力做。暴力全排列，时间复杂度极其之高。虽然题目给了10s，，但估计还是过不去。

- 首先是找到字符串里的`owo`，这个比较取巧的方法就是直接正则`'owo'`匹配，但是正则一个字符只能匹配一次，但是题目要求中o可以用两次，那么直接`.replace('o','oo')`，把每个`o`
  扩充成两个，这样就可以正常进行正则匹配了。
- 将每次输入都保存到数组中，然后使用`itertools.permutations()`生成全排列，再循环寻找最大`owo`最多的数组。

【完整代码】

[I.py · AYO/Algorithm - Gitee.com](https://gitee.com/ayo_yo/Algorithm/blob/蓝桥杯_国赛/I.py)

