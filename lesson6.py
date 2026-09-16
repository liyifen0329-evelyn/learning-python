# -*- coding: utf-8 -*-
"""第 6 课: 函数 def —— 从"写一段话"到"造一个工具"

用法: 别急着跑! 先通读一遍, 猜猜每一部分会打印出什么, 再运行对答案。
"""

# ============ 1. 最小的函数 ============
# def = define(定义)。给它起个名字, 名字后面的 () 里放"要交给它的材料"

def say_hello(name):
    print("你好,", name)

say_hello("Evelyn")
say_hello("刘杰博士")
say_hello("深圳")


# ============ 2. return: 函数把结果"吐"回来 ============

def double(x):
    return x * 2

print(double(5))
print(double(100))
print(double(7) + double(3))


# ============ 3. 动手: 把第 5 课的统计打包成一个工具 ============
# 下面是第 5 课留下的"散装"代码 —— 数据一换就得重跑一遍, 还不算工具。

heights = [90, 77, 120, 140, 85, 100]

def summary(data):
    print("无人机数量:", len(data))
    print("总高度:", sum(data))
    print("平均高度:", sum(data) / len(data))
    print("最高:", max(data))
    print("最低:", min(data))

summary(heights)

summary([120])
other = [300,60,90]
summary(other)



#
#     def summary(heights):
#         这里放统计的代码(注意缩进)
#
# TODO 2: 把上面的 5 个 print 删掉, 改成调用它:  summary(heights)
#
# TODO 3: 再加一行  summary([120])  —— 只有一架无人机, 结果还对吗?
#         (想想上次那个"边界值必须专门测试的教训)
