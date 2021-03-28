from os import read, write


imgIn = open('./image2.jpg', 'br')
imgOut = open('./secret.jpg', 'bw')

message = b"Below is the tool for encryption and decryption. Either you can use the public/private keys generated above or supply your own public/private keys."

countFF = 0
readB = imgIn.read(1)
while True:
    if readB == b'\xff':
        countFF += 1
        if countFF == 3:
            imgOut.write(b'\xff\xfe')
            imgOut.write(b'\x00\x00')
            imgOut.write(message)
            imgOut.write(b'\x00\x00')
            imgOut.write(b'\xff')
            break
    imgOut.write(readB)
    readB = imgIn.read(1)

for b in imgIn:
    imgOut.write(b)

imgIn.close()
imgOut.close()