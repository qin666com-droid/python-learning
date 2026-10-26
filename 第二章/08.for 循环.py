# for循环  :遍历输入的字符串;(遍历每一个元素)
# msg = input("输入要遍历的字符串:")
# for i in msg: #i 表示遍历出来的元素, msg 表示需要遍历的数据
#     print(f"元素: {i}")
# else:
#     print("over")

#练习1:计算1-100间所有奇数之和
# total = 0
# # for i in range(1,101):
# #     if i % 2!=0:
# #         total +=i
#
# # 简化
# for i in range(1,101,2):
#         total +=i
# print(f"1-100间所有奇数之和为:{total}")

#练习2:计算100-500间所有3的倍数的数字之和

# total = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         total +=i
# print(f"100-500间所有3的倍数的数字之和:{total}")






#嵌套循环
#案例: 根据输入的长方形的长度 m,宽度 n, 打印一个长方形
#    print("*") :自带换行效果,每一次执行都会输出新的一行中;
#    print("*",end="") : end便是的是每一次输出以什么结束;默认\n,表示换行

#1.接收键盘录入 m ,n
# 长度
# m = int(input("请输入长度:"))
# #宽度
# n = int (input("请输入宽度:"))
#
# #2.打印长方形
# for a in range(n):  #控制行
#     for i in range(m): #控制列
#         print("*", end="  ")
#
#     print()
#

#练习:打印99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}x{i}={j*i}",end="\t")
#     print()

#练习1:根据输入的直角边的边长,打印等腰直角三角形
#
# a = int(input("请输入直角边的边长:"))
# for i in range(1,a+1):
#     for j in range(i):
#         print("*",end="\t")
#     print()

#练习2:根据输入的数字,打印对应的数字金字塔

# a = int(input("请输入数字:"))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#练习3:打印国际象棋棋盘
#
# a = 8
#
# for i in range(a):
#     for j in range(a):
#         if (i+j) % 2==0:
#             print("■",end="\t")
#         else:
#             print("□",end="\t")
#     print()



