#!/usr/bin/env python

import socket
import base64
import os


TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024
file="pic.jpg"

bytesl=open(file,'rb').read()
bytesl=base64.b64encode(bytesl)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytesl)
data = s.recv(BUFFER_SIZE)
s.close()

print data
