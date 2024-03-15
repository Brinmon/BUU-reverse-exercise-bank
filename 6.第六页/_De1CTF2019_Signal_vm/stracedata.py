file_path = "stracedata.txt"  # 替换成你的文本文件路径

# 打开文本文件并读取每一行
with open(file_path, "r",encoding="utf-8") as file:
    lines = file.readlines()

# 过滤行，保留以“wait”开头的行
filtered_lines = [line for line in lines if line.startswith("wait")]

# 将过滤后的行写回文本文件
with open(file_path, "w") as file:
    file.writelines(filtered_lines)