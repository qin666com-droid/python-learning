"""
实例: 演示编解码

细节:
    1.编码 = 把我们看懂的 转换成 我们看不懂的
        '字符串'.encode('utf-8'(码表))
    2.解码 = 把我们看不懂的 转换成 我们看懂的
        '二进制'.decode('utf-8'(码表))
    3.只要乱码了,原因只有1个,编解码不同
    4.英文字母,数字,特殊符号无论什么码表的只占1个字节,中文在gbk占2个字节,utf-8中占3个字节
    5.二进制数据特殊写法,即 b'字母,数字,特殊符号',  该方式针对中文无效


"""

#需求1:编码
q1 = '扶苏888acd!@#'

print(q1.encode())              #b'\xe6\x89\xb6\xe8\x8b\x8f888acd!@#'
print(q1.encode('utf-8'))       #b'\xe6\x89\xb6\xe8\x8b\x8f888acd!@#'
print(q1.encode('gbk'))         #b'\xb7\xf6\xcb\xd5888acd!@#'
print('*'*30)

#需求2:解码
q2 = b'\xe6\x89\xb6\xe8\x8b\x8f888acd!@#'
print(type(q2))                 #<class 'bytes'>
print(q2.decode())              #扶苏888acd!@#
print(q2.decode('utf-8'))       #扶苏888acd!@#
print('*'*30)

print(q2.decode('gbk'))         #鎵惰嫃888acd!@#
#编解码不一致,就有可能导致乱码







