#!/usr/bin/env python

import socket
import base64
import os


TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024000  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
os.mkdir('image_from_client')
myfile=open('image_from_client/recv_pic.jpg','wb')
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    data = base64.b64decode(data)
    myfile.write(data)
    conn.send("recieve done!")  # echo
conn.close()
