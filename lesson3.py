# -*- coding: utf-8 -*-
"""第 3 课练习: 高度三档检查(教学简化版)"""

height = int(input("请输入飞行高度(米): "))

if height < 120:
    print("✅ 放心飞:低于 120 米")
elif height < 300:
    print("⚠️ 需要许可:120 米到 300 米之间")
else:
    print("🚫 禁止飞行:300 米及以上")
