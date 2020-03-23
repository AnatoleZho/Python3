from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567
class TSServProtocal(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected fromL', clnt)

    def dataReceived(self, data):
        print(data);
        self.transport.write(('[{}] {}'.format(ctime(), data.decode())).encode())

factory = protocol.Factory()
factory.protocol = TSServProtocal

print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()



