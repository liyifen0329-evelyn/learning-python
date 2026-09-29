# hw16.py — 变式题 · 导出一份"告警清单"（第 16 课）
#
# 【要做什么】
#   读 data/flight_log_02.csv。
#   把高度超过 120 米的那些记录，按高度【从高到低】排好，
#   导出成一个文件，名字叫 alert_list.csv（文件里不要"座位号"那一列）。
#
# 【期望输出】
#   终端上什么都不打印（成功是安静的）。
#   打开 alert_list.csv，里面应该是这 5 行：
#
#   timestamp,height_m,speed_ms,battery_pct
#   14:01:00,145,8.4,77
#   14:01:10,138,8.1,73
#   14:00:50,130,8.0,81
#   14:00:40,122,7.8,85
#
# 你的代码写在最下面：
import pandas as pd
df = pd.read_csv("data/flight_log_02.csv")
Alist = df[df["height_m"] > 120].sort_values("height_m", ascending = False)

Alist.to_csv("alert_list.csv", index = False)
