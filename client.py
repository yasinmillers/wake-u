import socket

s = socket.socket()
s.connect(("localhost",9999))
msg = s.recv(1024)
print(msg.decode())
s.close()