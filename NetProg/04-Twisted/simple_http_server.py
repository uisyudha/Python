# coding=utf-8
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver

# Mode line callback function dataReceived tidak bisa digunakan
class EchoServer(LineReceiver):
    first_line = True
    directory = ['/', '/submit', '/about']
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
            #request url
            url_raw = parse_data[1]

            # Split jika ada query parameter
            url_parsed = url_raw.split('?')
            if len(url_parsed) == 2:
                self.path = url_parsed[0]
                self.query = url_parsed[1]
            else:
                self.path = url_parsed[0]

        else:
            # Baca content length
            parse_data = line.split(':')
            if parse_data[0] == "Content-Length":
                self.content_length = int(parse_data[1])

        if not line:
            self.first_line = True
            if self.method == 'GET':
                if self.path not in self.directory:
                    status = "HTTP/1.0 404 Not Found\r\n"
                    body = '<!DOCTYPE html>' \
                               '<html lang=en>' \
                               '<meta charset=utf-8>' \
                               '<meta name=viewport content="initial-scale=1, minimum-scale=1, width=device-width">' \
                               '<title>Error 404 (Not Found)!!1</title>' \
                               '<style>*{margin:0;padding:0}html,code{font:15px/22px arial,sans-serif}html{background:#fff;color:#222;padding:15px}body{margin:7% auto 0;max-width:390px;min-height:180px;padding:30px 0 15px}* > body{background:url(//www.google.com/images/errors/robot.png) 100% 5px no-repeat;padding-right:205px}p{margin:11px 0 22px;overflow:hidden}ins{color:#777;text-decoration:none}a img{border:0}@media screen and (max-width:772px){body{background:none;margin-top:0;max-width:none;padding-right:0}}#logo{background:url(//www.google.com/images/branding/googlelogo/1x/googlelogo_color_150x54dp.png) no-repeat;margin-left:-5px}@media only screen and (min-resolution:192dpi){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat 0% 0%/100% 100%;-moz-border-image:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) 0}}@media only screen and (-webkit-min-device-pixel-ratio:2){#logo{background:url(//www.google.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png) no-repeat;-webkit-background-size:100% 100%}}#logo{display:inline-block;height:54px;width:150px}</style>' \
                               '<p><b>404.</b> <ins>That’s an error.</ins>' \
                               '<p>The requested URL <code>' + self.path +'</code> was not found on this server.  <ins>That’s all we know.</ins>'
                    self.send_response(status, body)
                elif self.path == '/':
                    # Kirim response ke client
                    body = '<!DOCTYPE html>' \
                           '<html>' \
                               '<form action="/submit" method="GET">' \
                                   'Nama : <input type="text" name="nama"><br>' \
                                   'NIM : <input type="text" name="nim"><br>' \
                                   '<button type="submit">GET SUBMIT</button>' \
                                   '<button type="submit" formmethod="POST" formaction="/submit">POST SUBMIT</button>' \
                               '</form>' \
                           '</html>'
                    status = "HTTP/1.0 200 OK\r\n"
                    self.send_response(status, body)
                elif self.path == '/submit':
                    # Parsing query parameter jika ada paramater
                    if hasattr(self, 'query'):
                        params = self.query.split('&')
                        status = "HTTP/1.0 200 OK\r\n"
                        body = ""
                        for i in params:
                            body = body + i + "\n"
                        self.send_response(status,body)
                    # Redirect ke /
                    else:
                        status = "HTTP/1.0 200 OK\r\n"
                        body = '<!DOCTYPE html>' \
                               '<html>' \
                                   '<head>' \
                                       '<meta http-equiv="Refresh" content="5;url=http://localhost:7887">' \
                                   '</head>' \
                                   '<body>' \
                                       '<p> Tidak dapat di akses langsung redirecting in 5 seconds..</p>' \
                                   '</body>' \
                               '</html>'
                        self.send_response(status,body)
                elif self.path == '/about':
                    status = "HTTP/1.0 200 OK\r\n"
                    body = "Twisted Simple HTTP Server"
                    self.send_response(status,body)
            elif self.method == 'POST':
                self.setRawMode()

    def rawDataReceived(self, data):
        self.content = self.content + data

        if len(self.content) >= self.content_length:
            self.setRawMode()
            status = "HTTP/1.0 200 OK\r\n"
            body = "Anda mengirmkan data : " + self.content
            self.send_response(status,body)
            self.content = ''

    def send_response(self, status, body):
        c_length = len(body)
        self.transport.write(status)
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
