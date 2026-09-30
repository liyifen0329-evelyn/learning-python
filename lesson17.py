# lesson17.py — 第 17 课 · 画图（把表格变成图）

import pandas as pd
import matplotlib.pyplot as plt

# 让图上的中文能显示出来，不写这行中文会变成一个个方块
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("data/flight_log_02.csv")

# 折线图：横轴走 timestamp，纵轴走 height_m
df.plot(x="timestamp", y="height_m", title="深圳配送航线 · 高度变化")

plt.xticks(rotation=45)   # 横轴的时间标签斜过来，不然挤成一团
plt.tight_layout()        # 自动调边距，别让字被切掉
plt.savefig("height_chart.png", dpi=150)              # 弹窗，把图显示出来

df.plot(x="timestamp", y="battery_pct",title="深圳配送航线 · 电量变化")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("battery_chart.png", dpi=150)