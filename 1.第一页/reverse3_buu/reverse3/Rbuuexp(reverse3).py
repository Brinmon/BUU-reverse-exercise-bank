from base64 import *
key = "e3nifIH9b_C@n@dH"#明文

flag = ""
for k in range(0,len(key)):#进行逆运算解决字符与位序相加
    x = ord(key[k]) - k
    flag = flag + chr(x)
print(b64decode(flag))#使用base64解密，即可输出flag
