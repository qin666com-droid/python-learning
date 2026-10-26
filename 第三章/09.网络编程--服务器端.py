#2.客户端与服务器端
"""
案例:网编入门案例,服务器端给客户端发送消息,客户端给出回执信息

服务器端开发流程:
    1.创建服务器端Socket对象
    2.绑定IP地址和端口号
    3.设置最大监听数
    4.等待客户端申请建立连接
    5.给客户端发送信息
    6.接收客户端的信息并打印
    7.释放资源

细节:
    客户端和服务器端是通过 字节流(bytes) 的形式实现的

"""
# 导包
import socket

# 1.创建服务器端Socket对象  ipv4 字节流(TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.绑定IP地址和端口号
server_socket.bind(("192.168.43.162", 10086))
# 3.设置最大监听数
server_socket.listen(10)
# 4.等待客户端申请建立连接
accept_socket, client_addr = server_socket.accept()
# 5.给客户端发送信息
accept_socket.send(b'hello world')
# 6.接收客户端的信息并打印
client_data = accept_socket.recv(1024).decode('utf-8')
print(f"服务器端收到的信息是:{client_data}")
# 7.释放资源
accept_socket.close()
# server_socket.close()    # 服务器端关闭,客户端会自动关闭连接,所以一般不关闭

#扩展: 设置端口号重用,目的是: 快速重启服务器(服务器关闭后,立即释放端口)
#参1: 当前的套接字对象, 参2: 选项名, 参3: 选项值
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
