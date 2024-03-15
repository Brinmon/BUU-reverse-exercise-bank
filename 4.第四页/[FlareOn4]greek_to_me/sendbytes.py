import sys
import os
import socket
ip = '127.0.0.1'
port = 2222
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send(bytes([0xa2]))
print(bytes([0xa2]))
s.close()