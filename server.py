import socket
import logging
import sys

# Logging levels
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

# configuration items for running the server
# Port configuration for stream
host, port = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((host, port))
listen_socket.listen(1)
print('Now listening on PORT %s' % port)
logging.debug('Now listening on PORT %s' % port)

def Main():
	#iterating loop for our main function
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
