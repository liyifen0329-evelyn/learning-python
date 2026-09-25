# redo_12b.py — 重打默写卡 09（第 12 课 pandas 入门）
#
# 规则：
#   - import pandas as pd / pd.read_csv(...) 这两行，允许打开 review12.py 看一眼，看一次就关掉
#   - 后面四个 print 必须自己想，不许参考任何文件
#   - 卡住就在原地写一行  # 卡住：xxx  ，然后跳过继续往下写
#
# 【要做什么】把 data/flight_log.csv 读进来放进 df，然后打印四样东西：
#   1. altitude 这一列的最大值
#   2. speed 这一列的平均值
#   3. battery 这一列的最小值
#   4. 这张表有几行几列
#
# 【期望输出】（格式随意，数字要对）
#   最高高度: 140
#   平均速度: 8.52
#   最低电量: 80
#   表格大小: (10, 4)
#
# 你的代码写在最下面这行下面：
import pandas as pd
df = pd.read_csv("data/flight_log.csv")
print(df["altitude"].max())
print(df["speed"].mean())
print(df["battery"].min())
print(df.shape)