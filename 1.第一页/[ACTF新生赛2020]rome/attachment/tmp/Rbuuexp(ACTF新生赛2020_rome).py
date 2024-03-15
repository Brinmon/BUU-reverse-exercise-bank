##字节爆破
# v15= [ 'Q','s','w','3','s','j', '_','l','z','4','_','U','j','w','@','l' ]
# flag=""

# for i in range(16):
#     for j in range(128):#ascii表上有127个字符，一个一个试吧
#         x=j
#         if chr(x).isupper():
#             x=(x-51)%26+65
#         if chr(x).islower():
#             x=(x-79)%26+97
#         if chr(x)==v15[i]:
#             flag+=chr(j)

# print ('flag{'+flag+'}')

#逆向算法
v15= [ 'Q','s','w','3','s','j', '_','l','z','4','_','U','j','w','@','l' ]
flag=""
for i in range(16):
    if (ord(v15[i])>64 and ord(v15[i])<91):
        temp=ord(v15[i])-65+51
        if temp<65:
            temp+=26
        flag+=chr(temp)
    elif (ord(v15[i])>96 and ord(v15[i])<123):
        temp=ord(v15[i])-97+79
        if temp<97:
            temp+=26
        flag+=chr(temp)
    else:
        flag+=chr(ord(v15[i]))
print ('flag{'+flag+'}')