import socket
import sys

print('proxy listening')

s = socket.socket()
port = 12345
addr = '127.0.0.1'
s.bind((addr,port))
s.listen(5)

while True:
    c, addr = s.accept()
    
    req = c.recv(1024).decode('ascii')

    #here is where you'd split req

    print(req)

    c.close()