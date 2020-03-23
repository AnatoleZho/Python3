
#!/usr/bin/venv python3

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567

class TSClntProtocal(protocol.Protocol):
    def sendData(self):
        data = input('>')
        if data:
            print('sending %s...', data)
            self.transport.write(data.encode())
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data)
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocal
    clientCOnnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()


reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
