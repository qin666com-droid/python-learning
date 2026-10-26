# #定义类 --> 不推荐 动态为对象添加属性
# class Car:
#     pass
#
#
# #创建对象
# c1 = Car()
# #动态为对象添加属性
# c1.color = "red"
# c1.brand = "BWM"
# c1. name = "X5"
# c1.price = 99999
#
# print(c1)
# print(c1.__dict__)




# # 定义类
# class Car:
# #   __init__ 方法是初始化的方法,会在对象中创建时自动调用,可以在该方法中
# #            为对象设置对应的属性
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         self.c_color = c_color
#         self.c_brand = c_brand
#         self.c_name = c_name
#         self.c_price = c_price
#         print("Car 类型的对象初始化完毕,对象属性已经添加完毕")
#
# #创建对象
# c1 =Car("red","BWM","X8",88888)
# print(c1.__dict__)


#---------------------定义类  实例方法--------------------
# class Car:
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.c_color = c_color
#         self.c_brand = c_brand
#         self.c_name = c_name
#         self.c_price = c_price
#         print("Car 类型的对象初始化完毕,对象属性已经添加完毕")
#
#     #定义实例方法
#     def running(self    ):
#         print(f"{self.c_brand} {self.c_name} 正在高速行驶中...")
#     def total_price(self,discount,rate):
#         """
#         计算车的总费用,包括:价格和税费
#         :param discount:折扣
#         :param rate:税率
#         :return:总费用
#         """
#         total_price = discount  * self.c_price + rate * self.c_price
#         return total_price
#
# c1 =Car("red","BWM","X8",88888)
#  # 调用对象中的方法
# c1.running()
#
# total = c1.total_price(0.9,0.05)
# print(total)






#-------------------------------魔法方法------------------------------
# class Car:
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.c_color = c_color
#         self.c_brand = c_brand
#         self.c_name = c_name
#         self.c_price = c_price
#         print("Car 类型的对象初始化完毕,对象属性已经添加完毕")
#
#     #定义实例方法
#     def running(self    ):
#         print(f"{self.c_brand} {self.c_name} 正在高速行驶中...")
#     def total_cost(self,discount,rate = 0.1):
#         total_cost = discount * self.c_price + rate * self.c_price
#         return total_cost
#
# #   魔法方法
#     def __str__(self):
#         return f"{self.c_color} {self.c_brand} {self.c_name} {self.c_price}"
#     def __eq__(self, other):
#         return self.c_color == other.c_color and self.c_brand == other.c_brand and self.c_name == other.c_name and self.c_price == other.c_price
#     def __lt__(self, other):
#         return self.c_price < other.c_price
#
#
#
#
# #测试
# c1 = Car("白色","BYD","秦",60000)
# print(c1)
#
# c2 = Car("白色","BYD","秦",600000)
# print(c2)
#
# print(c1 == c2)
#
# print(c1<c2)


#----------------------------实例属性 与 类属性----------------------
# class Car:
#     # 类属性(所有实例对象共享的)
#     wheel = 4  #轮胎数量
#     tax_rate = 0.1 # 购置税税率
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         #实例属性
#         self.c_color = c_color
#         self.c_brand = c_brand
#         self.c_name = c_name
#         self.c_price = c_price
#         # self.wheel = 2
#         print("Car 类型的对象初始化完毕,对象属性已经添加完毕")
#
#     #定义实例方法
#     def running(self    ):
#         print(f"{self.c_brand} {self.c_name} 正在高速行驶中...")
#     def total_cost(self,discount,rate = 0.1):
#         total_cost = discount * self.c_price + rate * self.c_price
#         return total_cost
#
# c1 = Car("白色","BYD","秦",60000)
# print(c1.total_cost(0.8) )
# print(c1.wheel) #通过实例对象查找属性时,先查找实例属性,其不存在,再查找类属性
# # c2 = Car("白色","BYD","秦",600000)
# # print(c2)
#
# #通过类名访问类属性
# print(Car.wheel)






















