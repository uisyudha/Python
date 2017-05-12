from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor


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


reactor.listenTCP(7887, EchoFactory())
reactor.run()
