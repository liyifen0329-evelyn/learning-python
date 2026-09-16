height = int(input("请输入飞行高度(米): "))

if height < 120:
    print("✅ 安全:高度低于 120 米")
else:
    print("⚠️ 警告:高度达到或超过 120 米,请检查空域许可!")
