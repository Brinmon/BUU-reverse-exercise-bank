flag='GXY{do_not_'
f2=[0x69,0x63,0x75,0x67,0x60,0x6f,0x66,0x7f,0]
v1=[]
for i in range(8):
    if i%2==1:
        v1.append(f2[i]+i-2)
    else:
        v1.append(f2[i]+i-1)
    f2[i]=v1[i]-i
    flag+=chr(f2[i])
print(flag)
