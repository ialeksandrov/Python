#!/usr/bin/python3
import socket


servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9000

servsock.bind((host, port))

servsock.listen(5)

while True:
    clientsocket,addr = servsock.accept()
    print("Got a Connection from %s" % str(addr))

    msg = "Thank you for connecting" + "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
