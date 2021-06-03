# -*- coding: utf-8 -*-

from socket import *
serverName= '192.168.43.125'
serverPort=12001
clientSocket=socket(AF_INET,SOCK_STREAM)        #创建套接字端口
print("This is TCP Client")						#打印信息，开始信息交互
clientSocket.connect((serverName,serverPort))   #连接服务端
message=input("Input lowercase sentence:")      #输入命令行
clientSocket.send(message.encode())             #发送给服务器
modifiedMessage=clientSocket.recv(1024)         #接受服务器返回的数据
print("=>",modifiedMessage.decode())			#打印由服务端返回的信息
clientSocket.close()                            #关闭套接字
