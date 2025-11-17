#!/usr/bin/env python3
# open a tcp connection and send a string
# you will need a tcpserver.py running first
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 8008
BUF_SIZE = 1024
MESSAGE = b'hi everyone'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUF_SIZE)
s.close()

print("received: ", data)
