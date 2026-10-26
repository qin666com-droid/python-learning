# # # 获取键盘上输入的数据 input(..)
# # name = input("请输入姓名:")
# # age = input("输入年龄:")
# # print(f"你的姓名是{name},年龄是{age}岁22")
#
# # 案例 银行卡ATM取款
# w = 10000 #总金额
# #1.输入密码
# password = input("输入密码:")
# print(f"密码正确:{password}")
# #2.输入取款金额
# qw = input("输入取款金额:")
# #3.计算余额并输出--> qw 转为int类型 -->int(..)
# print(f"计算余额并输出:{ w - int(qw) }")

# 案例 :根据输入的两个数字,计算和,并输出到控制台
a = input("输入数字:")
b = input("输入数字:")
print(f"计算和:{int(a)+int(b)}")