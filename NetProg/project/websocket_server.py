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

		dict_data = json.loads(data)
		if dict_data['id'] == 'sub':
			topik = dict_data['topik']
			
			if topik in dict_subs:
				dict_subs[topik].append(self)
			else:
				dict_subs[topik] = []
				dict_subs[topik].append(self)
			
			dict_data['status'] = 'success'
			data = json.dumps(dict_data)
			self.transport.write(data)

		elif dict_data['id'] == 'pub':
			topik = dict_data['topik']
			pesan = dict_data['pesan']

			if topik in dict_subs:
				list_subs = dict_subs[topik]
				data = {'topik': topik, 'pesan': pesan}
				for sub in list_subs:
					str_data = json.dumps(data)
					sub.transport.write(str_data)

class EchoFactory(protocol.Factory):
	def buildProtocol(self, address) :
		return EchoServer()

factory = EchoFactory()
reactor.listenTCP(8877, WebSocketFactory(factory) )
reactor.run()
