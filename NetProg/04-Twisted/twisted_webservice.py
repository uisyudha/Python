from twisted.web.resource import Resource
from twisted.web.server import Site, NOT_DONE_YET
from twisted.internet import reactor
from twisted.enterprise import adbapi
import json
import urlparse

# Fungsi untuk fetching data dari sqlite dalam bentuk dictionary
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Call function dbpool
def set_dict_factory(conn):
    conn.row_factory = dict_factory

# Inisiasi dbpool dan setup call function ke set_dict_factory
dbpool = adbapi.ConnectionPool("sqlite3", "pegawai.db", check_same_thread=False, cp_openfun=set_dict_factory)

# Protocol untuk handle HTTP
class Pegawai(Resource):
    isLeaf = True

    # Fungsi yang menghandle GET method READ Pegawai
    def render_GET(self, request):
        # Split request path berdasarkan tanda /
        # Jika user request resource /pegawai/1 maka hasil split ['', 'pegawai'. '1']
        resource = request.path.split("/")
        resource_len = len(resource)
        # Print request
        print request.method, request.path

        # Callback function setelah query dijalankan
        # Fungsi ini dijankan setelah query di eksekusi
        def onResult(data):
            # Konversi ke json
            str_data = json.dumps(data)
            # Set response code
            request.setResponseCode(200)
            # Tulis str_data ke body
            request.write(str_data)
            # Request finish
            request.finish()

        # Jika panjang resource == 2, hasil split path berdasarkan / ["", "pegawai"]
        if resource_len == 2:
            if resource[1] == "pegawai":
                # Defisinikan fungsi untuk menjalankan query
                def getPegawai():
                    return dbpool.runQuery("SELECT * FROM PEGAWAI")

                # Panggil fungsi query, dan set callback functionnya
                getPegawai().addCallback(onResult)

            # Resource yang diminta tidak ada
            else:
                status = "Request path or parameter error"
                self.requestError(request, status)

        # Jika panjang resourc kurang dari 3, hasil split path misal ["", "pegawai", "3"]
        elif resource_len <= 3:
            if resource[1] == "pegawai":
                # Cek jika resource indek ke 2 adalah angka
                if self.is_number(resource[2]):
                    # parsing resourc[2] ke integer sebagai id di database pegawai
                    id = int(resource[2])

                    # Fungsi getPegawai id return hasil query
                    def getPegawaiId():
                        return dbpool.runQuery("SELECT * FROM PEGAWAI WHERE ID=?", (id,))

                    # Panggil fungsi getPegawaiId dengan callback function onResult
                    getPegawaiId().addCallback(onResult)

                # Jika resource[1] berisi selain pegawai
                else:
                    status = "Request path or parameter error"
                    self.requestError(request, status)
        else:
            status = "No Resource"
            self.requestError(request, status)

        # Return NOT_DONE_YET agar server tidak berhenti setelah request finish
        return NOT_DONE_YET

    # Fungsi handle POST method CREATE Pegawai
    def render_POST(self, request):
        # Split request path
        resource = request.path.split("/")
        resource_len = len(resource)
        # Print request
        print request.method, request.path

        # Callback function setelah query dijalankan
        # Fungsi ini dijankan setelah query di eksekusi
        def onResult(data):
            self.requestSuccecs(request)

        if resource_len == 2:
            if resource[1] == "pegawai":
                # Get post data
                nama = request.args['nama'][0]
                alamat = request.args['alamat'][0]
                gaji = request.args['gaji'][0]

                def createPegawai():
                    return dbpool.runQuery("INSERT INTO PEGAWAI(nama, alamat, gaji) VALUES(?, ?, ?)", (nama, alamat, gaji, ))
                    #return dbpool.runQuery("SELECT * FROM PEGAWAI")

                createPegawai().addCallback(onResult)
        else:
            status = "No resource"
            self.requestError(request, status)

        return NOT_DONE_YET

    # Fungsi handle PUT update pegawai
    def render_PUT(self, request):
        # Split request path
        resource = request.path.split("/")
        resource_len = len(resource)
        print request.method, request.path

        def onResult(data):
            self.requestSuccecs(request)

        if resource_len == 3:
            if resource[1] == "pegawai":
                if self.is_number(resource[2]):
                    id = resource[2]

                    # Get content
                    # request.args akan bernilai {} jika pada method PUT
                    # Baca content yang terencode xxx-www-urlencode, parsing content dengan urlparse
                    content = urlparse.parse_qs(request.content.getvalue())
                    nama = content['nama'][0]
                    alamat = content['alamat'][0]
                    gaji = content['gaji'][0]

                    def updatePegawai():
                        return dbpool.runQuery("UPDATE PEGAWAI SET nama = ?, alamat = ?, gaji = ? WHERE ID = ?", (nama, alamat, gaji, id, ))

                    updatePegawai().addCallback(onResult)
                else:
                    status = "Request path or parameter error"
                    self.requestError(request, status)

        else:
            status = "No resource"
            self.requestError(request, status)

        return NOT_DONE_YET


    def render_DELETE(self, request):
        # Split request path
        resource = request.path.split("/")
        resource_len = len(resource)
        print request.method, request.path

        def onResult(data):
            self.requestSuccecs(request)

        if resource_len == 3:
            if resource[1] == "pegawai":
                if self.is_number(resource[2]):
                    id = resource[2]

                    def updatePegawai():
                        return dbpool.runQuery("DELETE FROM PEGAWAI WHERE ID = ?", (id,))

                    updatePegawai().addCallback(onResult)
                else:
                    status = "Request path or parameter error"
                    self.requestError(request, status)

        else:
            status = "No Resourse"
            self.requestError(request, status)

        return NOT_DONE_YET

    # Fungsi response jika request error
    def requestError(self, request, status):
        request.setResponseCode(404)
        request.write(status)
        request.finish()

    # Fungsi response jika request success
    def requestSuccecs(self, request):
        request.setResponseCode(200)
        status = {"status": "success"}
        request.write(json.dumps(status))
        request.finish()

    # Fungsi untuk check value string adalah angka
    def is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

# Factory
factory = Site(Pegawai())
reactor.listenTCP(7887, factory)
reactor.run()