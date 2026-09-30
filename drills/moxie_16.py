# moxie_16.py — 默写卡 14 · 筛 + 排 + 导出（复习第 16 课）
#
# 【规则】不许打开 lesson16.py / hw16.py，不许翻笔记。
#         卡住就写一行  # 卡住：xxx  然后跳过继续，别当场翻书。
#         限时 5 分钟。
#
# 【要做什么】读 data/flight_log.csv 进 df
#   （注意：不是 flight_log_02.csv，是另一个文件）
#
#   1. 把 altitude 超过 120 米的记录挑出来，
#      按 altitude 从高到低排好，用一个箱子接住
#   2. 把这个箱子导出成 data/over_limit.csv，
#      文件里不要出现座位号
#   3. 打印这个箱子一共几条
#
# 【期望输出】终端先打一行：
#   总共 3 条
#   然后 data/over_limit.csv 长这样（表头 + 3 行，
#   第一列不能是 4、5、3 这种座位号）：
#   time,altitude,speed,battery
#   09:00:40,140,9.0,90
#   09:00:50,132,8.6,88
#   09:00:30,125,9.1,92
#
# 你的代码写在最下面
import pandas as pd
df = pd.read_csv("data/flight_log.csv")
over120 = df[df["altitude"] > 120].sort_values("altitude",ascending = False)
over120.to_csv("data/over_limit.csv", index=False)
print(over120)
print("总共", len(over120), "条")