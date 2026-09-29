# moxie_15.py — 默写卡 13 · 排序 + 汇总（复习第 15 课）
#
# 【规则】不许打开 lesson15.py，不许翻笔记。卡住就写一行
#         # 卡住：xxx  然后跳过继续，别当场翻书。
#
# 【要做什么】读 data/flight_log_02.csv 进 df。
#   先把每一行的状态算出来，存成一列 status（三档，和上次一样）：
#     高度超过 120 米              → ⚠️ 超限
#     超过 110 米但不超过 120 米   → 🟡 接近限高
#     其余                         → ✅ 正常
#   然后打印两样东西：
#     1. 按 height_m 从高到低排好的整张表
#     2. status 这一列，每个类别各几条
# 【期望输出】第一块 —— 12 行，最高的在最上面：
#        timestamp  height_m  speed_ms  battery_pct status
#   6   14:01:00       145       8.4           77 ⚠️ 超限
#   7   14:01:10       138       8.1           73 ⚠️ 超限
#   5   14:00:50       130       8.0           81 ⚠️ 超限
#   4   14:00:40       122       7.8           85 ⚠️ 超限
#   3   14:00:30       118       7.4           89 🟡 接近限高
#   8   14:01:20       112       7.6           69 🟡 接近限高
#   9   14:01:30        96       7.2           65 ✅ 正常
#   2   14:00:20        90       7.0           93 ✅ 正常
#   10  14:01:40        80       6.8           61 ✅ 正常
#   1   14:00:10        75       6.5           97 ✅ 正常
#   11  14:01:50        65       6.0           57 ✅ 正常
#   0   14:00:00        60       6.2          100 ✅ 正常
#   第二块 —— 三行，多的在上面：
#   ✅ 正常      6
#   ⚠️ 超限      4
#   🟡 接近限高   2
#
# 你的代码写在最下面
import pandas as pd
df = pd.read_csv("data/flight_log_02.csv")
df["status"] = "正常"
df.loc[df["height_m"] > 110, "status"] = "接近限高"
df.loc[df["height_m"] > 120, "status"] = "超限"
print(df)
df_sorted = df.sort_values("height_m",ascending = False)
print(df_sorted)
print(df["status"].value_counts())
print(df)
