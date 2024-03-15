key1="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
key2="TOiZiZtOrYaToUwPnToBsOaOapsyS"
flag=""

for i in range(len(key2)):
    if i %2 == 0:
        flag +=key2[i]
        continue
    if(key2[i].isupper()):#是否是大写字母
        flag+=chr(key1.find(key2[i])+96)
    else:
        flag+=chr(key1.find(key2[i])+38)

print(flag)