# coding=utf-8
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver


# Mode line callback function dataReceived tidak bisa digunakan
class EchoServer(LineReceiver):
    first_line = True
    method = ''
    content = ''

    # Dipanggil ketika koneksi berhasil dibuat
    def connectionMade(self):
        print "Koneksi berhasil di buat"

    def lineReceived(self, line):
        print line

        if self.first_line:
            parse_data = line.split(' ')
            self.method = parse_data[0]
            self.first_line = False

        else:
            # Baca content length
            parse_data = line.split(':')
            if parse_data[0] == "Content-Length":
                self.content_length = int(parse_data[1])

        if not line:
            self.first_line = True
            if self.method == 'GET':
                body = "Hello Word"
                self.send_response(body)
            elif self.method == 'POST':
                self.setRawMode()

    def rawDataReceived(self, data):
        self.content = self.content + data

        if len(self.content) >= self.content_length:
            self.setLineMode()
            # Kirim respon
            self.send_response("Anda mengirimkan data " + self.content)
            self.content = ''

    def send_response(self, body):
        c_length = len(body)
        self.transport.write("HTTP/1.0 200 OK\r\n")
        self.transport.write("Content-Length: " + str(c_length) + "\r\n")
        self.transport.write("\r\n")
        self.transport.write(body)


# Definisi class factory
class EchoFactory(Factory):
    # Callback func ketika client baru terhubung
    def buildProtocol(self, address):
        return EchoServer()


reactor.listenTCP(7887, EchoFactory())
reactor.run()
