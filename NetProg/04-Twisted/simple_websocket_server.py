from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from txws import WebSocketFactory

# Perbadaan ada di factory,
# Definisi class protocol
class EchoServer(Protocol):
    # Dipanggil ketika koneksi berhasil dibuat
    def connectionMade(self):
        print "Koneksi berhasil di buat"

    def dataReceived(self, data):
        print data
        data = "OK " + data
        # Kirim balik ke client
        self.transport.write(data)


# Definisi class factory
class EchoFactory(Factory):
    # Callback func ketika client baru terhubung

    def buildProtocol(self, address):
        return EchoServer()

factory = EchoFactory()
reactor.listenTCP(7887, WebSocketFactory(factory))
reactor.run()
