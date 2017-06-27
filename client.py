#!/usr/bin/python3
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9000

sock.connect((host, port))
msg = sock.recv(1024)

sock.close()
print(msg.decode('ascii'))
