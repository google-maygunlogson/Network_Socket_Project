import socket
import sys

print('proxy listening')

cache_map = {}

def send_req_to_server(req):
    print('req sent:', req)

    s = socket.socket()
    port  = 54321
    addr = '127.0.0.1'
    s.connect((addr,port))
    s.sendall(req.encode('utf-8'))
    
    res = str(s.recv(1024))
    res = res[2:-1]
    print("res:", res)
    return res

# send_req_to_server('POST:K:V')

#socket listening to client
s = socket.socket()
port = 12345
addr = '127.0.0.1'
s.bind((addr,port))
s.listen(5)

while True:
    c, addr = s.accept()
    
    req = c.recv(1024).decode('ascii')

    req = req.split(':')

    print(req)

    #if post then send to server
    if req[0] == 'POST':
        send_req_to_server( ':'.join(req) )
        c.send(b'post received')

    #if get then 
    elif req[0] == 'GET':
        #if key in cache map then return value
        if req[1] in cache_map:
            print('responding from cache')
            c.send( cache_map[req[1]].encode('utf-8') )
        #else request from server then send to client
        else:
            res = send_req_to_server( ':'.join(req) )
            cache_map[ req[1] ] = str(res)
            c.send( cache_map[req[1]].encode('utf-8') )
            print('cached new get res. cache_map:',cache_map)

    # #if dump then req from server 
    # #and cache everything
    elif req[0] == 'DUMP':
        res = send_req_to_server( ':'.join(req) )
        c.send(res.encode('utf-8'))

    c.close()