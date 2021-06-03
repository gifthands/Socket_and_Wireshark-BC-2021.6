import base64
from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start
mailserver = "smtp.qq.com"
#Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
#Fill in end
recv = clientSocket.recv(1024).decode()
print (recv)
if recv[:3] != '220':
	print ('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print (recv1)
if recv1[:3] != '250':
	print ('250 reply not received from server.')
 
# Send MAIL FROM command and print server response.
# Fill in start

#登录
mailFromAddress = '2442561355@qq.com'
mailPassWord = 'iamoqfeanyjgebhg'   #我的QQ邮箱开启smtp服务的服务码
mailToAddress = '2442561355@qq.com'



loginCommand = 'AUTH LOGIN\r\n'.encode()
clientSocket.send(loginCommand)
recv = clientSocket.recv(1024).decode()

print(recv)
if recv[:3] != '334':
	print('334 reply not received from server')
 
# 邮箱账户
user = base64.b64encode(mailFromAddress.encode()).decode()
userCommand = user + '\r\n'

clientSocket.send(userCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '334':
	print('334 reply not received from server')

password = base64.b64encode(mailPassWord.encode()).decode()
passCommand = password + '\r\n'

clientSocket.send(passCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '235':
	print('235 reply not received from server')

MFCommand = 'MAIL FROM: <'+mailFromAddress+'>\r\n'

clientSocket.send(MFCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
	print('250 reply not received from server')
# Fill in end
	
# Send RCPT TO command and print server response. 
# Fill in start
RTCommand = 'RCPT TO: <'+mailToAddress+'>\r\n'

clientSocket.send(RTCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
	print('250 reply not received from server')
# Fill in end
	
# Send DATA command and print server response. 
# Fill in start
DATACommand = 'DATA\r\n'

clientSocket.send(DATACommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '354':
	print('354 reply not received from server')
# Fill in end
	
# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end
	
# Message ends with a single period.
# Fill in start

clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
	print('250 reply not received from server')
# Fill in end
	
# Send QUIT command and get server response.
# Fill in start
QUITCommand = 'QUIT\r\n'

clientSocket.send(QUITCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '221':
	print('221 reply not received from server')
# Fill in end
