import socket
url = 'localhost'
BUFFSIZE = 1024

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((url,8080))
print(s.recv(BUFFSIZE))
s.send('Hello! This is from client!'.encode(encoding='utf_8', errors='strict'))
s.close()
