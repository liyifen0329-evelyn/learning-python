# moxie_14.py — 默写卡 12 · 给每一行打标签（复习第 14 课）
#
# 【规则】不许打开 lesson14.py，不许翻笔记。卡住就写一行
#         # 卡住：xxx  然后跳过继续，别当场翻书。
#
# 【要做什么】读 data/flight_log_02.csv 进 df，加一列 status：
#     高度超过 120 米              → ⚠️ 超限
#     超过 110 米但不超过 120 米   → 🟡 接近限高
#     其余                         → ✅ 正常
#   然后打印整张表。
#
# 【期望输出】整张表 12 行 + 多出一列 status。自己核一下条数：
#     ⚠️ 超限      4 条
#     🟡 接近限高   2 条
#     ✅ 正常      6 条
#
# 你的代码写在最下面：
import pandas as pd
df = pd.read_csv("data/flight_log_02.csv")
print(df)
df["status"] = "正常"
df.loc[df["height_m"] > 110, "status"] = "接近限高"
df.loc[df["height_m"] > 120, "status"] = "超限"
print(df)