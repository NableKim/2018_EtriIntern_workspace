import bluetooth

target_name = "Galaxy A3 (2016)"
target_address = None

try:
    nearby_devices = bluetooth.discover_devices(duration=20)
except BluetoothError as e:
        LOG.error("BT error %s" % e )
for bdaddr in nearby_devices:
    print bdaddr
    if target_name == bluetooth.lookup_name(bdaddr):
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with addres ", target_address
else:
    print "could not find target bluetooth device nearby"
