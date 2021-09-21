#!/usr/bin/env python

import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 'put-a-port-based-on-the-info-collected-from-task-C'#must be integer
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT)) #establishes the connection

while (1):
	#s.send(MESSAGE)#sends a message to the server
	data = s.recv(BUFFER_SIZE) #waits for a reply from the Server
	#data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print ("received data:", data.decode('utf-8'))
	#finish_connection = raw_input("Finish connection (Y/N)")
	#if finish_connection== "Y":
	#	s.send("close_connection")#sends a message to the server
	#	break
	time.sleep(1)
s.close() #closes the socket
