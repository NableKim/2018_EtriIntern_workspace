import bluetooth
import subprocess

# For host device to be discoverable
cmd = 'sudo hciconfig hci0 piscan'
subprocess.check_output(cmd, shell=True)

# find an available port
port=bluetooth.PORT_ANY

# make socket
server_sock.bind(("". port))
server_sock.listen(1)
print "listening on a port %d" % port

# define service information and register service info to SDP server
uuid = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848"
bluetooth.advertise_service(sercer_sock, "aaa", uuid)

# Get client socket when client want to connect
print "Accepted connection from ", address

# Receive data from client
data = client_sock.recv(1024)
print "received [%s]"  % data

# Finished
client_sock.close()
server_sock.close()
