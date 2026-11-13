"""
案例:演示property属性的用法

property属性介绍:
    概述/目的/作用:
        把 函数 当作 变量来使用
    实现方式:
        方式1:装饰器
        方式2:类属性

property装饰器的用法:
    @property               修饰 获取值的函数
    @获取值的函数名.setter  修饰 设置值的函数

property类属性的用法:
    类属性名 = property(获取值的函数,设置值的函数)

    之后,就可以直接 ,上述的函数名 来当作变量直接用

"""
#需求 :定义学生类,私有属性 age,通过 property 类属性 来实现
#1. 定义学生类
class Student:
    def __init__(self):
        self.__age = 18

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age

    #封装上述的公共方式为 类属性
    #参1: 获取值的函数
    #参2: 设置值的函数
    age = property(get_age,set_age)



#2. 测试
if __name__ == '__main__':
    s = Student()
    #设置值
    s.age = 23
    print(s.age)






