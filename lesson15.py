# 第 15 课 · 排序 + 汇总
#
# 前 14 课你都在"一行一行看数据"。
# 但报告里没人看 12 行原始数字 —— 报告要的是结论:
#     "最危险的是哪几秒"  /  "12 次采样里有几次超标"
#
# 今天两个动作, 都是【问表一个问题, 让它给你答案】。

import pandas as pd

df = pd.read_csv("data/flight_log_02.csv")
df["status"] = "✅ 正常"
df.loc[df["height_m"] > 110, "status"] = "🟡 接近限高"
df.loc[df["height_m"] > 120, "status"] = "⚠️ 超限"


# ── 动作 1 · 排序: 哪几秒最危险? ─────────────────────────
#    df . sort_values ( "按哪一列排" , ascending=False )
#         └ 排序         └ 报列名, 要引号  └ 从大到小
#   ascending = 上升。False = 不要上升 = 降序。
#   它【不改原表】—— 它吐出一张【新表】给你(第 6 课 return), 你得接住。
df_sorted = df.sort_values("height_m", ascending=False)
print(df_sorted)


# ── 动作 2 · 汇总: 各几条? ──────────────────────────────
#   先取出那一列 df["status"], 再在它屁股后面点 .value_counts()
#   value_counts = 数每个值各出现几次
#   —— 就是你第 10 课自己总结的那条规律: 被处理的东西 . 方法(参数)
print(df["status"].value_counts())


# ── 验证: 排完序, 原来的 df 变了没有? ────────────────────
print(df)


# ── 想一想(先猜, 再改代码跑)─────────────────────────────
# 如果 sort_values 后面【不写】 ascending=False, 第一行会是谁?
