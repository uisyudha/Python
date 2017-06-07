from twisted.internet import protocol, reactor
from txws import WebSocketFactory
import json

# List untuk menampung koneksi
dict_subs = {}
clients = []

# Definisikan class untuk protocol yg akan kita buat
class EchoServer(protocol.Protocol):
	# Callback func ketika koneksi berhasil dibuat
	def connectionMade(self) :
		print "Koneksi baru berhasil dibuat"
		# Jika terkoneksi, tambahkan client ke list koneksi
		clients.append(self)

	def connectionLost(self, reason) :
		print "Koneksi putus"
		# Jika koneksi putus, hapus client dari list koneksi
		clients.remove(self)

	# Callback func ketika ada message masuk dari client
	def dataReceived(self, data):
		print data

		#Decode
		dict_data = json.loads(data)
		if dict_data['id'] == 'sub':
			topik = dict_data['topik']
			# Cek jika topik ada di dict_subs tambahkan
			if topik in dict_subs:
				dict_subs[topik].append(self)
			# Jika topik belum ada buat topik baru
			else:
				dict_subs[topik] = []
				dict_subs[topik].append(self)
			# Tambahkan key 'stataus' dan value 'succecs' ke dict_data
			dict_data['status'] = 'success'
			# Encode dict_data pada var data
			data = json.dumps(dict_data)
			# Kirim data ke subscriber sebagai notifikasi sukses
			self.transport.write(data)

		elif dict_data['id'] == 'pub':
			topik = dict_data['topik']
			pesan = dict_data['pesan']

			# Jika topik ada di dict_subs
			if topik in dict_subs:
				list_subs = dict_subs[topik]
				# Buat dictionary data yang akan dikirim,
				data = {'topik': topik, 'pesan': pesan}
				# Kirimkan ke semua subscriber dengan topik tersebut
				for sub in list_subs:
					str_data = json.dumps(data)
					sub.transport.write(str_data)

class EchoFactory(protocol.Factory):
	def buildProtocol(self, address) :
		return EchoServer()

factory = EchoFactory()
reactor.listenTCP(8877, WebSocketFactory(factory) )
reactor.run()