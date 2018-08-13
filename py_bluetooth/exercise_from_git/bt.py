# this code was copied from https://github.com/fabienroyer/Bluetooth/blob/master/bt.py

import bluetooth
from subprocess import Popen, PIPE
import sys

# define Bluetooth Device Class
class BT(object):
    def __init__(self, receiveSize=1024):
        self.btSocket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self._ReceiveSize = receiveSize

    def __exit__(self):
        self.Disconnect()

    def Connect(self, mac, port=3333):
        self.btSocket.connect((mac, port))

    def Disconnect(self):
        try:
            self.btSocket.close()
        except Exception:
            pass

    # Search for nearby devices
    def Discover(self):
        btDevices = bluetooth.discover_devices(lookup_names = True)
        if(len(btDevices)>0):
            return btDevices
        else:
            raise Exception('No Bluetooth device!')

    # Print nearby devices list
    def DumpDevices(self, btDeviceList):
        for mac, name in btDeviceList:
            print("BT device name: {0}, MAC: {1}".format(name, mac))

    def BindListen(self, mac, port=3333, backlog=1):
        self.btSocket.bind((mac, port))
        self.btSocket.listen(backlog)

    def Accept(self):
        client, clientInfo = self.btSocket.accept()
        return client, clientInfo

    def Send(self, data):
        self.btSocket.send(data)

    def Receive(self):
        return self.btSocket.recv(self._ReceiveSize)

    def GetReceiveSize(self):
        return self._ReceiveSize

# Client
def StartBTClient():
    cli = BT()
    print('BT Discovery...')
    # Search for nearby devices
    btDeviceList = cli.Discover()
    cli.DumpDevices(btDeviceList)

    # select one device you want to connect
    mac = btDeviceList[0][0]
    name = btDeviceList[0][1]
    print('Connecting to first BT device found: {0}, MAC:{1}'.format(name, mac))
    cli.Connect(mac)

    # After connected, get input from user to send data to server
    print('Connected... Enter data or \'exit\' to terminate the connection')
    while True:
        data = raw_input()
        if (data=='exit'):
            break
        try:
            cli.Send(data)
        except Exception as e:
            print(e.__str__())
            break
    cli.Disconnect()

# Get Host Mac address by parsing the result of command "$ hcitool dev"
def GetFirstMAC():
    proc = Popen(['hcitool', 'dev'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, error = proc.communicate()
    if(proc.returncode == 0):
        lines = output.split('\r')
        for line in lines:
            if 'hci0' in line:
                temp = line.split('\t')
                temp = temp[2].strip('\n')
                return temp
            raise Exception('MAC not found')
    else:
        raise Exception('Command: {0} returned with error: {1}'.format(cmd, error))

# Server
def StartBTServer():
    srv = BT()
    # Get server's mac address
    mac = GetFirstMAC()

    # Bind and Be ready to listen
    srv.BindListen(mac)
    print('Listening for connections on: {0}'.format(mac))

    # Server is listening to accept clents' connection request
    while True:
        client, clientInfo = srv.Accept()
        print('Connect to: {0}, port: {1}'.format(clientInfo[0], clientInfo[1]))
        try:
            # if connected, server can get input from client
            while True:
                data = client.recv(srv.GetReceiveSize())
                if(data is not None):
                    print(data)
                    client.send(data)
        except:
            print("Closing client socket")
        client.close()
    srv.Disconnect()

if __name__ == '__main__':
    cmd = sys.argv[1]
    if(cmd == 'server'):
        StartBTServer()
    elif(cmd == 'client'):
        StartBTClient()
    else:
        print("Bluetooth RFCOMM client/server demo")
        print("Copyright 2014 Nwazet, LLC.")
        print("Please specify 'client' or 'server'")
        print("This demo assumes a single Bluetooth interface per machine.")
