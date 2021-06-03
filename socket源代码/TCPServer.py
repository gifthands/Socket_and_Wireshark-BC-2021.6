# -*- coding: utf-8 -*-

from socket import *
serverName='192.168.43.125'
serverPort=12001
serverSocket=socket(AF_INET,SOCK_STREAM)	#创建套接字
serverSocket.bind((serverName,serverPort))	#绑定IP地址和端口bind()
print("Ther server is ready to receive")
serverSocket.listen(5)						#进行监听
while True:
	conn,addr=serverSocket.accept()			#连接套接字和客户端地址
	print("Connected by ",addr)				#连接成功，打印信息
	Data=conn.recv(1024).decode()			#从客户端接受数据（需要解码）
	print("Receive the message \"%s\""%Data)#打印信息
	ChangedData=Data.upper()				#将数据转换为大写
	conn.send(ChangedData.encode())			#将数据发送给客户端
	print("Send the message \"%s\""%ChangedData)#打印信息
	conn.close()							#关闭套接字
