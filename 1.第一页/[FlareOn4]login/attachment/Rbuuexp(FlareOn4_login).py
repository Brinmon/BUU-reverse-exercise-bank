a='PyvragFvqrYbtvafNerRnfl@syner-ba.pbz'
flag=''
for i in a:
    if i >='A' and i<='M':
        flag += chr(ord(i)+13)
    elif i >='a' and i<='m':
        flag += chr(ord(i)+13)
    elif i>='N' and i<="Z":
        flag+=chr(ord(i)-13)
    elif i>='n' and i<='z':
        flag+=chr(ord(i)-13)
    else:
        flag+=i
print(flag)

