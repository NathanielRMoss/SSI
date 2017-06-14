import os # for JSON reading of file modified times
import socket # for internet sockets
import logging # for debugging
import time # time functions
import sys # for Logging
from multiprocessing import Process, Pool, TimeoutError, Lock # to multiprocess sql inserts 
from http.server import BaseHTTPRequestHandler, HTTPServer

# configuration items for running the server
# Logging initation
party = 5 #Threads in our pool, default may need to be 4.
logging.basicConfig(filename='debug.log', level=logging.DEBUG)
# Port configuration for stream
host, port = 'localhost', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

class HTTPHandler(BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        send_headers()
    def do_ERROR(s):
        # Respond to a GET request.
        s.send_response(500)
        s.send_header("Content-type", "text/html")
        hs.end_headers()
        s.wfile.write('<html><head><title>Error 500: Internal Server Error</title></head>')
        s.wfile.write('<body><p>You shouldn\'t be here with HTML.</p>')
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        # s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        s.wfile.write("</body></html>")
    
def SensorWrite(arg1,arg2,arg3):
	return;

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

def ErrorHandler(errortype,error):
	print(errortype + ': ' + error)
	if errortype == 'warn':
		logging.warning(errortype + ': ' + error)
	if errortype == 'debug':
		logging.debug(errortype + ': ' + error)
	return

def Main():
	# Main Function
	# Get the config from the JSON file specified
	try:
		CONFIG = open('config.ini', 'r')
		CONFIG.close()
	except FileNotFoundError:
		ErrorHandler('warn','CONFIG.INI: No config file found at boot.')
	#	print('CONFIG.INI: No config file found at boot.')
	#	logging.warning('CONFIG.INI: No config file found at boot.')	
	#parse the JSON config
	# 
	# is okay?
	# if error == 1
	#	logging.debug
	#	raise KeyboardInterrupt
	listen_socket.bind((host, port))
	listen_socket.listen(1)
	print('Now listening on PORT %s' % port)
	logging.debug('Now listening on PORT %s' % port)
	# iterating loop for our main function
	pool = Pool(processes=party) 
	# Multithreading Start        
	while True:
		client_connection, client_address = listen_socket.accept()
		print('Incoming connection on: ' + str(client_address))
		logging.debug('Incoming Connection on ' + str(client_address))
		request = client_connection.recv(1024).decode('ascii')
		if not request:
			break
		logging.debug(request)
		#bucket the data for comparison
		KEY = request[:16]
		CMD = request[17:19] 
		PAGES = request[20]
		DATA = request[21:1004]
		#Authentication loop
		try: 
			tablename = 'client_' + str(KEY)
			tableexists = checkTableExists(dbcon, tablename)			
		except NoConnection: # need to check this error specifically
			logging.debug('No Connection to database, KEYCHECKFAILED')
			client_connection.send(str(KEY) + 'ONO1' + 'No Connection to Database.')
			break  
		#except NoExists:
		#	if COMMAND == 'NEW':
			#make a new table for this client_key
		
		#Authenticated, what's the command?		
		CMD = request [17:19]
		if CMD == 'SEN':
			#read DATA and determine sensor data
			#append data to client_keys database
			#check success
			client_connection.send(str(KEY) + 'YESS' )
			break
		if CMD == 'QUE':
			# check to see if json has been modified
			# query JSON file for config changes
			client_connection.send(str(KEY) + 'YESQ' )			
		if KEY == 'http':
			httpd = HTTPInit((host,port), do_ERROR)
	client_connection.close()

if __name__ == '__main__':
    Main()
