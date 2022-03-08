import socket
from datetime import datetime

host='192.168.194.1'
port=7000
max_size=1024

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))

print('Starting the server At ',datetime.now())
print('Waiting for incoming client connection ! ')

sock.listen(5)
client,addr=sock.accept()

while True:
    data=client.recv(max_size)
    if data.decode()=='q':
        break
    print('At ',datetime.now(),addr,'said',data.decode())
    message_to_client=input('Enter your message to client : ')
    message_to_client_encoded=message_to_client.encode()
    client.send(message_to_client_encoded)
    if message_to_client=='q':
        break

client.close()
sock.close()
