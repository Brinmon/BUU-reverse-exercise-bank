 
 
def fun1():
    opcode=[9,4,4,9,0,0,8,1,0,8,2,1,8,3,2,6,1,4,5,1,0x15,7,0,1,4,0,3,1,0x6b,0xcc,0x7e,0x1d,8,1,3,4,0,1,2,0xa,4,0,9,0,0,8,1,0,8,2,1,8,3,2,6,3,8,5,3,3,7,0,3,3,0,2,1,0x7c,0x79,0x79,0x60,8,1,3,4,0,1,2,10,4,0,9,0,0,8,1,0,8,2,1,8,3,2,6,1,8,7,0,1,3,0,2,1,0xbd,0xbd,0xbc,0x5f,8,1,3,4,0,1,2,10,4,0,0]
    cnt1=2
    i=0
    for a in range(len(opcode)):
        if opcode[i]==0:
            print("over")
            break
        elif opcode[i]== 1:
            temp=(opcode[i+1])|(opcode[i+2]<<8)|(opcode[i+3]<<16)|(opcode[i+4]<<24)
            i+=5
            cnt1 += 1
            print("mov outnum[",cnt1,"] ",hex(temp))
        elif opcode[i] ==2:
            cnt1-=1
            print("sub cnt1 1")
            i+=1
        elif opcode[i] ==3:
            print("add elx[",opcode[i+1],"] elx[",opcode[i+2],"]")
            i += 3
        elif opcode[i] ==4:
            print("sub elx[", opcode[i + 1], "] elx[", opcode[i + 2], "]")
            i += 3
        elif opcode[i] ==5:
            print("mul elx[",opcode[i+1],"] " ,opcode[i + 2])
            i += 3
        elif opcode[i] ==6:
            print("ROR  elx[",opcode[i+1],"] ", opcode[i + 2])
            i += 3
        elif opcode[i] ==7:
            print("mov elx[", opcode[i + 1], "] elx[", opcode[i + 2], "]")
            i+=3
        elif opcode[i] ==8:
            print("mov elx[", opcode[i+1], "] outnum[", opcode[i + 2], "]")
            i += 3
        elif opcode[i] ==9:
            print("xor elx[", opcode[i + 1], "] elx[", opcode[i + 2], "]")
            i += 3
        elif opcode[i] ==10:
            print("or elx[", opcode[i + 1], "] elx[", opcode[i + 2], "]")
            i += 3
 
  
from z3 import*
s=Solver()
num1=BitVec('num1',32)
num2=BitVec('num2',32)
num3=BitVec('num3',32)
s.add((((num1>>4)*21-num3-0x1d7ecc6b)|((num3>>8)*3+num2-0x6079797c)|((num1>>8)+num2-0x5fbcbdbd))==0)
s.add(num1&0xff==0x5e)
s.add(num3&0xff==0x5e)
s.add((num2 & 0xFF0000) == 0x5E0000)
print(s.check())
answer=s.model()
print(answer)
#[num2 = 1600020063, num3 = 1583243102, num1 = 1583308382]
aa=[1583308382,1600020063,1583243102]
flag="flag{"
for i in range(len(aa)):
    flag += hex(aa[i])[2:]
flag+="}"
print(flag)
# def encode_400806(ptr,First_6024CC,Second_6024C0,Third_6024C8):
#     data1_6020A0 = [0] * 10
#     target_6024A0 = [0] * 20
#     data1_6020A0[0] = First_6024CC
#     data1_6020A0[1] = Second_6024C0
#     data1_6020A0[2] = Third_6024C8
#     dword_6024BC = 0
#     idx1_6024B8 = 2
#     idx_6024B4 = 0
#     v5 = 1
#     while v5:
#         opcode = ptr[idx_6024B4]
#         if opcode == 0:
#             v5 = 0
#         elif opcode == 1:
#             data1_6020A0[idx1_6024B8] = (ptr[idx_6024B4 + 4] << 24) + (ptr[idx_6024B4 + 3] << 16) + (ptr[idx_6024B4 + 2] << 8) + ptr[idx_6024B4 + 1]
#             idx1_6024B8 += 5
#             print("data1_6020A0[",idx1_6024B8,"]")
#         elif opcode == 2:
#             idx1_6024B8 -= 1
#         elif opcode == 3:
#             target_6024A0[ptr[idx_6024B4 + 1]] += target_6024A0[ptr[idx_6024B4 + 2]]
#             idx_6024B4 += 2
#         elif opcode == 4:
#             target_6024A0[ptr[idx_6024B4 + 1]] -= target_6024A0[ptr[idx_6024B4 + 2]]
#             idx_6024B4 += 2
#         elif opcode == 5:
#             target_6024A0[ptr[idx_6024B4 + 1]] *= ptr[idx_6024B4 + 2]
#             idx_6024B4 += 2
#         elif opcode == 6:
#             target_6024A0[ptr[idx_6024B4 + 1]] = target_6024A0[v9] >> ptr[idx_6024B4 + 2]
#             idx_6024B4 += 2
#         elif opcode == 7:
#             target_6024A0[ptr[idx_6024B4 + 1]] = target_6024A0[ptr[idx_6024B4 + 2]]
#             idx_6024B4 += 2
#         elif opcode == 8:
#             target_6024A0[ptr[idx_6024B4 + 1]] = data1_6020A0[dword_6024BC + ptr[idx_6024B4 + 2]]
#             idx_6024B4 += 2
#         elif opcode == 9:
#             target_6024A0[ptr[idx_6024B4 + 1]] ^= target_6024A0[ptr[idx_6024B4 + 2]]
#             idx_6024B4 += 2
#         elif opcode == 10:
#             target_6024A0[ptr[idx_6024B4 + 1]] |= target_6024A0[ptr[idx_6024B4 + 2]]
#             idx_6024B4 += 2
#         else:
#             print(f"Invalid opcode. {opcode}")
#             exit(1)
#         idx_6024B4 += 1
#     return idx_6024B4

# opcode=[9,4,4,9,0,0,8,1,0,8,2,1,8,3,2,6,1,4,5,1,0x15,7,0,1,4,0,3,1,0x6b,0xcc,0x7e,0x1d,8,1,3,4,0,1,2,0xa,4,0,9,0,0,8,1,0,8,2,1,8,3,2,6,3,8,5,3,3,7,0,3,3,0,2,1,0x7c,0x79,0x79,0x60,8,1,3,4,0,1,2,10,4,0,9,0,0,8,1,0,8,2,1,8,3,2,6,1,8,7,0,1,3,0,2,1,0xbd,0xbd,0xbc,0x5f,8,1,3,4,0,1,2,10,4,0,0]
# First_6024CC = 1234
# Second_6024C0 = 456
# Third_6024C8 = 789
# encode_400806(opcode,First_6024CC,Second_6024C0,Third_6024C8)