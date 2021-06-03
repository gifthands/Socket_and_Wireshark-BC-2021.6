#import socket module
import datetime
from socket import * 
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverName='192.168.43.125'
serverPort=80
serverSocket.bind(("",serverPort))
#Fill in end
serverSocket.listen(5) 
while True:
 #Establish the connection
	print ("Ready to serve...")
	connectionSocket, addr = serverSocket.accept()	 #Fill in end 
	try:
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata=f.read()
		#print(outputdata)
		#Send one HTTP header line into socket
		#Fill in start
		time=datetime.datetime.now()
		GMTtime=datetime.datetime.strftime(time,"%a, %d %b %G %T GMT")
		head="HTTP/1.1 200 OK\r\nConnection: close\r\nDate:"+GMTtime+"\r\nServer:WanYiWebServer\r\nLast-Modified: Fri, 21 Dec 2020 22:22:22 GMT\r\nContent-Length:%d\r\nContent-Type: text/html\r\n\r\n"%len(outputdata)
		connectionSocket.send(head.encode())
		print("file \"%s\" Sucessfully Found"%(filename[1:]).decode())
		#Fill in end 
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)): 
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.close()		
	except IOError:
		#Send response message for file not found
		#Fill in start
		message='HTTP/1.1 404 Not Found'
		connectionSocket.send(message.encode())
		print("file \"%s\" Not Found"%(filename[1:]).decode())
		#Fill in end
		#Close client socket
		#Fill in start
		connectionSocket.close()
		#Fill in end
