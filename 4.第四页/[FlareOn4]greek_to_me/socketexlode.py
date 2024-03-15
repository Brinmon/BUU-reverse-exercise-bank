import sys
import os
import socket

ip = '127.0.0.1'
port = 2222
for i in range(255):
    os.startfile(r"D:\CTF_Study\Reverse\BUU\4.第四页\[FlareOn4]greek_to_me\greek_to_me.exe")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(bytes([i]))
    
    data = s.recv(1024)
    s.close()
    print("发送的数据：",bytes([i]))
    print("收到的数据：",data)
    if 'Congratulations'.encode() in data:
        print("%x" % i)
        break