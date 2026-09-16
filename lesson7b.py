# -*- coding: utf-8 -*-
"""第 7 课(下半): 把 summary 改造成"会报名字"的工具

上半场你知道了: 列表靠位置, 字典靠名字。
现在把这个本事, 用回你自己写的 summary 上。
"""

heights = [90, 77, 120, 140, 85, 100]


# ---- 1. 老版本: 靠位置, 很脆 ----

def summary_old(data):
    count = len(data)
    total = sum(data)
    average = total / count
    hi = max(data)
    lo = min(data)
    return [count, total, average, hi, lo]


r = summary_old(heights)
print("老版本取平均:", r[2])

# 只要 return 里的顺序被人动一下, 这行就静默拿错数。
# 而且光看 r[2] 这三个字符, 三个月后的你 (或者 AI) 根本看不出它是"平均"。


# ============================================================
# 2. TODO: 你来写一个新版本
# ============================================================
# 上面那个 summary_old 别删 —— 留着当"反面教材", 待会儿对比用。
# 你在下面【新写一个】函数, 名字就叫 summary。
#
# 做法: 把 summary_old 整个抄下来, 只动两个地方
def summary(data):
    count = len(data)
    total = sum(data)
    average = total / count
    hi = max(data)
    lo = min(data)
    return {"count": count, "total": total, "average": average, "max": hi, "min": lo}

#   1) 第一行改名字:      def summary(data):
#   2) 中间 5 行统计, 一个字都不用改
#   3) 最后那行 return 改成:
result = summary(heights)
print(result)
print("平均值:", result["average"])
print("最高值:", result["max"])
print("最低值:", result["min"])
print("数量:", result["count"])
print("总和:", result["total"])
#        return {"count": count, "total": total, "average": average,
#                "max": hi, "min": lo}
#
#      键名用英文:
#        "count"   数量      "total"  总和      "average" 平均
#        "max"     最高      "min"    最低
#
#      ⚠️ 注意方向: 键名在【左】, 变量在【右】。
#         "average": average
#          左边: 你贴的标签    右边: 装着的值
#         别写反了。
#
#   为什么用英文? 真实工作里的数据都来自 JSON / 接口 / 数据库,
#   键名基本全是英文。中文键 Python 支持, 但工作中很少见。
#   顺便把这 5 个词记住 —— 读 AI 写的代码天天见到它们。
#
# 函数写好后, 在下面自己敲这三行 (别复制, 手打才记得住):
#   result = summary(heights)
#   print(result)
#   print("平均值:", result["average"])


# ============================================================
# 3. 想一想 (先别写, 想好了告诉我)
# ============================================================
# 现在如果有人把 return 里的顺序整个打乱, 变成:
#
#   return {"max": hi, "count": count, "average": average, "min": lo, "total": total}
#
# 你的 result["average"] 还会拿错数吗? 为什么?


# ============================================================
# 4. 收尾: 让数据自己说出结论
# ============================================================
# 背景 (你在低空经济课上学过的): 微型/轻型无人机在适飞空域,
# 真高一般不超过 120 米。而你的数据里最高是 140 米 —— 超了。
#
# 用今天学的字典 + 第 3 课学的 if, 让程序自己判断并打印结论。
# 条件就用 result["max"] > 120。
#
#   成立时打印:  ⚠️ 有飞行超过 120 米限高, 最高 ___ 米
#   否则打印:    ✅ 全部在限高内, 最高 ___ 米
#
# 自己敲, 别复制粘贴 —— 手打才记得住。

if result[ "max"] > 120:
    print("有飞行超过120米限高, 最高高度", result["max"], "米")
else:
    print("全部在限高内, 最高高度", result["max"], "米")
