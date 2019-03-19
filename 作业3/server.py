import socket
import threading
import time
BUFFSIZE = 1024
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send('Welcome!'.encode(encoding='utf_8', errors='strict'))
    print(sock.recv(BUFFSIZE))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8080))
s.listen(5)
print('Waiting for connection')
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
