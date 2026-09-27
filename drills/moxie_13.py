# moxie_13.py — 默写卡 11 · 筛选 + 计数（复习第 13 课）
#
# 【规则】不许打开 lesson13.py，不许翻笔记。卡住就写一行
#         # 卡住：xxx  然后跳过继续，别当场翻书。
#
# 【要做什么】读 data/flight_log_02.csv 进 df，然后打印两样东西：
#   1. 高度超过 120 米的那些记录（整行都要，不是只打印高度）
#   2. 这些记录一共几条
#
# 【期望输出】（格式随意，数字要对）
#        timestamp  height_m  speed_ms  battery_pct
#   4    14:00:40       122       7.8           85
#   5    14:00:50       130       8.0           81
#   6    14:01:00       145       8.4           77
#   7    14:01:10       138       8.1           73
#   总共 4
#
# 你的代码写在最下面：
import pandas as pd
df = pd.read_csv("data/flight_log_02.csv")
print(df["height_m"] > 120 )
print(df[df["height_m"] > 120])
print(len(df[df["height_m"] > 120]))