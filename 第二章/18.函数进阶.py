#-----------------------函数 - 变量的作用域---------------------------
#全局变量 : 在函数外部 或 函数的内部都是可以访问的
# num = 36
# def circle_area(radius):
#     #局部变量: 只能在函数内部使用
#     area = 3.14 * radius**2
#
#     # #局部变量 num
#     # num = 4444
#     # print("num=",num) #4444
#     global num
#     num = 36
#     print("num=" ,num) #36
#     return area
#
#
# #调用函数
# print("num=",num) # 36
# print(circle_area(10))


#----------------- 函数-传参方式------------------
#定义函数
# def reg_stu(name,age,gender,city):
#     print(f"注册成功,姓名: {name},年龄: {age},性别: {gender},城市: {city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}
#
#
# #传参方式一:位置传参
# stu = reg_stu("撒撒",11,"nan",city="北京")
# print(stu)
#
#
# #传参方式二:关键字传参
# stu = reg_stu(name="sd",gender="nan",age=21,city="nan")
#
# print(stu)
#
#
# #传参方式三: 位置传参+关键字传参
# #-->位置参数在前,关键字参数在后
#
# stu = reg_stu("ds",55,gender="nv",city="nv")
# # print(stu)
#
# #----------------------默认参数-----------------------------------
# #定义函数
# def reg_stu(name,age,gender = "男",city ="魔都"):
#         print(f"注册成功,姓名: {name},年龄: {age},性别: {gender},城市: {city}")
#         return {"name":name,"age":age,"gender":gender,"city":city}
#
# #调用函数
# stu = reg_stu("wan",20)
# print(stu)
#
# stu = reg_stu("wang",20,gender="nv")
# print(stu)
#
#
# stu = reg_stu("wanlo",20,gender="nv",city="beijing")
# print(stu)







#-----------不定长参数---------------------------------
#位置参数  -->  *args -->元组


#需求:根据传入的数据,计算这批数据的最大值,最小值,平均值

# def cal_data(*args):
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args)/len(args)
#     return min_data,max_data,round(avg_data,1)
# print(cal_data(5,6,8,9,20))

# #关键字参数  --> **kwargs -->字典
#
# def cal_data(*args,**kwargs):
#     """
#     根据传入的数据,计算这批数据的最大值,最小值,平均值
#     :param args: 不定长位置参数,需要计算的这批数据
#     :param kwargs:不定长关键字参数
#     round : 保留的小输位个数
#     print :是否打印输出
#     :return:最小值,最大值.平均值
# #     """
# #     min_data = min(args)
# #     max_data = max(args)
# #     avg_data = sum(args)/len(args)
# #     if kwargs.get("round") is not None:
# #         avg_data = round(avg_data,kwargs.get("round"))
# #     if kwargs.get("print") :
# #         print(f"{min_data},{max_data},{avg_data}")
# #     return min_data,max_data,avg_data
# # print(cal_data(5,6,8,9,20,round = 2,print = True))
# #
# # print(cal_data(2,6,465,48,45,21,31,64))





#函数的参数类型
#加
# def add(a,b):
#     return a+b
#
# #减
# def sub(a,b):
#     return a-b
#
#
# #乘
# def mul(a,b):
#     return a*b
#
#
# #除
# def div(a,b):
#     return a/b
#
# #计算
# def calc(a,b,oper):
#     return oper(a,b)
#
# print(calc(2,3,add))
#
# print(calc(2,3,sub))
# print(calc(2,3,mul))
# print(calc(2,3,div))






 #-------------------------------------匿名函数----------------------
#需求1:打印一个分割线
# def out_line():
#     print("----------------------")
#
# line = lambda :print("---------------------------")
# line()




#需求2:计算两数之和
# def add(a,b):
#     return a+b

# add = lambda a,b:a+b
# print(add(4,5))


#需求3:对列表进行排序操作,按照字符个数,从小到大排序
# data_list=["C++","Go","C","Java","JavaScript","Python","Rust"]
# print(data_list)
#
# data_list.sort( key=lambda item: len(item))#匿名函数典型的应用场景
#
#
# print(data_list)



#-------------------------------案例---------------------------
#案例1:定义一个函数,根据传入的数字,计算该数字阶乘的结果
#递归调用:在函数中自己调用自己的情况 -->一定得有终结点,否则会陷入死循环
# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         return n*jc(n-1)
#
# a = jc(5)
# print(a)

"""
 案例3:定义一个函数，用于根据传入的一批商品信息
 (商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额
具体规则如下:
-优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
-积分抵扣需要商品总金额满5000才可以使用，
100 积分抵扣1元(且抵扣金额不能超过商品总价，积分只能整百抵扣)。
"""
# def clac(*args, coupon=0,sc=0,ed=0):
#     """
#     根据传入的一批商品信息
#  (商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额
#     :param args: 商品信息(商品名、价格、数量)-->("莉莉",7777777,1)
#     :param coupon: 优惠券
#     :param sc: 积分抵扣
#     :return: 订单的总金额
#     """
#     #订单的总金额 = 商品总金额-优惠券-积分抵扣+运费
#     #1.计算商品的总金额
#     total = [goods[1] * goods[2] for goods in args]
#     total_cost = sum(total)
#     #2.加减优惠券
#     if total_cost >= 5000 and coupon <= total_cost:
#         total_cost = total_cost - coupon
#
#     #3.使用积分抵扣
#     if total_cost > 5000 and sc // 100 <=total_cost:
#         total_cost = total_cost - sc // 100
#
#     #4.加减运费
#     total_cost +=ed
#
#
#     #5.计算订单的总金额
#     return total_cost
#
# toc = clac(("七森莉莉",7777777,1),coupon = 3000,ed =999)
# print(toc)

