ptr = [198,232,816,200,1536,300,6144,984,51200,570,92160,1200,565248,756,1474560,800,6291456,1782,65536000]

for i in range(19):
    if ((i+1) & 1):#初始i为0，源程序i为1
        print(chr(ptr[i] >> (i+1)),end="")
    else:
        print (chr(ptr[i] // (i+1)),end="")


