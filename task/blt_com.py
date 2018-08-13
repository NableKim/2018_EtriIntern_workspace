import bluetooth
from PyOBEX.client import Client
import os
import sys
import threading, time

target_dict_list = []

class FTPclient(threading.Thread):
    def __init__(self, address, port, file_path, file_name):
        threading.Thread.__init__(self)
        self.address = address
        self.port = port
        self.client = Client(self.address, self.port)
        self.file_path = file_path
        self.file_name = file_name

    def run(self):
        try:
            self.client.connect()
            self.client.put(self.file_name, open(self.file_path).read())
            print '********************************************************************'
            print self.address+' : File Transfer Success!!!'
            print '********************************************************************'
        except:
            print '********************************************************************'
            print self.address++' : File Transfer Failed...'
            print '********************************************************************'
        self.client.disconnect()
        self.client.delete

def sdpBrowse(addr):
    global target_dict_list
    oop_available = False
    services = bluetooth.find_service(address=addr)
    for service in services:
        name = service['name']
        proto = service['protocol']
        port = str(service['port'])
        print 'Found! - ' + str(name) + ' on ' + str(proto) + ' : ' + port

        if name=='OBEX Object Push':
            print '===================================================================='
            print 'Get OOP service info...'
            print '===================================================================='
            target_dict_list.append({'address':addr, 'name':name, 'proto':proto, 'port':int(port)})
            oop_available = True

    # check if OOP service in unavailable
    if not oop_available:
        print '===================================================================='
        print addr + ' device doesn\'t support OBEX Object Push service...'
        print '===================================================================='

def getOopServiceInfo(target_address):
    print '===================================================================='
    print 'Let\'s find ' + target_address + '\' services...'
    print '===================================================================='
    # find services on target devices
    sdpBrowse(target_address)

def bltFTP():
##    target_dict_list = []

    try:
        nearby_devices = bluetooth.discover_devices(lookup_names=True, duration=5)
    except BluetoothError as e:
        LOG.error("BT error %s" % e )
        quit()

    for addr, name in nearby_devices:
        print name +"\t"+ addr

    target_address_str=raw_input("Which one do you want to connect? : ")

    if not target_address_str:
        print "You didn't input any devices\' MAC address"
        sys.exit(1)

    # Separate Mac address inputs with ' ' (space)
    target_addresses_list=target_address_str.split(' ')

    # Search for services on each devices and Collect devices' info to support OOP
    for target_address in target_addresses_list:
        getOopServiceInfo(target_address)
    
    if len(target_dict_list)<1:
        sys.exit(1)
        #quit()

    # Get file path and Set file name to save as from user
    file_path=raw_input('Please input file\'s path to send it (ex. /home/pi/kss/image.jpg) : ')
    print '===================================================================='

    # Set file name to be stored on target device
    file_name=raw_input('Please set file name to save as (ex. HelloWorld.jpg) : ')
    print '===================================================================='
    print '\n\n'

    # make connect socket thread and run
    target_addresses_size=len(target_dict_list)
    ftp_client_list=[]
    for index in range(0, target_addresses_size):
        ftpclient = FTPclient(target_dict_list[index]['address'], target_dict_list[index]['port'], file_path, file_name)
        ftp_client_list.append(ftpclient)
        ftpclient.start()

    # join
    for ftpclient in ftp_client_list:
        ftpclient.join()

    print "Ending Connection..."
