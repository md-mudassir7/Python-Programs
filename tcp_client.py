import socket
from datetime import datetime

host='192.168.194.1'
port=7000
max_size=1024

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

print('Starting the Client At ',datetime.now())

while True:
    msg=input('Enter the message to server : ')
    msg_encode=msg.encode()
    s.send(msg_encode)
    if msg=='q':
        break
    c_data=s.recv(max_size)
    if c_data.decode()=='q':
        break
    print('At ',datetime.now(),' Server replied ',c_data.decode())
    
