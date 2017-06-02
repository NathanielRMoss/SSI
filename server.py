import socket # for internet sockets
import logging # for debugging
import time # time functions
import sys # for Logging
from multiprocessing import Process, Pool, TimeoutError, Lock # to multiprocess sql inserts 
from http.server import BaseHTTPRequestHandler, HTTPServer

# configuration items for running the server
# Logging initation
party = 1 #Threads in our pool, default may need to be 4.
logging.basicConfig(filename='debug.log', level=logging.DEBUG)
# Port configuration for stream
host, port = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def ServerInit(): # currently not used
	listen_socket.bind((host, port))
	listen_socket.listen(1)
	print('Now listening on PORT %s' % port)
	logging.debug('Now listening on PORT %s' % port)
	return;

def HTTPInit(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
	server_address = ()
	print(server_address, handler_class)
#	httpd = server_class(server_address, handler_class)
#	httpd.serve_forever()
#def Connection(): to be defined

class HTTPHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        send_headers()
    def do_GET(s):
        # Respond to a GET request.
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Error 500: Internal Server Error</title></head>")
        s.wfile.write("<body><p>You shouldn't be here with HTML.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        # s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        s.wfile.write("</body></html>")
    
def SensorWrite(arg1,arg2,arg3):
	return;

def ImportJSON(file):
	file = open('config.ini', 'r')
	file.close()
	return;

def Main():
	# Main Function
	listen_socket.bind((host, port))
	listen_socket.listen(1)
	print('Now listening on PORT %s' % port)
	logging.debug('Now listening on PORT %s' % port)
	# iterating loop for our main function
	httpd = HTTPInit((host,port), BaseHTTPRequestHandler)
	pool = Pool(processes=party) 
	# Multithreading Start        
	while True:
		client_connection, client_address = listen_socket.accept()
		request = client_connection.recv(1024).decode('utf-8')
		if not client_connection:
			break
		print('Incoming Connection on: ' + str(client_address))
		logging.debug('Incoming Connection on ' + str(client_address))
		logging.debug(request)
		client_connection.close()

if __name__ == '__main__':
    Main()
