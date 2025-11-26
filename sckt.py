import socket
s = socket.socket()
s.bind(("localhost",9999))
s.listen(3)
print("server started")
while True:
    c,addr = s.accept()
    print("connected to ",addr)
    c.send(b"welcome to server")
    c.close()   