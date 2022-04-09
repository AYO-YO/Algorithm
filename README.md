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
