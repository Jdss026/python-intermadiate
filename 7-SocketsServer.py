"""
OSCI Model: Transport Layer: UDP & TCP
Sockets: Internet(socket.AF_INET) or Unix
Protocol: TCP(Connection Oriented, socket.SOCK_DGRAM) or UDP(Faster, socket.SOCK_STREAM)
Ports: Not commonly used
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 5555)) #Host the socket will run
s.listen()

while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    client.send("You are connected!".encode())
    client.close()
