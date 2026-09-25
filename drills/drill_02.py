# drill_02.py — 变式题（条件变了，套路一样）
#
# 【要做什么】读 data/flight_log_02.csv 进 df，然后打印四样东西：
#   1. 最高高度
#   2. 平均速度
#   3. 最低电量
#   4. 这张表有几行几列
#
# 【期望输出】（格式随意，数字要对）
#   最高高度: 145
#   平均速度: 7.25
#   最低电量: 57
#   表格大小: (12, 4)
#
# 你的代码写在最下面：
import pandas as pd
df = pd.read_csv("data/flight_log_02.csv")
print(df["height_m"].max())
print(df["speed_ms"].mean())
print(df["battery_pct"].min())
print(df.shape)
