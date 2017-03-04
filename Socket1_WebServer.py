#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverSocket.bind(("",1600))
serverSocket.listen(1)
serverPort=1600
print('webserver port',serverPort)
host=gethostbyname(gethostname())
print('host:',host)
while True:
	#Establish the connection
	print ('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	try:
		message =connectionSocket.recv(1024)
		filename=message.split()[1]
		f = open(filename[1:])
		outputdata =f.read()
		print(outputdata)
		#Send one HTTP header line into socket
		connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf-8'))
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode('utf-8'))
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		connectionSocket.send('404 Not Found'.encode('utf-8'))
		#Close client socket
		connectionSocket.close()
	serverSocket.close()