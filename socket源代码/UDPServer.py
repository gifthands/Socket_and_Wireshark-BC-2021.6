# -*- coding: utf-8 -*-

from socket import *
serverPort=12000		#服务器端口号
serverSocket=socket(AF_INET,SOCK_DGRAM)		#创捷服务器套接字
serverSocket.bind(('192.168.43.125',serverPort)) #绑定，自己设置
print("Ther server is ready to receive")
while True:
	message,clientAddress=serverSocket.recvfrom(1024)	#接受客户端消息
	print("Receive the message \"%s\""%message.decode())  #打印得到的信息
	ChangedMessage=message.decode().upper()	   #将客户端传来的字母边为大写
	serverSocket.sendto(ChangedMessage.encode(),clientAddress) #将信息传回给客户端
	print("Send the message \"%s\""%ChangedMessage) #打印已经发送的信息

