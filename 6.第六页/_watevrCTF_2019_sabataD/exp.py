def sub_558C0AE00AEA(a1):
    if a1 > 96 and a1 <= 122:
        return sub_558C0AE00B3E(a1, 97)
    if a1 <= 64 or a1 > 90:
        return a1
    return sub_558C0AE00B3E(a1, 65)

def sub_558C0AE00B3E(a1, a2):
    return (a2 + (a1 - a2 + 13) % 26)

target =""
s1 = "Fetch from file with index"
s2 = "watevr-admin"
pattern = "/home/ctf////flag.txt"
s1list = list(s1)
idx1 = 0
s2list = list(s2)
idx2 = 0
patternlist = list(pattern)
idx3 = 0
print("被加密前的文本：",end="")
for i in range(151):
    if i%3 == 0:
        if(idx1<len(s1list)):
            print(s1list[idx1],end="")
            target +=s1list[idx1]
            idx1 +=1
        else:
            target +="_"
            print("_",end="")
    if i%3 == 1:
        if(idx2<len(s2list)):
            print(s2list[idx2],end="")
            target +=s2list[idx2]
            idx2 +=1
        else:
            target +="_"
            print("_",end="")
    if i%3 == 2:
        if(idx3<len(patternlist)):
            print(patternlist[idx3],end="")
            target +=patternlist[idx3]
            idx3 +=1
        else:
            target +="_"
            print("_",end="")
target += "256"
print("")

tarlist = list(set(target))
tag = [0]*40
my_dict ={}
for i in range(255):
    tmp = chr(sub_558C0AE00AEA(i))
    # print(tmp)
    if tmp in tarlist: #检查输出和我们的输入并且记录到字典！
        idx1 = tarlist.index(tmp)
        if(not tag[idx1]):
            my_dict.update({tmp: i})
        tag[idx1] = 1
print("生成的字典：",my_dict)
print("生成的密钥:",end="")
for ch in target:
    print(chr(my_dict[ch]),end="")
