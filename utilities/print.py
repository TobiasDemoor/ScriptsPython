import os
import sys
from PyPDF2 import PdfFileReader

nombreArchivo = sys.argv[1]
reader = PdfFileReader(open(nombreArchivo, 'rb'))
pags = reader.getNumPages()

n = 1
cmd = "pdftk %s cat "%nombreArchivo
while (n <= pags):
    cmd += "%d "%n
    n += 2
cmd += "output - | lpr"
print(cmd)
os.system(cmd)

if input("De vuelta las hojas (ingrese x para abortar) ") != "x":
    n = pags
    if pags%2 == 1:
        n -= 1
        os.system("lpr blank.pdf")

    cmd = "pdftk %s cat "%nombreArchivo
    while (n > 0):
        cmd += "%d "%n
        n -= 2
    cmd += "output - | lpr"
    print(cmd)
    os.system(cmd)