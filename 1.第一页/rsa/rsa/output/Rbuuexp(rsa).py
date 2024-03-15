import gmpy2 
import rsa 
 
e = 65537
n = 86934482296048119190666062003494800588905656017203025617216654058378322103517
p = 285960468890451637935629440372639283459
q = 304008741604601924494328155975272418463

phin = (q-1)*(p-1)

d = gmpy2.invert(e, phin)

key = rsa.PrivateKey(n, e, int(d), p, q)

with open("D:\\桌面\\Rverse\\BUU刷题\\第一页\\rsa\\rsa\\output\\flag.txt", "rb+") as f:
    f = f.read()
    print(rsa.decrypt(f, key))
