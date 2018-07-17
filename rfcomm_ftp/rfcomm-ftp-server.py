import bluetooth
import subprocess
import os
import time

# For host device to be discoverable
cmd = 'sudo hciconfig hci0 piscan'
subprocess.check_output(cmd, shell=True)

# Define which protocol will you use
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# initialize socket and turn on listening
port = 1
server_sock.bind(("", port))
print "Bound and then listening..."
server_sock.listen(1)

client_sock, address = server_sock.accept()
print "Accept connection from ", address

# get a file size to send
sendPath = '/home/pi/kss/image.jpg'
packageSize = os.path.getsize(sendPath)
print "File size is %d" % packageSize

if(packageSize == None):
    packageSize = 1024

# ser which file will you sendPath
f = open(sendPath, 'rb')

# send exact file name
client_sock.send(sendPath)

# start file transfer
packet = 1
print(sendPath, "is ", os.path.getsize(sendPath), "starts @", time.ctime())
while(packet):
    packet = f.read(1024)
    client_sock.send(packet)
    print "packet size : %d" % len(packet)
print("Finished sending @ :", time.ctime())
isFileSent = True
f.close()

client_sock.close()
server_sock.close()
