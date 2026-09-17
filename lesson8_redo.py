with open("data/welcome.txt", encoding="utf-8") as f:
      lines = f.readlines()

n = 1
for line in lines:
    print(n, line.strip())
print("这个文件一共", len(lines), "行")