str=[180, 136, 137, 147, 191, 137, 147, 191,148, 136, 133, 191, 134, 140, 129, 135, 191, 65]#密钥

flag = ""
for i in range(0,len(str)):
	flag += chr(str[i] - 64 ^ 0x20)
print(flag)

