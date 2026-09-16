# -*- coding: utf-8 -*-
"""第 5 课: 数数、求和、求平均 —— 把一排数据变成结论"""

heights = [90,77,120,140,85,100]

# 1) 这一队有几架无人机?  len = length(长度)
print("无人机数量:", len(heights))

# 2) 求高度总和: 先准备一个"记账本", 从 0 开始
total = 0
for h in heights:
    total = total + h
print("总高度:", total)

# 3) 求平均高度
average = total / len(heights)
print("平均高度:", average)

print("最高:",max(heights))
print("最低:",min(heights))
print("总和:",sum(heights))
