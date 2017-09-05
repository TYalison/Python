#这次作业因为有很多不明白的地方,所以参考了一些网上的代码,若有问题请批评指正。
from socket import *
bufferSize=1024
def sendMsg(host,port):
    address=(host,port)
    clientSocket=socket(AF_INET,SOCK_STREAM)
    clientSocket.connect(address)
    while True:
        data=raw_input('>')
        if not data:
            break
        clientSocket.send(data)
        data=clientSocket.recv(bufferSize)
        if not data:
            break
        print(data)
    clientSocket.close()
sendMsg('localhost',12340)
