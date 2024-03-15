flag = ""  # 创建一个空字符串变量 flag，用于存储解密后的标志

with open("log.txt") as f:  # 打开名为 "log.txt" 的文件，并将其赋值给变量 f
    prev_h = None  # 创建一个变量 prev_h，用于存储前一个哈希值的初始值（设为 None）
    for l in f:  # 对文件 f 的每一行进行迭代
        try:
            print(l)
            arr = eval(l.strip())  # 去除行首尾的空白字符，然后使用 eval 函数将字符串转换为 Python 对象
            if arr[4] == 1:  #  如果 arr 列表的第五个元素为1
                if prev_h:  # 如果 prev_h 不为 None（即不是第一次迭代）
                    for i in range(256):  # 对范围在 0 到 255 的整数进行迭代
                        if (prev_h + i) * arr[1] % arr[0] == arr[2]:  # 如果满足一定条件
                            flag += chr(i)  # 将整数 i 转换为对应的 ASCII 字符，并将其添加到 flag 中
                            break  # 跳出内层循环
                prev_h = arr[2]  # 将 arr 列表的第三个元素赋值给变量 prev_h
        except:  # 如果发生异常（无法使用 eval 函数将字符串转换为 Python 对象）
            pass  # 继续下一次迭代

print(flag)  # 打印最终解密后的标志