# if条件判断
# 案例
# score = 600
# if score > 680:
#     print("欢迎你来到京北大学!!")
#
# print("!!!!!!")
#
# # if  案例:完成登录功能(账号密码:18888888888/666888)
# #1 接收用户输入的账号和密码
# account = 18888888888
# password = 666888
#
# account1 = int(input("输入账号"))
# password1 = int(input("输入密码"))
# #2 判断账号和密码是否全部正确,若正确,则登录成功
# if account1 == account and password1 == password:
#     print("账户正确")
#     print("成功登录!!!")
# #3 判断账号和密码是否有错误,若有任何一个错误,则登录吃白,提示错误信息
# if account1 != account or password1 != password:
#     print("账户错误")
#     print("账号或密码错误!!!")

# if..else..案例:完成登录功能(账号密码:18888888888/666888)
#1 接收用户输入的账号和密码
# account = 18888888888
# password = 666888
#
# account1 = int(input("输入账号"))
# password1 = int(input("输入密码"))
# #2 判断账号和密码是否全部正确,若正确,则登录成功
# if account1 == account and password1 == password:
#     print("账户正确")
#     print("成功登录!!!")
# #3 判断账号和密码是否有错误,若有任何一个错误,则登录吃白,提示错误信息
# else:
#     print("账户错误")
#     print("账号或密码错误!!!")

# 案例:判断输入的年份是否为闰年/平年
# year = int(input("输入年份"))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

#练习1:判断输入的数字是奇数还是偶数
# a = int(input("请输入数字:"))
# if a%2 ==0:
#     print("为偶数")
# else:
#     print("为奇数")

#练习2:判断输入的年龄是否成年(>=18,成年)
# age = int(input("请输入年龄:"))
# if age >= 18:
#     print("已成年")
# else:
#     print("未成年")
#练习3:判断输入的数字是正数还是负数(不考虑0)
# a = float(input("请输入数字"))
# if a >0 :
#     print("是正数")
# elif a<0 :
#     print("是负数")
# else:
#     print("为0")
#练习4:判断分数是否及格(>=60,及格)
# score = int(input("请输入分数:"))
# if score >=60:
#     print("及格!")
# else:
#     print("不及格!!!")

# 多条件判断 案例:判断账户登录--admin/111  root/222  qq/333
# username = input("输入账号")
# password = input("输入密码")
# if username =="admin" and password =="111":
#     print("nice!!!")
# elif username == "root" and password == "222":
#     print("nice!!!")
# elif username =="qq" and password =="333":
#     print("nice!!!")
# else:
#     print("NO!!!")


#练习:判断成绩等级
#>=85 优秀;60-85 及格;否则不及格
# score =int(input("请输入成绩:"))
# if score >=85:
#     print("优秀")
# elif 60<= score <85:
#     print("及格")
# else:
#     print("不及格")

#练习:根据总额和折扣规则,付款
#>=500 8折;>=300,<500 9折;>=100,<300 95折;<100 无折扣
# num = float(input("请输入总金额"))
# if num >=500:
#     print(f"打8折,实际应付金额为{num * 0.8}")
# elif 300<=num<500:
#     print(f"打9折,实际应付金额为{num * 0.9}")
# elif 100<=num<300:
#     print(f"打95折,实际应付金额为{num * 0.95}")
# else:
#     print(f"无折扣,应付{num}")
"""
# 案例:根据输入的边长,判断是等边/等腰/普通三角形,
#  还是不能构成三角形
1.两边之和大于第三边
2.三边相等--等边
两边相等--等腰
三边不等--普通
"""   # pass 空语句,起到语法占位的作用
# a = int(input("请输入第一个边长:"))
# b = int(input("请输入第二个边长:"))
# c = int(input("请输入第三个边长:"))
# if a+b>c and a+c>b and b+c>a:
#     if a==b and b==c:
#         print("为等边三角形!")
#     elif (a==b and b!=c) or (a==c and c!=b) or (b==c and c!=a):
#         print("为等腰三角形!")
#     else:
#         print("为普通三角形.")
# else:
#     print("不能构成三角形!")

#练习:根据用电度数,计算电费
#第一档:<=2880,单价0.4883元/度
#第二档:>2880,<=4800,单价0.5383元/度
#第三档:>4800,单价0.7883元/度
# a = float(input("请输入该月用电量:"))
# if a<=2880:
#     print(f"该月应付{a * 0.4883}元")
# elif 2880< a <=4800:
#     print(f"该月应付{a * 0.5383}元")
# else:
#     print(f"该月应付{a * 0.7883}元")


