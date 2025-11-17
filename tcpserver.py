#!/usr/bin/env python3
# listen for a tcp connection and echo back once if we get anything
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 8008
BUF_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print("connection from:",addr)
while True:
    data = conn.recv(BUF_SIZE)
    if not data: break
    print("received data:",data)
    conn.send(data)
conn.close()
print("closed connection")
