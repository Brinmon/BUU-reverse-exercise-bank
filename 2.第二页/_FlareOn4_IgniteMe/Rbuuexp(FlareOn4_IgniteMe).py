key=[0x0D, 0x26, 0x49, 0x45, 0x2A, 0x17, 0x78, 0x44, 0x2B, 0x6C,0x5D, 0x5E, 0x45, 0x12, 0x2F, 0x17, 0x2B, 0x44, 0x6F, 0x6E,0x56, 0x09, 0x5F, 0x45, 0x47, 0x73, 0x26, 0x0A, 0x0D, 0x13,0x17, 0x48, 0x42, 0x01, 0x40, 0x4D, 0x0C, 0x02, 0x69,0x00]

num=4
flag=[0 for x in range(0,len(key))]
end=len(key)-1
flag[end]=key[end]^num
for n in range(1,end+1):
	flag[end-n]=key[end-n]^flag[end-n+1]

str1=''
for x in range(0,len(key)):
    str1 += chr(flag[x])

print(str1)