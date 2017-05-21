# Import httplib
import  httplib

# Buat koneksi
connection = httplib.HTTPConnection('ip.jsontest.com')
# Buat request, parameter (method,url,body,header)
connection.request('GET', '/')
# Tampung respone dalam variable raw
raw = connection.getresponse()
# Read raw respone simpan di resp
resp = raw.read()
# Print resp
print resp

