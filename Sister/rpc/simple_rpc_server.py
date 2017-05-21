from SimpleXMLRPCServer import SimpleXMLRPCServer

def tambah(a, b):
    return (a + b)


def kurang(a, b):
    return  (a - b)

server = SimpleXMLRPCServer(('', 6666))
print "Listening on port 6666"

server.register_function(tambah, "tambah")
server.register_function(kurang, "kurang")

server.serve_forever()
