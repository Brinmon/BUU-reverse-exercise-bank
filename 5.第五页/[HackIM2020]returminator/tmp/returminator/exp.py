from z3 import *
 
r = [208, 225, 237, 20, 214, 183, 79, 105, 207, 217, 
     125, 66, 123, 104, 97, 99, 107 , 105, 109, 50, 
     48, 202, 111, 111, 29, 63, 223, 36, 0, 124, 
     100, 219, 32]
 
f = [Int(f'f_{i}') for i in range(31)]
s = Solver()
for i in range(31):
    s.add([f[i]>0x20, f[i]<0x7f])
    
    
s.add(f[0]+f[2]+f[4] -100 == r[0])
s.add(f[6]+f[8]+f[10] == r[1])
s.add(f[12]+f[14]+f[16] == r[2])
s.add(f[18]+f[1]-f[30] == r[3])
s.add(f[3]+f[22]+f[3]-100 == r[4])
s.add(f[5]+f[29]+f[28]-f[7]-100 == r[5])
s.add(f[9]+f[17]-f[11] == r[6])
s.add(f[13]+f[15]+f[20]-f[19]-f[27] == r[7])
s.add(f[21]+f[23]+f[23] == r[8])
s.add(f[25]+f[26] == r[9])
s.add(f[30] == r[10])
s.add(f[9] == r[11])
s.add(f[8] == r[12])
s.add(f[0] == r[13])
s.add(f[1] == r[14])
s.add(f[2] == r[15])
s.add(f[3] == r[16])
s.add(f[4] == r[17])
s.add(f[5] == r[18])
s.add(f[6] == r[19])
s.add(f[7] == r[20])
s.add(f[11]+f[0] == r[21])
s.add(f[29] == r[22])
s.add(f[29] == r[23])
s.add(f[29]-f[13] == r[24])
s.add(f[28]-f[14] == r[25])
s.add(f[28]+f[15] == r[26])
s.add(f[0]-f[27] == r[27])
s.add(f[23]-f[24] == r[28])
s.add(f[26]+f[0]-f[1] == r[29])
s.add(f[19] == r[30])
s.add(f[11]+f[12] == r[31])
s.add(f[21]-f[20] == r[32])
 
if s.check() == sat:
    d = s.model()
    print(d)
    for i in range(31):
        print(chr(d[f[i]].as_long()), end='')
 
#hackim20{B4byR0pDo0dOod00duDoo}
#flag{B4byR0pDo0dOod00duDoo}