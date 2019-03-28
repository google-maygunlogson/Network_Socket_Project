# ref: https://www.geeksforgeeks.org/socket-programming-python/
import socket
import sys


def handle_post(key, value):
    hashmap[key] = value
    print(hashmap)
def handle_get(key):
    if key in hashmap:
        return hashmap[key]
    return "key doesn't exist"
def handle_dump():
    return str(hashmap)


print("server started")

hashmap = {}

s= socket.socket()


port = 54321

s.bind(('127.0.0.1',port))


s.listen(5)


while True:
    c, addr = s.accept()
    
    req = c.recv(1024).decode('ascii')
    

    req = req.split(':')

    print(req)

    if req[0] == 'POST':
        c.send(b'post received')
        handle_post(req[1],req[2])
    elif req[0] == 'GET':
        res = handle_get(req[1])
        c.send(res.encode('utf-8'))
    elif req[0] == 'DUMP':
        res = handle_dump()
        c.send(res.encode('utf-8'))


    c.close()

