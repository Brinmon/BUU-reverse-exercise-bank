input = [  0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 
  0x61, 0x61, 0x61, 0x61, 0x61, 0x61]
  
resultkey = [  0x2C, 0x2D, 0x26, 0x31, 0x2E, 0x2A, 0x27, 0x22, 0x2B, 0x24, 
  0x2F, 0x28, 0x29, 0x25, 0x23, 0x20]

xorkey = []

for i in range(len(input)):
    xorkey.append(input[i]^resultkey[i])
# print(xorkey) #[77, 76, 71, 80, 79, 75, 70, 67, 74, 69, 78, 73, 72, 68, 66, 65]

flag = [  0x17, 0x63, 0x77, 0x03, 0x52, 0x2E, 0x4A, 0x28, 0x52, 0x1B, 
  0x17, 0x12, 0x3A, 0x0A, 0x6C, 0x62, 0x00] 


def funaddnum(a1: int, a2: int):
    flag[a1] -= a2


def funxoridxandidx(a1: int, a2: int):
    flag[a1] ^= flag[a2]


def funsubinputa1andinputa2(a1: int, a2: int):
    if flag[a1] < flag[a2]:
        # 如果flag[a1]<flag[a2]则原来的flag[a1]-flag[a2]是负数，所以需要取负
        flag[a1] = -flag[a1]
    flag[a1] += flag[a2]


commands = '''
funaddnum(0, 10)
funxoridxandidx(1, 2)
funaddnum(2, 7)
funsubinputa1andinputa2(3, 7)
funxoridxandidx(4, 5)
funsubinputa1andinputa2(6, 1)
funaddnum(7, 3)
funxoridxandidx(8, 7)
funsubinputa1andinputa2(9, 8)
funsubinputa1andinputa2(10, 7)
funxoridxandidx(11, 12)
funsubinputa1andinputa2(12, 2)
funxoridxandidx(14, 15)
funaddnum(15, 2)
'''.split('\n')
commands = commands[::-1]
for command in commands:
    if len(command) < 5:
        continue
    eval(command)


for index, i in enumerate(xorkey):
    flag[index] ^= (xorkey[index])

flag = [chr(x) for x in flag]
flag = ''.join(flag)
print(flag)  # @_7r3e_f0r_fuNN!

