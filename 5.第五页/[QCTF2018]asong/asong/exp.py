dataread = []
with open(r'D:\CTF_Study\Reverse\BUU\5.第五页\[QCTF2018]asong\asong\out', 'rb') as file:
    byte = file.read(1)
    while byte:
        dataread.append(int(byte.hex(), 16))
        byte = file.read(1)
print("读取out的数据：",dataread)

data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x68, 0x1E, 0x0F, 0x1D, 0xA9, 0x13, 0x26, 0x43, 0x3C, 0x00, 0x14, 0x27, 0x1C, 0x76, 0xA5, 0x1A, 0x00, 0x3D, 0x33, 0x85, 0x2D, 0x07, 0x22, 0x00, 0x3E, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x28, 0x47, 0x00, 0x00, 0x42, 0xF5, 0x00, 0x00, 0x00, 0x61, 0x00]
data1 = [0x00000016, 0x00000000, 0x00000006, 0x00000002, 0x0000001E, 0x00000018, 0x00000009, 0x00000001, 0x00000015, 0x00000007, 0x00000012, 0x0000000A, 0x00000008, 0x0000000C, 0x00000011, 0x00000017, 0x0000000D, 0x00000004, 0x00000003, 0x0000000E, 0x00000013, 0x0000000B, 0x00000014, 0x00000010, 0x0000000F, 0x00000005, 0x00000019, 0x00000024, 0x0000001B, 0x0000001C, 0x0000001D, 0x00000025, 0x0000001F, 0x00000020, 0x00000021, 0x0000001A, 0x00000022, 0x00000023]
outdata = [236, 41, 227, 65, 225, 247, 170, 29, 41, 237, 41, 153, 57, 243, 183, 169, 231, 172, 43, 183, 171, 64, 159, 169, 49, 53, 44, 41, 239, 168, 61, 75, 176, 233, 225, 104, 123, 65]

i = 37
start_3 = outdata[37]<<5
while(i > 0):
    outdata[i] = (outdata[i]>>3 | outdata[i-1]<<5) & 0xff
    i -= 1
outdata[0] = ((outdata[0]>>3) | start_3) & 0xff
print("逆运算第一步后的数据：",outdata)

idx = 0
left = []
right = []
while(data1[idx]):
    left.append(idx)
    right.append(data1[idx])
    idx = data1[idx]
left.append(1)
right.append(0)
print(left)
print(right)
left.reverse()
right.reverse()
for i in range(len(outdata)):
    outdata[right[i]] = outdata[left[i]]
print("逆运算第二步后的数据：",outdata)

def trancode(a):
    if a==10:
        return a+35
    elif (a==32) or (a==33) or (a==34):
        return a+10
    elif a==39:
        return a+2
    elif a==44:
        return a-4
    elif a==46:
        return a-7
    elif (a==58) or (a==59):
        return a-21
    elif a==63:
        return a-27
    elif a==95:
        return a-49
    else:
        if a <48 or a>57:   #数字
            if (a<=64) or (a>90):
                if (a>96) and (a<=122):
                    return a-87  #大写字母 不区分
                else:
                    return -1
            else:
                return a-55  #小写字母
        else:
            return a-48  #0-9
string1 = 'abcdefghijklmnopqrstuvwxyz0123456789_'#ABCDEFGHIJKLMNOPQRSTUVWXYZ
strlist=[i for i in string1]
vmtable = []
for i in string1:
    vmtable.append(trancode(ord(i))&0xff)
print("第三次逆运算的结果：",end="")
for ch in outdata:
    print(strlist[vmtable.index(data.index(ch))],end="")
