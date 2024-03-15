byte_402000 = '~}|{zyxwvutsrqponmlkjihgfedcba`_^]\[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9876543210/.-,+*)(\'&%$# !"'

v4 = [42,70,39,34,78,44,34,40,73,63,43,64]

flag = ''

for i in v4:
    flag += chr(byte_402000.find(chr(i)) + 1)

print(flag)