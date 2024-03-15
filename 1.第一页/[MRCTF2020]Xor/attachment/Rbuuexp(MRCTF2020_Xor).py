from binascii import *

flag = ''
flag += chr(0x4d ^ 0)

key = 'SAWB~FXZ:J:`tQJ"N@ bpdd}8g'
key = b2a_hex(key.encode()).decode()
for i in range(len(key)//2):
    flag += chr(int(key[i*2:(i+1)*2],16)^(i+1))
print(flag)
