from pwn import *

a = []
b = []
a.append(166163712 // 1629056)
a.append(731332800 // 6771600)
a.append(357245568 // 3682944)
a.append(1074393000 // 10431000)
a.append(489211344 // 3977328)
a.append(518971936 // 5138336)
#第六个需要
b.append(406741500 // 7532250)
b.append(294236496 // 5551632)
b.append(177305856 // 3409728)
b.append(650683500 // 13013670)
b.append(298351053 // 6088797)
b.append(386348487 // 7884663)
b.append(438258597 // 8944053)
b.append(249527520 // 5198490)
b.append(445362764 // 4544518)
b.append(981182160 // 10115280)
b.append(174988800 // 3645600)
b.append(493042704 // 9667504)
b.append(257493600 // 5364450)
b.append(767478780 // 13464540)
b.append(312840624 // 5488432)
b.append(1404511500 // 14479500)
b.append(316139670 // 6451830)
b.append(619005024 // 6252576)
b.append(372641472 // 7763364)
b.append(373693320 // 7327320)
b.append(498266640 // 8741520)
b.append(452465676 // 8871876)
b.append(208422720 // 4086720)
b.append(515592000 // 9374400)
b.append(719890500 // 5759124)

flag1 = ""
for i in a:
    flag1 = flag1 + chr(i)
print(flag1)
flag3 = ""
for i in b:
    flag3 = flag3 + chr(i)
print(flag3)
flag2=""

for x in range(4):
    tar = flag1 + str(x) + flag3
    sh = process('./re')
    log.info('current low byte:{}'.format(x))
    sh.sendline(tar)
    temp=(sh.recv(25))
    print(temp)
    if(temp==b'input your flag:Correct!\n'):
        print(tar)
        sh.interactive()
        break
    else:
    	continue


