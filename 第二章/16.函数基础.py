#注意:函数定义的时候并不会执行,只有调用的时候,才会执行逻辑;先定义,再调用
#函数定义
import math


# def out_line():
#     print("----------------------")
#     print("**********************")
#
#
#
# #函数调用
#
# out_line()



#函数的参数与返回值
#函数1: 计算圆的面积
# def circle_area(r):
#     return math.pi*r**2  # math.pi -->Π
# circle_area(6)
# print(circle_area(10))
#
#函数2:计算长方形的面积
# def rectangle_area(c,k):
#     """
#     根据长方形的长度和宽度,计算长方形的面积
#     :param c:长度
#     :param k:宽度
#     :return:长方形的面积
#     """
#     area = c*k
#     return area
# # help(rectangle_area)
# print(rectangle_area(4,2))
#
# #函数3:计算圆的面积和周长
#
# def circle(r):
#     #-->如果返回值有多个,多个返回值之间逗号隔开 -->
#     #                          多个返回值封装到元组中
#     """
#         根据圆的半径,计算圆的面积和周长
#     :param r:半径
#     :return:面积和周长
#     """
#     return  round(math.pi*r**2,1),round(2*math.pi*r,1)
# all =circle(5)
# print(all)
#
# #解包
# area,len = circle(5)
# print(area,len)



#函数的嵌套调用
#
# def a():
#     print("a-->lalala")
#     b()
#     print("a-->alalal")
#
# def b():
#     print("b-->lblblb")
#     c()
#     print("b-->blblbl")
# def c():
#     print("ccccc")
# a()









