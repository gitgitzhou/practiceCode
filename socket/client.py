import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostname())
s.connect((socket.gethostname(), 1234))
msg=s.recv(1024)
print(msg.decode("utf-8"))
