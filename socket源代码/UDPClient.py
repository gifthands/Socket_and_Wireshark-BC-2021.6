# -*- coding: utf-8 -*-

from socket import *
serverName= '192.168.43.125'     #本机回送地址
serverPort=12000            #创建的客户器端口号
clientSocket=socket(AF_INET,SOCK_DGRAM)     #创建客户端套接字
print("This is UDP Client")	#打印提示信息，开始交互
message=input("Input lowercase sentence:")  #输入命令行
clientSocket.sendto(message.encode(),(serverName,serverPort)) #将信息给服务器
modifiedMessage,serverAddress=clientSocket.recvfrom(1024) #得到返回的信息和服务器的地址
print("=>",modifiedMessage.decode())		#打印得到的信息（需要解码）
clientSocket.close()        #关闭套接字


