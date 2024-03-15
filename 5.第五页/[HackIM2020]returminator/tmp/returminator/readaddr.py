from pwn import *

o = [296, 272, 272, 272, 296, 360, 272, 424, 272, 208, 120, 120, 120, 96, 120, 120, 120, 120, 120, 120, 120, 208, 120, 120, 208, 208, 208, 208, 208, 272, 120, 208, 208]

data_list = []  # 存储数据的列表

with open('blob', 'rb') as f:
    for offset in o:
        data = f.read(offset)
        groups = [data[i:i+8] for i in range(0, len(data), 8)]
        for c in groups:
            write_addr=u64(c)
            if(write_addr>0x400000 and write_addr < 0x500000):
                if write_addr not in data_list:
                    data_list.append(write_addr)  # 如果数据符合64位地址格式，则将其添加到列表中

print("符合64位地址格式的数据列表：", data_list)
