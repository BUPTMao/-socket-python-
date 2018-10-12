# coding=gbk
#client客户端
import socket
address = ('127.0.0.1',9996)#主机IP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(address)

flag = True
while flag:
    str = input('Please input :')
    strInput=str.encode('utf-8')
    s.send(strInput)
    data=s.recv(200)
    if data:
        print("from:", address)
        print("got recive :", data.decode())