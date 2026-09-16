# -*- coding: utf-8 -*-
"""第 6 课(下半): 让工具"吐结果" —— return 的真正威力

上半场你造了 summary, 但它只会"喊"(print), 不会"吐"(return)。
现在来看看这事有多要命。
"""

heights = [90, 77, 120, 140, 85, 100]


# ---- 1. 你手上这台机器, 目前只会"喊" ----

def summary(data):
    count = len(data)
    total = sum(data)
    average = total / count
    hi= max(data)
    lo= min(data)
    return [count, total, average, hi, lo]

# ---- 2. 现在我想把"平均高度"存起来, 以后拿去画图 ----
# 先猜: result 里装的是什么?

result = summary(heights)
print(result)
print("平均高度是:",result[2])

print("---- result 装的是:", result)
print("---- 它是哪种类型:", type(result))


# ---- 3. 样板: 一个会"吐东西"的函数 ----
# 一个 return 只能吐一样东西。想吐好几个? 装进一个列表吐出来。

def 三个数():
    return [1, 2, 3]

a = 三个数()
print("---- 收到:", a)
print("---- 下标 0 是:", a[0])      # 还记得第 4 课: 下标从 0 开始


# ---- TODO: 轮到你了 ----
# 把上面第 1 部分的 summary 改造成"会吐结果"的版本:
#
#   1) 保留那 5 行统计, 但改成把结果存进变量(别直接 print)
#   2) 最后加一行:  return [数量, 总和, 平均, 最高, 最低]
#   3) 改完之后, 用 result = summary(heights) 接住它
#   4) 试试 print(result[2])  —— 你觉得会打印出什么?
#
# 改好保存, 跑 python3 lesson6b.py
