# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from binascii import *
import hashlib
import libnum
from Crypto.Util.number import *
enc = [189, 173, 180, 132, 16, 99, 179, 225, 198, 132, 45, 111, 186, 136, 116, 196, 144, 50, 234, 46, 198, 40, 101, 112, 201, 117, 120, 160, 11, 159, 166]

for j in range(256):
    a = [j]
    for i in range(31):
        a.append(((enc[i] ^ ((a[i]^0x13)*2+7))-(a[i]%9)-2)&0xff)
    # s = "".join(map(chr,a))
    if a[31]==0xc4:
        print(a)

flag = [0x4d,0x77,0x5e,0x0f,0xb3,0x4d,0x99,0xa6,0x8a,0xfa,0x54,0xb3,0x1e,0x96,0x91,0x7c,0x18,0x85,0xf8,0x30,0x5e,0x61,0xba,0x34,0x1c,0xe9,0x84,0x45,0x0b,0x38,0xbe,0xc4]
for i in xrange(len(flag)-1,-1,-1):
	for j in xrange(i//4-1,-1,-1):
		flag[i]^=flag[j]
print flag
flag = [77, 119, 94, 15, 254, 0, 212, 235, 176, 192, 110, 137, 122, 242, 245, 24, 115, 238, 147, 91, 134, 185, 98, 236, 137, 124, 17, 208, 7, 52, 178, 200]

c1 = b'\x4d\x77\x5e\x0f\xfe\x00\xd4\xeb\xb0\xc0\x6e\x89\x7a\xf2\xf5\x18'
c2 = b'\x73\xee\x93\x5b\x86\xb9\x62\xec\x89\x7c\x11\xd0\x07\x34\xb2\xc8'

des_crypto = b'\x0a\xf4\xee\xc8\x42\x8a\x9b\xdb\xa2\x26\x6f\xee\xee\xe0\xd8\xa2'
#将密文放进去内存，然后改下1为0获得输入key=th1s1sth3n1c3k3y
aes_key = b"th1s1sth3n1c3k3y"
def aes_decrypt(cipher, key=aes_key):
    aes = AES.new(key,mode=AES.MODE_ECB)
    return aes.decrypt(cipher)

print aes_decrypt(c1)+aes_decrypt(c2)

