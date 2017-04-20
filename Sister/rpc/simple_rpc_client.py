import xmlrpclib

proxy = xmlrpclib.ServerProxy("http://localhost:6666")

a = 100
b = 100

print proxy.tambah(a,b)
print proxy.kurang(a,b)