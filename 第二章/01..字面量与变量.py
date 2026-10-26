#  字面量的写法
# print(100)  #整数(int)
# print(3.14) # 浮点数/小数(float)
# print(True) # 布尔(bool)
# print(False) # 布尔(bool)
# print("jjj") # 字符串(str)
# print("--------") # 字符串(str)
# print(None) # 空值(None Type)
#
# # 布尔类型本质也是整数类型
# print(True + 1) # 2
# print(False - 1) # -1

# 变量-->python 是动态类型语言,一个变量可以储存不同类型的数据
# 但,项目开发中,推荐变量只存储一种类型的数据
# num = 224.1
# print(num)
#
# num = num + 1
# print(num)
#
# num = "OK"
# print(num)
#
# num = True
# print(num)

# 案例
# a = 20.7 #基础播放量
# b = 50 # 新增播放量
# print("未来第一个月的播放量: ",a+b,"万")
# print("未来第二个月的播放量: ",a+b+b,"万")
# 案例 -升级;一次性定义多个变量
# a,b=20.7,50
# print("未来第一个月的播放量: ",a+b,"万")
# print("未来第二个月的播放量: ",a+b+b,"万")
#
#
# # 标识符
# true = 1
# print(true)

# 案例 交换两个变量值
# a =10
# b =20
# c = a
# a = b
# b = c
# print(a)
# print(b)

# 案例 交换三个变量值
a = 100
b = 200
c = 300
d = a #d=100
a = c #a=300
c = b #c=200
b = d #b=100
print(a,b,c)