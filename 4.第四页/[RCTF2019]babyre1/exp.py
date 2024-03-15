import xxtea
import hashlib
key = [0xc7,0xe0,0xc7,0xe0,0xd7,0xd3,0xf1,0xc6,0xd3,0xc6,0xd3,0xc6,0xce,0xd2,0xd0,0xc4]
key = "".join(chr(m) for m in key)
text = [0x55,0x7e,0x79,0x70,0x78,0x36,0x0,0x0]
for i in range(0xff):
    for j in range(4):
        text[6] = i
        text[7] = j
        encrypt_data = xxtea.encrypt("".join(chr(n) for n in text),key)
        encrypt_data = encrypt_data.hex()
flag = "rctf{"+ encrypt_data +"}"
hl = hashlib.md5()
hl.update(flag.encode(encoding='utf-8'))
if hl.hexdigest() == '5f8243a662cf71bf31d2b2602638dc1d':
    print("yesyes")
    print(encrypt_data)
 
#rctf{05e8a376e4e0446e}