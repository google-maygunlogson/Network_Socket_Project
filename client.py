import socket

def send_get(s, key):
    req = 'GET:'+key
    s.sendall(req.encode('utf-8'))
    print(s.recv(1024))
def send_post(s, key, value):
    req = 'POST:' + key + ":" + value
    s.sendall(req.encode('utf-8'))
    print(s.recv(1024))
def send_dump(s):
    req = "DUMP"
    s.sendall(req.encode('utf-8'))
    print(s.recv(1024))



#FUNCTIONS
def handle_operations():
    while True:
        s = socket.socket()

        port = 12345

        s.connect(('127.0.0.1', port)) 

        cmd = input("GET key, POST key value, DUMP, or Q (quit) ")
        cmd = cmd.split(' ')
        op = cmd.pop(0)
        if op.upper() == "GET":
            key = cmd.pop(0)
            send_get(s,key)
        elif op.upper() == "POST":
            key = cmd.pop(0)
            value = ''.join(cmd)
            send_post(s, key, value)
        elif op.upper() == "DUMP":
            send_dump(s)
        elif op.upper() == 'Q':
            print('Q')
            break
        else:
            print('Invalid response. Try again.')
        
        s.close()

handle_operations()

