

from socket import *

HOST = 'localhost'
PORT = 21567
BUGSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('>')
    if not data:
        break
    udpCliSock.sendto(data.encode(), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUGSIZ)

    if not data:
        break
    print(data.decode())

udpCliSock.close()