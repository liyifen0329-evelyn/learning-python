# lesson18.py — 第 18 课 · groupby（分堆）
#
# 一句话：把"分堆统计"这件事，从 SQL 的 GROUP BY 搬到 pandas。
#
# 跑法：  python3 lesson18.py
# 从上往下看输出，一步一步对。这一步不用你写代码，先跑通、看懂。

import pandas as pd

df = pd.read_csv("data/drone_flights.csv")


# ============================================================
# 第 1 步 · 只"分堆"，什么都不算
# ============================================================
# 今天的动词：df.groupby("route")
# 括号里跟 SQL 的 GROUP BY 后面一样 —— 放"按什么分堆"，是【一个列名】

print("=== 第 1 步：df.groupby(\"route\") 分出来的到底是什么？ ===")
g = df.groupby("route")
print(g)
print()

# 你看到的不是表、也不是一堆数字，而是一行 <...DataFrameGroupBy object...>。
# 这就是今天的核心认知：
#
#   groupby 不给你【答案】，它给你一台【分好堆的机器】。
#   你得再跟它说一句"每堆要算什么"，它才吐答案。


# ============================================================
# 第 2 步 · 跟机器说"每堆算几行" —— 接上 .size()
# ============================================================
# 第二段是"贴在"分堆机器后面的：点号连着，中间不能断开，更不能另起一行

print("=== 第 2 步：df.groupby(\"route\").size() ===")
print(df.groupby("route").size())
print()

# 读这个输出：每一行 = 一条航线 + 它飞了几次
#   深圳北站-科技园   5    ← 这一堆里有 5 条记录
#   ...


# ============================================================
# 第 3 步 · 再排个序
# ============================================================
print("=== 第 3 步：后面再接 .sort_values(ascending=False) ===")
print(df.groupby("route").size().sort_values(ascending=False))
print()


# ============================================================
# 第 4 步 · 换个"每堆算什么"：分堆那一截一个字不用改
# ============================================================
# 只算某一列的时候，在【分堆】和【算什么】两段中间，插一个 ["列名"]

print("--- 4-1 每堆几行（.size()）---")
print(df.groupby("route").size())
print()

print("--- 4-2 每堆的平均落地电量（.mean()）---")
print(df.groupby("route")["battery_left_pct"].mean())
print()

# 对照着看这三段：
#   df.groupby("route")            ← ① 分堆
#               ["battery_left_pct"]  ← ② 要算哪一列（只算一列时才写）
#                               .mean()  ← ③ 每堆算什么


# ============================================================
# 第 5 步 · 一个坑（就是你今天掉进去的那个）
# ============================================================
print("=== 第 5 步：同一个 .size，挂在不同东西上，结果完全不同 ===")

# 挂在【一列】身上：它给你的是一列车有几个元素 —— 一个数字，不是动作
print("df[\"route\"].size      =", df["route"].size)      # 20

# 挂在【分堆机器】身上：它给你的才是"每堆几行"
print("df.groupby(\"route\").size() 长这样：")
print(df.groupby("route").size())
print()

# 所以：一个【不带括号】（它是描述），一个【必须带括号】（它是动作）。
# 回扣第 12 课：df.shape 也不带括号，同一个道理。


# ============================================================
# 第 6 步 · 和 SQL 对一张表（你今天上午刚写的）
# ============================================================
#   SQL                                    pandas
#   FROM drone_flights                     df = pd.read_csv("data/drone_flights.csv")
#   GROUP BY route                         .groupby("route")
#   COUNT(*)                               .size()
#   MAX(max_height_m)                      ["max_height_m"].max()
#   AVG(battery_left_pct)                  ["battery_left_pct"].mean()
#   ORDER BY ... DESC                      .sort_values(ascending=False)
#
# 一个区别：SQL 一句话说完；pandas 是【两段式】——
# 先分堆，再补一句"每堆算什么"。


# ============================================================
# 练习（现在轮到你自己写）
# ============================================================
# 原题：每条航线飞了几次，从多到少排
#   期望输出：
#     深圳北站-科技园      5
#     宝安机场-光明科学城    4
#     深圳湾-前海        4
#     福田口岸-河套       3
#     盐田港-大鹏        2
#     龙岗中心城-坪山      2
print(df.groupby("route"))
df.groupby("route")
hx = df.groupby("route").size()
print(hx.sort_values(ascending=False))

# 变式题：每条航线的最高飞行高度（max_height_m），从高到低排
#   期望输出：
#     宝安机场-光明科学城    136
#     深圳北站-科技园      131
#     盐田港-大鹏        127
#     深圳湾-前海        122
#     龙岗中心城-坪山      115
#     福田口岸-河套       101
df.groupby("route")
hx = df.groupby("route")["max_height_m"]
print(hx.max().sort_values(ascending=False))