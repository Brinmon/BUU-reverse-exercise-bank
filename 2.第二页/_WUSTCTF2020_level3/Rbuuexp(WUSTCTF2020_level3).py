import base64
import string
 
flag = 'd2G0ZjLwHjS7DmOzZAY0X2lzX3CoZV9zdNOydO9vZl9yZXZlcnGlfD=='
base64_table =list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
v0=''

i=0
for i in range(10):
     v0 = base64_table[i]
     base64_table[i] = base64_table[19 - i]
     result = 19 - i
     base64_table[result] = v0
     
base64_table=''.join(base64_table)

string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

print(base64.b64decode(flag.translate(str.maketrans(base64_table,string2))))


