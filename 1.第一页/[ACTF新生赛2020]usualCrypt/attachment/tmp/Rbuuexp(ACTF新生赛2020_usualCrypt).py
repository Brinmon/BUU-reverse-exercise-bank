import base64
KEY2=list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

for idx in range(6,15):
    temp=KEY2[idx+10]
    KEY2[idx+10]=KEY2[idx]
    KEY2[idx]=temp

new_table = ''.join(str(i) for i in KEY2)
print(new_table)
#输出后：ABCDEFQRSTUVWXYPGHIJKLMNOZabcdefghijklmnopqrstuvwxyz0123456789+/

old_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
target = "zMXHz3TIgnxLxJhFAdtZn2fFk3lYCrtPC2l9"

res = ''#大小写转换
for i in target:
	if 'a' <= i <= 'z':
		tmp = ord(i) - 32
	elif 'A' <= i <= 'Z':
		tmp = ord(i) + 32
	else:
		tmp = ord(i)
	res += chr(tmp)

general = ''
for i in res:
	general += old_table[new_table.find(i)]#进行base64码表等量替换
print(general)
print(base64.b64decode(general))