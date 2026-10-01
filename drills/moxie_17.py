# 默写卡 15 · 画图（复习 lesson17）
import pandas as pd
df = pd.read_csv("data/flight_log_02.csv")

import matplotlib.pyplot as plt
df.plot(x="timestamp", y="battery_pct", title="深圳配送航线 · 电池变化")
plt.savefig("battery_check.png",dpi=150)