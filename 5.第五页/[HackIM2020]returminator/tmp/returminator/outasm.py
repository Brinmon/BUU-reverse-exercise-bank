from pwn import *
# 这个发现其实就是main函数里 dest的地址，改写成dest就好了！ 原：4210848: 'db 28h dup(?)',
dic = {4198818: 'pop     rax retn', 4210848: 'flag', 4198810: 'pop     rdi retn', 4198820: 'add     rax, rdi retn', 4198890: 'mov     rdi, rax retn', 4198870: 'movzx   rdi, byte ptr [rdi] retn', 4198812: 'pop     rsi retn', 4198824: 'add     rax, rsi retn', 4198894: 'mov     rsi, rax retn', 4198875: 'movzx   rsi, byte ptr [rsi] retn', 4198814: 'pop     rdx retn', 4198828: 'add     rax, rdx retn', 4198898: 'mov     rdx, rax retn', 4198880: 'movzx   rdx, byte ptr [rdx] retn', 4198845: 'xor     rax, rax retn', 4198849: 'sub     rax, rdi retn', 4198911: 'call    _exit', 4198857: 'sub     rax, rdx retn', 4198816: 'pop     rcx retn', 4198832: 'add     rax, rcx retn', 4198902: 'mov     rcx, rax retn', 4198885: 'movzx   rcx, byte ptr [rcx] retn', 4198861: 'sub     rax, rcx retn', 4198853: 'sub     rax, rsi retn'}

o = [296, 272, 272, 272, 296, 360, 272, 424, 272, 208, 120, 120, 120, 96, 120, 120, 120, 120, 120, 120, 120, 208, 120, 120, 208, 208, 208, 208, 208, 272, 120, 208, 208]
 
txt = ''

data_list = []  # 存储数据的列表

with open('blob', 'rb') as f:
    for offset in o:
        data = f.read(offset)
        groups = [data[i:i+8] for i in range(0, len(data), 8)]
        for c in groups:
            write_addr=u64(c)
            if write_addr==0x6161616161616161:
                print("======================================")
                txt += "======================================\n"
                continue
            if write_addr in dic:
                txt += dic[write_addr]+'\n'
                print(dic[write_addr])
            else:
                txt += hex(write_addr)+'\n'
                print(hex(write_addr))

# 打开文件并以写入模式写入数据
with open("outasm.txt", "w") as file:
    file.write(txt)

print("数据已成功写入文件。")
