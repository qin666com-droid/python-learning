#字符串 -->不可变的(无法修改),有序性,可迭代性
# 基本操作

# s ="hello world"
# print(s[2])  #正向索引
# print(s[-3]) #反向索引
#
# for i in s:
#     print(i)
#
# #切片
#
# print(s[0:5:1])
# print(s[:5:1])
# print(s[:5])
# #步长 -->正数:从前往后截取;负数:从后往前截取
# #(方向得一致)
# print(s[0:4:-1]) #反向冲突,截取失败
# print(s[-1:-7:-1])
# print(s[::-1])


#------------------常用方法----------------
"""
find() 在字符串中查找子串，返回第一次出现的索引位置，
        找不到返回-1
count() 统计子串在字符串中出现的次数
upper() 将字符串中的所有字母转换为大写
lower() 将字符串中的所有字母转换为小写
split() 将字符串按指定分隔符分割成列表
strip() 去除字符串两端的空白字符或指定字符
replace() 将字符串中的指定子串替换为新的子串
startswith()/endwith()
            检查字符串是否以指定子串开头/结尾，
              返回布尔值
"""
# a = "  hello-world-lalalala"
#
# index = a.find("l")
# print(index)
#
# c =a.count("l")
# print(c)
#
# su = a.upper()
# print(su)
#
# us = a.lower()
# print(us)
#
# sl = a.split("-")
# print(sl)
#
# ss = a.strip()
# print(ss)
#
# zh = a.replace("-", " ")
# print(zh)
#
# print(a.startswith("l"))
# print(a.endswith("l"))
#
# print("---------")
# print(a)

#----------字符串-案例-------------------
#案例1 :邮箱验证:用户输入一个邮箱,验证格式是否正确
#(包含一个@和至少一个'.')
# mail = input("输入邮箱:")
# if mail.count("@") == 1 and mail.count(".") >=1:
#     print(f"{mail}格式正确")
# else:
#  print(f"{mail}格式错误")


#方式二: in 运算符 -->判断子串是否存在字符串中
# mail = input("请输入邮箱:")
# if mail.count("@") ==1 and "." in mail:
#  print(f"{mail}格式正确")
# else:
#  print(f"{mail}格式错误")


#练习1:输入字符串,判断该串是否回文(两边对称)
# a = input("请输入:")
# # b = input("请输入:")
# if a [::]==a[::-1]:
#     print(f"{a}回文")
# else:
#     print(f"{a}不对称")


#练习2: 将输入的10个字符串,反转后全部转为大写
#并记录在列表里,最后将其遍历输出
# a= input("输入字符串:")
#定义一个空的列表
list1 = []
#循环输入10次字符串
for i in range(1,11):
    text = input(f"第{i}个字符串:")
    #先用切片反转,再变大
    text =text[::-1].upper()
    #将结果添加到列表中
    list1.append(text)
#对列表进行遍历并输出
for i in list1:
    print(i)



