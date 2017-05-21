from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver

# Mode line callback function dataReceived tidak bisa digunakan
class EchoServer(LineReceiver):
    first_line = True
    # Dipanggil ketika koneksi berhasil dibuat
    def connectionMade(self):
        print "Koneksi berhasil di buat"

    def lineReceived(self, line):
        if self.first_line:
            parsed_data = line.split(' ')
            self.method = parsed_data[0]
            self.url = parsed_data[1]
            self.first_line = False
        else:
            parsed_data = line.split(':')
            if parsed_data[0] == 'Content-Lenght':
                self.content_length = parsed_data[1]

        if not line:
            if self.method == 'GET':
                if self.url == '/':
                    body = 'Halaman Utama'
                    status = 'HTTP/1.0 200 OK\r\n'
                    self.send_response(status, body)
                elif self.url == '/about':
                    status = 'HTTP/1.0 200 OK\r\n'
                    self.send_response(status, body)
                else:
                    body = '404 Not Found'
                    status = 'HTTP/1.0 404 Not Found\r\n'
                    self.send_response(status, body)

            elif self.method == 'POST':
                pass

    def send_response(self, status, body):
        content_length = len(body)
        self.transport.write(status)
        self.transport.write('Content-Length: ' + str(content_length) + '\r\n')
        self.transport.write('\r\n')
        self.transport.write(body)

        # Kirim balik ke client
        ##self.transport.write(data)


# Definisi class factory
class EchoFactory(Factory):
    # Callback func ketika client baru terhubung
    def buildProtocol(self, address):
        return EchoServer()


reactor.listenTCP(7887, EchoFactory())
reactor.run()
