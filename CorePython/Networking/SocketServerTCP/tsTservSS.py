#!/usr/bin/venv python3

from socketserver import TCPServer as TCP, StreamRequestHandler as SRH

from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:', self.client_address)
        print(self.rfile.readline().decode())
        self.wfile.write(('[{}] {}'.format(ctime(), self.rfile.readline())).encode())


tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for contection...')
tcpServ.serve_forever()
























