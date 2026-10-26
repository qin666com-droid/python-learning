"""
案例:演示 带参数的装饰器

记忆:
    1.1个装饰器的参数有且只有1个
    2.如果装饰器有多个参数,可以在该装饰器的外边再包裹一层,把该装饰器当作其内部函数,返回即可

"""
#需求:定义一个既能装饰减法,也能装饰加法的装饰器 ->即: 带有参数的装饰器
#1.定义装饰器
#fun_name:原函数名 flag:标记 报错,装饰器的参数有且只有1个
# def my_decorator(fun_name,flag):
# def login(flag):

#     def my_decorator(fun_name):
#         #1.1定义内部函数
#         def fun_in(a,b):
#             #1.2增加功能
#             if flag =='+':
#                 print("正在努力计算[加法]中.....")
#             elif flag =='-':
#                 print("正在努力计算[减法]中.....")
#             #1.3有引用
#             return fun_name(a,b)
#         #1.4返回内部函数
#         return fun_in
#
#     return my_decorator
#
#
# #2.定义原函数 表示:加法运算
# @login('+')
# def get_sum(a,b):
#     return a+b
#
# #3.定义原函数 表示:减法运算
# @login('-')
# def get_diff(a,b):
#     return a-b
#
#
# #4.测试
# print(get_sum(3,5))
# print("*"*20)
# print(get_diff(9,1))



#优化
def my_decorator(fun_name):
    #1.1定义内部函数
    def fun_in(a,b):
        #1.2增加功能
        if fun_name.__name__ == 'get_sum':
            print("正在努力计算[加法]中.....")
        elif fun_name.__name__ == 'get_diff':
            print("正在努力计算[减法]中.....")
        #1.3有引用
        return fun_name(a,b) 
    #1.4返回内部函数
    return fun_in




#2.定义原函数 表示:加法运算
@my_decorator
def get_sum(a,b):
    return a+b

#3.定义原函数 表示:减法运算
@my_decorator
def get_diff(a,b):
    return a-b


#4.测试
print(get_sum(3,5))
print("*"*20)
print(get_diff(9,1))
