import socket
from threading import Thread

"""
使用udp的时候:
如果先要发送数据给对方,则不需要bind端口,对方收到数据之后就知道发送方的端口了
如果需要接收数据,则需要先bind端口,对方才能发送数据过来

udp直接sendto()就可以发送数据

tcp需要先连接到对方socket
"""
t = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
t.bind(('', 5589))


def send_data():
    while True:
        send_str = input('please input send data')
        t.sendto(send_str.encode(), ("192.168.1.11", 57912))


def receive_data():
    while True:
        receive_info = t.recvfrom(1024)
        receive_info[0].decode()
        print(receive_info[0].decode())

 
thread_send = Thread(target=send_data)
thread_receive = Thread(target=receive_data)
thread_send.start()
thread_receive.start()
