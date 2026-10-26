# # """
# #
# # #1.无参无返回的原函数
# #
# # #细节:
# #     装饰器的内部函数格式 要和 被装饰的原函数 保持一致
# #     既:原函数是无参无返回的,则 装饰器的颞部函数也必须是 无参无返回的
# #         原函数有参有返回的,则 装饰器的内部函数也必须是 有参有返回的
# # """
# #
# # #需求:定义无参无返回值的 get_sum()求和函数,在不改变其代码的基础上,添加友好提示:正在努力计算
# # #1. 定义装饰器
# # def my_decorator(fun_name):
# #     #1.1定义内部函数,其格式必须和 被装饰的原函数 保持一致
# #     def fun_in():
# #         #1.2添加额外功能
# #         print("正在努力计算中....")
# #
# #
# #     #1.3调用原函数
# #         fun_name()
# #     #1.4返回内部函数(对象)
# #     return fun_in
# # #2.定义原函数
# # @my_decorator
# # def get_sum():
# #     a=10
# #     b=20
# #     sum=a+b
# #     print(sum)
# #
# # #3.测试
# # #3.1传统方式
# # # get_sum = my_decorator( get_sum)
# # # get_sum()
# #
# #
# #
# #
# # #3.2语法糖
# # get_sum()
#
# """
#




# #2.有参无返回的原函数
#
# #细节:
#     装饰器的内部函数格式 要和 被装饰的原函数 保持一致
#     既:原函数是无参无返回的,则 装饰器的颞部函数也必须是 无参无返回的
#         原函数有参有返回的,则 装饰器的内部函数也必须是 有参有返回的
# """
#
# #2.需求:定义有参无返回值的 get_sum()求和函数,在不改变其代码的基础上,添加友好提示:正在努力计算
# #1. 定义装饰器
# def my_decorator(fun_name):
#
#
#     #1.1定义内部函数,其格式必须和 被装饰的原函数 保持一致
#         def fun_in(x,y):
#
#         #1.2添加额外功能
#             print("正在努力计算中....")
#
#     #1.3调用原函数
#             fun_name(x,y)
#     #1.4返回内部函数(对象)
#         return fun_in
# #2.定义原函数
# @my_decorator
# def get_sum(a,b):
#
#     sum=a+b
#     print(sum)
#
# #3.测试
# #3.1传统方式
# # get_sum = my_decorator(get_sum)
# # get_sum(1,2)
#
# #3.2语法糖
# get_sum(1,2)
#
#

# # #细节:
# #     装饰器的内部函数格式 要和 被装饰的原函数 保持一致
# #     既:原函数是无参无返回的,则 装饰器的颞部函数也必须是 无参无返回的
# #         原函数有参有返回的,则 装饰器的内部函数也必须是 有参有返回的
# # """
# 3.无参有返回的原函数 get_sum()求和函数,在不改变其代码的基础上,添加友好提示:正在努力计算
#1. 定义装饰器
# def my_decorator(fun_name):
# #1.1定义内部函数
#     def fun_in():
#         #1.2额外功能
#         print("正在计算中....")
#         #1.3 有引用
#         return fun_name()
#     return fun_in
#
# @my_decorator
# def a_sum():
#     a =10
#     b =20
#     return a+b
#
# # a_sum = my_decorator(a_sum)
# # sum = a_sum()
# a=a_sum()
# print(a)


# # #细节:
# #     装饰器的内部函数格式 要和 被装饰的原函数 保持一致
# #     既:原函数是无参无返回的,则 装饰器的颞部函数也必须是 无参无返回的
# #         原函数有参有返回的,则 装饰器的内部函数也必须是 有参有返回的
# # """
# 4.有参有返回的原函数 get_sum()求和函数,在不改变其代码的基础上,添加友好提示:正在努力计算

#1. 定义装饰器
# def my_decorator(fun_name):
#     #1.1定义内部函数
#     def fun_in(x,y):
#         #1.2额外功能
#         print("正在努力计算中....")
#         #1.3 有引用
#         return fun_name(x,y)
#     return fun_in
# #2.定义原函数
# @my_decorator
# def get_sum(a,b):
#     sum=a+b
#     return sum
# #3.测试
# #3.1传统方式
# # get_sum = my_decorator(get_sum)
# # sum = get_sum(1,2)
# # print(sum)
# #3.2语法糖
# print(get_sum(1,2))




# # #细节:
# #     装饰器的内部函数格式 要和 被装饰的原函数 保持一致
# #     既:原函数是无参无返回的,则 装饰器的颞部函数也必须是 无参无返回的
# #         原函数有参有返回的,则 装饰器的内部函数也必须是 有参有返回的
# # """

#需求:定义一个可以计算多个数据和字典value的函数,并添加友好提示:正在努力计算
#1. 定义装饰器
def my_decorator(fun_name):
    #1.1定义内部函数,其格式必须和 被装饰的原函数 保持一致
    def fun_in(*args,**kwargs):
        #1.2添加额外功能
        print("正在努力计算中....")
        #1.3调用原函数
        return fun_name(*args,**kwargs)
    #1.4返回内部函数(对象)
    return fun_in
#2.定义原函数
@my_decorator
def get_sum(*args,**kwargs):
    """
    计算 数字列表和字典value的和
    :param args: 数字列表 *args -->接收所有的位置参数,封装到元组
    :param kwargs: 字典,键是字符串,值是数字 **kwargs -->接收所有的关键字参数,封装到字典
    :return: 结果之和
    """
    # #2.1定义求合变量
    # sum = 0
    # #2.2遍历args,获取每个元素,求和
    # for i in args:
    #     sum += i
    # #2.3遍历字典,获取到每个值
    # for k,v in kwargs.items():
    #     sum += v
    # #2.4返回结果
    # return sum
    #优化如下
    return sum(args) + sum(kwargs.values())
#3. 测试
print(get_sum(1,2,3,a=10,b=20))












