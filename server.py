#这次作业因为有很多不明白的地方,所以参考了一些网上的代码,若有问题请批评指正。
from socket import *
from time import ctime
bufferSize=1024
def recvMsg(host,port):
    address=(host,port)
    serverSocket=socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(address)
    serverSocket.listen(5)
    while True:
        print('waiting for connection...')
        clientSocket,address=serverSocket.accept()
        print('connected from ',address)
        while True:
            data=clientSocket.recv(bufferSize)
            if not data:
                break
            print('received data: ',data)
            clientSocket.send('[%s] %s' % (ctime(),data))
        clientSocket.close()
    serverSocket.close()
recvMsg('localhost',12340)
