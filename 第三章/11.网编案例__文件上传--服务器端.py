"""
案例: 文件上传--服务器端

回顾:网编服务器端的流程
    1.创建服务器端Socket对象
    2.绑定IP地址和端口号
    3.设置最大监听数
    4.等待客户端申请建立连接
    5.读取客户端申请建立连接
    6.释放资源
"""
# 导包
import socket

#1.创建服务器端Socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#2.绑定IP地址和端口号
server_socket.bind(('192.168.43.162', 80))
#3.设置最大监听数
server_socket.listen(10)
#4.等待客户端申请建立连接
accept_socket, client_addr = server_socket.accept()
#5.读取客户端申请建立连接
#5.1关联目的地文件
with open('./data/my.txt', 'wb') as f:
    #5.2 循环读取数据
    while True:
        #5.3接收客户端的数据
         bys = accept_socket.recv(8192) #8192字节 = kb
        #5.4判断是否读取到数据,无数据(客户端关闭连接)结束即可
         if len(bys) == 0:
            break

        #5.5将读取到的数据写入文件
         f.write(bys)


#6.释放资源
accept_socket.close()





