#a = 20
#b = 10
#c = 10.0

"""
d = a+b
print "int + int", d 

f = a + c
print "int + float", f

x="Hasil penjumlahan adalah"
print x + str(f) + "casting ke string"
"""

list_hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")


for i in list_hari:
	print i

for j in range(0, len(list_hari)):
	print list_hari[j]


dict_ibukota = {"Indonesia" : "Jakarta", "Thailand" : "Bangkok"}

print dict_ibukota["Indonesia"]

for key in dict_ibukota:
	print key
	
for key, value in dict_ibukota.items():
	print key, value
	

try:
	print dict_ibukota["Tidak ada"]
except KeyError:
	print "Index Not Found"
