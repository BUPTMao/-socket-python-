# coding=gbk
#server服务器
import socket
address = ('127.0.0.1',9996)#本主机IP
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(address)


while 1:
    data,address=s.recvfrom(2048)
    if not data:
        break
    print("got data from",address)
    print(data.decode())
    replydata = input("reply:")
    s.sendto(replydata.encode("utf-8"),address)
s.close()