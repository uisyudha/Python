from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

kata = ["tuti", "wardani", "hamid"]
# Defisikan class protocol
class EchoServer(Protocol):
    def connectionMade(self):
        print "Koneksi berhasil dibuat"

    def connectionLost(self, reason):
        print "Koneksi terputus"

    def dataReceived(self, data):
        print data
        if data in kata:
            data = "****"

        self.transport.write(data)

# Defisinikan class Factory
class EchoFactory(Factory):
    def buildProtocol(self, addr):
        return EchoServer()


reactor.listenTCP(7887, EchoFactory())
reactor.run()