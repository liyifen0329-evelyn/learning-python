# hw15.py — 第 15 课作业（排序 + 汇总）
# 规矩不变：只给"要做什么"和"期望输出长什么样"，不给步骤、不给提示词。
#
# 数据都用 data/flight_log.csv
# ⚠️ 列名我不告诉你 —— 自己去表头里找（09-27 学的习惯：换数据先问数据）


# ══ 题 1 · 原题 ══════════════════════════════════════════════════
#
# 读进 df，然后打印两样东西：
#   1. 整张表，按【高度】从高到低排
#   2. 给每行加一列 level：
#         高度超过 110 米      → ⚠️ 超限
#         其余                 → ✅ 正常
#      然后打印 level 各出现几次
#
# 【期望输出】
#     表格 10 行，第一行高度 140，最后一行高度 75
#     ⚠️ 超限    4
#     ✅ 正常    6
import pandas as pd
df = pd.read_csv("data/flight_log.csv")

df["level"]= "正常"
df.loc[df["altitude"] > 110,"level"] = "超限"

df_sorted = df.sort_values("altitude",ascending = False)
print(df_sorted)
print("level出现了:",df["level"].value_counts(),"次")



# ══ 题 2 · 变式（换了列、换了方向、换了分档条件）═════════════════
#
#   1. 整张表，按【速度】从低到高排
#   2. 给每行加一列 level：
#         电量低于 90          → 🔋 低电量
#         其余                 → ✅ 正常
#      然后打印 level 各出现几次
#
# 【期望输出】
#     表格 10 行，第一行速度 7.8，最后一行速度 9.1
#     🔋 低电量    5
#     ✅ 正常     5
df["level"] = "正常"
df.loc[df["battery"] < 90, "level"] = "低电量"

df_sorted = df.sort_values("speed",ascending = True)
print(df_sorted)
print("level出现了:",df["level"].value_counts(),"次")

