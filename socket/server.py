import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
print (socket.gethostname())
#port number can be anything between 0-65535(we usually specify non-previleged ports which are > 1023)
s.listen(5)

while True:
    clt,adr=s.accept()
    print("Connection to established")
   #f string is literal string prefixed with f which
   #contains python expressions inside braces
    #to send info to clientsocket
    clt.send(bytes("Socket Programming in Python","utf-8 "))

