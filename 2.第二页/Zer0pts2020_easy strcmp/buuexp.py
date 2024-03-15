import binascii

str1 = "zer0pts{********CENSORED********}"
qword_201060 = [0,0x410A4335494A0942, 0x0B0EF2F50BE619F0, 0x4F0A3A064A35282B]

flag = b''
for i in range(4):  #3的话是因为24/8=3---->********CENSORED********
    z = str1[i * 8 : (i + 1) * 8]                           #分成四份,也就是八个一组
    x = binascii.b2a_hex(z.encode('ascii')[::-1])            #将里面的元素转换为16进制的ascii,由于是小端序所以需要将数据倒置
    y = binascii.a2b_hex(hex(int(x, 16) + qword_201060[i])[2:])[::-1]   #与201060的元素相加，[2:]是将数据中的0x去除
    flag += y
print(flag + b'}')