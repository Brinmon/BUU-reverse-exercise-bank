_global = ['f',0xA,'k',0xC,'w','&','O','.','@',0x11,'x',0xD,'Z',';','U',0x11,'p',0x19,'F',0x1F,'v','"','M','#','D',0xE,'g',6,'h',0xF,'G','2','O']
#首先将global转化为可见字符串
for i in range(0,len(_global)):
    if(isinstance(_global[i],int)):#将数字转化为字符
        _global[i] = chr(_global[i])

flag='f'
for i in range(1,len(_global)):
    flag += chr( ord(_global[i]) ^ ord(_global[i-1]) )#a^b=c 等于 a^c=b
#ord()返回字符串对应的ASCII码，chr()返回数值对应的字符
print(flag)