# -*- coding: utf-8 -*-
"""第 4 课: 列表 list + for 循环 —— 批量检查无人机高度"""

# 一排编了号的箱子, 5 个数 -> 编号 0,1,2,3,4
heights = [80, 150, 45, 320, 110]

# 对于 heights 里的每一个, 叫它 h, 把下面缩进的做一遍
for h in heights:
    if h < 120:
        print(h, "米  可以飞")
    else:
        print(h, "米  超高, 要许可")
