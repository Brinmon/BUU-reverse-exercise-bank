v5 = [0]*6
v5[0] = 1;
v5[1] = 5;
v5[2] = 4;
v5[3] = 2;
v5[4] = 3;
v5[5] = 0;
xor_list = []
for k in range(0x12):
    xor_list.append(int(6 * (k // 6) + v5[k % 6]))
key1 = list("jZekqArhU|9g>0O}|dE@")
xor_result = [0]*0x12
for i in range(0x12):
    xor_result[xor_list[i]] = ord(key1[i])^xor_list[i]
for i in range(0x12):
    print(chr(xor_result[i]),end="")


aOuAO =[  0x87, 0xA0, 0xA8, 0xAD, 0xA4, 0xA5, 0xE1, 0xB5, 0xAE, 0xE1, 
  0xA2, 0xA9, 0xA4, 0xA2, 0xAA, 0xE1, 0xB2, 0xA8, 0xA6, 0xAF, 
  0xE0, 0xC1, 0x00]

for i in range(len(aOuAO)):
    print(chr(aOuAO[i]^0xc1),end="")