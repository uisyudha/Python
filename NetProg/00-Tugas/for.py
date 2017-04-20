import sys
"""
Program untuk menampilkan pola
*
**
***
****
*****
"""""

for i in range(0,10):
    for j in range(0,i):
        sys.stdout.write("*")
        sys.stdout.flush()
    print ""
