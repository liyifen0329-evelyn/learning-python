# review12.py — 第 12 课的核心，只有这几行
# 对照看你 redo_12.py 里手写的那一坨：open / readlines / strip / split / 配对
# 这 5 步，pandas 用下面这一行全干完了。

import pandas as pd

df = pd.read_csv("data/flight_log.csv")

print(df)
