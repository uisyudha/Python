import httplib, urllib
import json

conn = httplib.HTTPConnection('localhost:9997')

# Data seluruh pegawai
def semua():
    conn.request('GET', '/pegawai')
    response = conn.getresponse()
    resp = response.read()

    data = json.loads(resp)
    for p in data:
        print p['nip'], p['nama'], p['alamat']


# Pegawai dengan id terntentu
def pegawai(id):
    conn.request('GET', '/pegawai/'+ str(id))
    response = conn.getresponse()
    resp = response.read()
    data = json.loads(resp)

    print data['nip'], data['nama'], data['alamat']

# Create pegawai
def tambah_pegawai(nip="", nama="", alamat=""):
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	params = urllib.urlencode({'nip': nip, 'nama': nama, 'alamat' : alamat})
	conn.request("POST", "/pegawai", params, headers)
	response = conn.getresponse()
	print response.read()

# Update pegawai
def update_pegawai(id, nip='', nama='', alamat=''):
    headers = {'Content-type': 'application/x-www-form-urlencded', 'Accept': 'text/plain'}
    params = urllib.urlencode({'nip': nip, 'nama': nama, 'alamat': alamat})
    conn.request('PUT', '/pegawai/' + str(id), params, headers)
    response = conn.getresponse()
    print response.read()

# Hapus pegawai
def hapus_pegawai(id):
    conn.request('DELETE', '/pegawai/' + str(id))
    response = conn.getresponse()
    print response.read()

#semua()
#pegawai(2)
#tambah_pegawai('678','Parjo', 'Kediri')
#update_pegawai(2, '910', 'Parjo2', 'Kediri')
#delete_pegawai(2)