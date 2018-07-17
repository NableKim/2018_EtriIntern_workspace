import bluetooth

bd_addr = "B8:27:EB:1C:F9:72"
port = 1

sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

sock.connect((bd_addr, port))

# get file name to receive from server
packageSize = 1024
name = sock.recv(packageSize)
f = open(name, 'wb')
print (name, " is opened...!")

packet = 1
print "Starting receiving..."
while packet:
    packet = sock.recv(packageSize)
    f.write(packet)
    if len(packet)==839:
        break
isFileGot = True
f.close()
print ("File Got!")

sock.close()
