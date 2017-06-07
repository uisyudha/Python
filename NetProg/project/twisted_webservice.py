from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.internet import reactor
import json
import websocket

# Protocol untuk handle HTTP
class WebService(Resource):
    isLeaf = True

    # Fungsi handle POST method CREATE Pegawai
    def render_POST(self, request):
        # Print request
        print request.method, request.path

        # Callback function setelah query dijalankan
        # Fungsi ini dijankan setelah query di eksekusi
        if request.path == "/":
            # Get post data
            topik = request.args['topik'][0]
            pesan = request.args['pesan'][0]
            print topik, pesan
            
            #Buat data yang akan dikirim ke websocket server
            data = {'id': 'pub', 'topik': topik, 'pesan': pesan}
            
            #Encode json
            str_data = json.dumps(data)
            
            # Buat object websocket
            ws = websocket.WebSocket()
            
            # Buat koneksi ke server
            ws.connect("ws://localhost:8877")

            ws.send(str_data)
            return "OK"

        else:
            return "No resource"
            

# Factory
factory = Site(WebService())
reactor.listenTCP(7887, factory)
reactor.run()