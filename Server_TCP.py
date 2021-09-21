#!/usr/bin/env python
#first run the server which listenes to the clients
import socket



import socket
import sys
import thread
import time

host = ''
port = 15005
BUFFER_SIZE = 1024
MESSAGE = "Kubernetes Lab Acceptance! v1.0"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
#s.settimeout(1)
print('Waiting for a connection.')
def connection_clients():
    #conn.send(str.encode('Welcome, type your info\n'))
#receive name of the car
	while True:
		conn, addr = s.accept()
		try:
			thread.start_new_thread(server_message,(conn,))
		except Exception as errtxt:
			print (errtxt)
		#print(Vehicle_ID+' connected to: '+addr[0]+':'+str(addr[1]))


def server_message(conn):
	while True:
		conn.send(MESSAGE)  # echo
		time.sleep(1)

try:

	thread.start_new_thread(connection_clients,())

except Exception as errtxt:
	print (errtxt)
	
try:
	while 1:
		pass
except KeyboardInterrupt:
	print ('Interruption called')	
	#function to determine if there is new data "peak"
    #start_new_thread(connection_clients,())

