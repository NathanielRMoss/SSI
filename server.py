import socket # for internet sockets
import logging # for debugging
import sys # for Logging
from multiprocessing import Process, Pool, TimeoutError, Lock # to multiprocess sql inserts 

# configuration items for running the server
# Logging initation
party = 1 #Threads in our pool, default may need to be 4.
logging.basicConfig(filename='debug.log', level=logging.DEBUG)
# Port configuration for stream
host, port = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def ServerInit():
	listen_socket.bind((host, port))
	listen_socket.listen(1)
	print('Now listening on PORT %s' % port)
	logging.debug('Now listening on PORT %s' % port)
	return;

#def Connection(): to be defined

def SensorWrite(arg1,arg2,arg3):
	return;

def ImportJSON(file):
	file = open('config.ini', 'r')
	file.close()
	return;

def Main():
	ServerInit()
	#iterating loop for our main function
	with Pool(processes=party) as pool: #multithreading pool start
		while True:
			client_connection, client_address = listen_socket.accept()
			request = client_connection.recv(1024).decode('utf-8')
			if not client_connection:
				break
			print('Incoming Connection on: ' + str(client_address))
			logging.debug('Incoming Connection on ' + str(client_address))
			logging.debug(request)
		
			http_response = "Connection established!"
			client_connection.send(http_response.encode('utf-8'))
		#client_connection.close()

if __name__ == '__main__':
	Main()
