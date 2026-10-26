"""
案例: 文件上传--客户端

回顾:网编客户端的流程
    1.创建客户端Socket对象
    2.连接服务器端IP地址和端口号
    3.关联数据源文件,读取内容,写给服务器端
    4.释放资源
"""
# 导包
import socket

#1.创建客户端Socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#2.连接服务器端IP地址和端口号
client_socket.connect(('192.168.43.162', 80))
#3.关联数据源文件,读取内容,写给服务器端
#3.1关联数据源文件
with open('d:/gg.txt', 'rb') as f:
    #3.2 循环读取数据
    while True:
        #3.3读取数据
        bys = f.read(8192) #8192字节 = kb
        # 3.4将读取到的数据写给服务器端
        client_socket.send(bys)
        # 3.5判断是否读取到数据,无数据(文件读取完成)结束即可
        if len(bys) == 0:
            break

#4.释放资源
client_socket.close()
