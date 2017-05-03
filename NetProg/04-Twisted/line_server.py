from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver

# Mode line callback function dataReceived tidak bisa digunakan
class EchoServer(LineReceiver):
    # Dipanggil ketika koneksi berhasil dibuat
    def connectionMade(self):
        print "Koneksi berhasil di buat"

    def lineReceived(self, data):
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
