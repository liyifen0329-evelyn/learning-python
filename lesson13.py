import pandas as pd

df = pd.read_csv("data/flight_log_02.csv")

# ① 先只比较，不筛选 —— 看看出来的是什么
print(df["height_m"] > 120)

# ② 把那串 True / False 塞回方括号里，只留 True 的行
print(df[df["height_m"] > 120])

# ③ 你的代码写在最下面，别夹在注释中间
print(df["battery_pct"] < 80)
print(df[df["battery_pct"] < 80])
print("总共",len(df[df["battery_pct"] < 80]))

df = pd.read_csv("data/flight_log.csv")
print(df["altitude"] > 120)
print(df[df["altitude"] > 120])
print("总共",len(df[df["altitude"] > 120]))