text ='killshadow'
key='adsfkndcls'
flag1=''
flag2=''
#大写字母 64~90
for i in range(0,len(text)):
	for j in range(65,91):
		if ord(text[i])==(j-39-ord(key[i])+97)%26+97:
			flag1 += chr(j)
# 小写字母 97~122
# for i in range(0,len(text))://之前代码分析错误，后来发现逻辑里小写字母会被直接排除
# 	for j in range(97,123):
# 		if ord(text[i])==(j-39-ord(key[i])+97)%26+97:
# 			flag2 += chr(j)

print("大写的："+flag1)
#print("大写的："+flag1+"\n"+"小写的："+flag2)
