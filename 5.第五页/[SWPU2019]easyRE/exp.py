import string

def sumstartandend0(ch):#计算数据前面和后面有多少个0
    str = bin(ord(ch))[2:]
    start = 9 - len(str)
    end = 0
    for endch in str[::-1]:
        if(endch == '1'):
            break
        end = end + 1
    return start,end

def fun0(start,end):#计算数据前面和后面有多少个0
    return start+end

def fun1(ch,start,end):#计算一
    chnum = ord(ch)
    sum1 = start+end
    chnum = (chnum<<start)&0xff
    chnum = chnum>>sum1
    return chnum

def fun2(ch,start):#计算二
    return ord(ch)>>(8-start)

def fun3(ch,end):#计算三
    return ord(ch)>>(8-end)

def fun4(v3,start,end):##计算四
    return v3>>(start+end)

def fun5(v2,start,v4):#计算五
    return (v2<<start)|v4

def encode1(ch):#第一次加密的正运算，this_28_401E40
    start,end = sumstartandend0(ch)
    v0 = fun0(start,end)
    v1 = fun1(ch,start,end)
    v4 = fun4(fun3(ch,end),start,end)
    v5 = fun5(fun2(ch,start),start,v4)
    return v0,v1,v4,v5,start,end

def encode2(a1):#第二次加密的正运算：this_36_4028A0
    v14 = 32
    v15 = 0
    v15_1 = []
    for i in range(8):
        if(i>=4):
            v14-=a1.saelfun0[i-4]
            v15 |= a1.fun5l[i-4]<<v14
        else:
            v14 -= 8-a1.saelfun0[i]
            v15 |= a1.fun1l[i]<<v14
            v7 = 16*a1.startl[i]
            v15_1.append(a1.endl[i] | v7)
    return v15,v15_1


#分析出本次加密的数据结构，定义一个类，一次性初始化4个字符
class SN:
    def __init__(self,string):
        self.str = string
        self.saelfun0 = []
        self.startl = []
        self.endl = []
        self.fun1l = []
        self.fun4l = []
        self.fun5l = []
    
    def datainit(self):
        for ch in self.str:
            v0,v1,v4,v5,start,end = encode1(ch)
            self.saelfun0.append(v0)
            self.startl.append(start)
            self.endl.append(end)
            self.fun1l.append(v1)
            self.fun4l.append(v4)
            self.fun5l.append(v5)

    def printout(self):
        print(
            f"str: {self.str}\n"
            f"saelfun0: {self.saelfun0}\n"
            f"startl: {self.startl}\n"
            f"endl: {self.endl}\n"
            f"fun1l: {self.fun1l}\n"
            f"fun4l: {self.fun4l}\n"
            f"fun5l: {self.fun5l}\n"
        )

#"swpuctf{1234-5678-9012-3456-7890}"
strlist = "1234-5678-9012-3456-7890".split("-")
"""[+] Dump 0x19FE64 - 0x19FE88 (37 bytes) :
[0x08, 0xEA, 0x58, 0xDE, 0x94, 0xD0, 0x3B, 0xBE, 0x88, 0xD4, 0x32, 0xB6, 0x14, 0x82, 0xB7, 0xAF, 0x14, 0x54, 0x7F, 0xCF, 0x20, 0x20, 0x30, 0x33, 0x22, 0x33, 0x20, 0x20, 0x20, 0x30, 0x20, 0x32, 0x30, 0x33, 0x22, 0x20, 0x20]
"""
#转化成下面的格式
t1 = [0xde58ea08,0xbe3bd094,0xb632d488,0xafb78214,0xcf7f5414]
t2 = [[0x20,0x20,0x30,0x33],[0x22,0x33,0x20,0x20],[0x20,0x30,0x20,0x32],[0x30,0x33,0x22,0x20],[0x20,0x20,0x24,0x20]]
#猜测5部分flag的每一部分是由小写字母和数值组成！
table = string.ascii_lowercase + string.digits

res = [0]*5
#开始爆破
for i1 in table:
    for i2 in table:
        for i3 in table:
            for i4 in table:
                a1 = SN(i1+i2+i3+i4)
                a1.datainit()
                v15,v15_l = encode2(a1)
                if v15 in t1:
                    idx = t1.index(v15)
                    if v15_l == t2[idx]:
                        print(i1+i2+i3+i4)
                        res[idx] = i1+i2+i3+i4
print("flag{"+res[0]+"-"+res[1]+"-"+res[2]+"-"+res[3]+"-"+res[4]+"}")

