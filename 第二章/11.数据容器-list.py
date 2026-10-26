# #列表操作
# #定义
# a = [5,6,True,99,"shit"]
# print(type(a))
#
# #访问列表元素
# #获取
# print(a [0]) #正向索引,从0开始
# print(a [-1]) #反向索引,从-1开始
#
# #修改
# # 指定的索引如果超出范围,就会报错 list assignment index out of range
#
# a[1] ="nice"
# print(a)
#
# #删除
# del a[0]
# print(a)
#
# #遍历
# for item in a:
#     print(item)
#
#
#

#----------------列表 list 切片-------------------
#定义列表
# a =["A","B","C","D","E","F","G","H","I","J"]
#
# #切片操作 a[开始索引:结束索引:步长]
# print(a [0:6:1])
# print(type(a[0:6:1]))
# print(a[0:-1:1])

#----------------列表 list 常用方法-----------------

#列表定义
# s= [5,66,78,8,99,789,520,1314,1209]
# print(s)
# # append() : 在列表尾部追加元素
# s.append(5211)
# print(s)
#
# # insert() : 在指定索引之前,插入元素
# s.insert(1,65)
# print(s)
#
# # remove() : 移除列表中第一个匹配到的元素
# s.remove(65)
# print(s)
#
# # pop()  : 删除列表中指定索引位置的元素并返回(如果为指定,默认删除最后一个)
# s.pop(0)
# print(s)
#
# e = s.pop(1)
# print(e)
#
# s.pop(2)
# print(s)
#
# # sort () : 对列表进行排序(列表元素的数据类型一致,才可以进行排序)
# s.sort()
# print(s)
#
# # reverse () :反转列表元素
# s.reverse()
# print(s)




#------------------------列表 list 案例-----------------
#案例1. 输入10个数字,存储到一个列表中,并将其排序
#输出其中的最小值,最大值和平均值
# # 1.定义列表
# num_list = []
# #2.将输入的数字存到列表中
#
# for i in range(10):
#     num = int(input("请输入数字:"))
#     num_list.append(num)
#
# print("列表为:",num_list)
# #3.对列表进行排序
# num_list.sort()
# print("排序后的列表为:",num_list)
# #4.输出其中的最小值,最大值和平均值
# #--->sum()  求和  ;len() 获取元素的个数(列表的长度)
# print("最小值为:",num_list[0])
# print("最大值为:",num_list[-1])
# print("平均值为:",sum(num_list)/len(num_list))


# #案例2.合并列表并删除重复的
#
# list1 = [1,22,4,88,66,22,5,7,9,1]
# list2 = [55,88,33,77,64,5,7,9,725]
#
# for num in list1:
#     list2.append(num)
# print("合并后的列表:",list2)
#
# list = []
# for num in list2:
# #判断list中是否存在num元素,若不存在,再添加
#     if num not in list :
# #判断元素是否存在于列表中,如果存在,则返回True;不存在,返回False
#         list.append(num)
# print("删除重复后的列表:",list)


#案例2(简化版!).合并列表并删除重复的

# list1 = [1,22,4,88,66,22,5,7,9,1]
# list2 = [55,88,33,77,64,5,7,9,725]
#
# #解包:将列表这一类容器解开成一个个独立的元素
# #组包:将多个值合并到一个容器
# new_list = [*list1,*list2]
# #或者!!!  new_list = list1+list2
# print("合并后的列表:",new_list)
#
# list = []
# for num in list2:
# #判断list中是否存在num元素,若不存在,再添加
#     if num not in list :
# #判断元素是否存在于列表中,如果存在,则返回True;不存在,返回False
#         list.append(num)
# print("删除重复后的列表:",list)




#案例3:生成1-20的平方列表
#方法一
# new_list = []
# for i in range(1,21):
#     new_list.append(i**2)
# print(new_list)

#方法二 列表推导式-->就是按照一定的规则快速生成一个列表的方法
#-->语法格式1:[ 要插入的值 for i in 序列/列表]
# new_list = [ i**2 for i in range(1,21)]
# print(new_list)

#案例4:从一个数字列表中提取索引偶数,并计算其平方,并生成新列表
#列表推导式-->就是按照一定的规则快速生成一个列表的方法
#-->语法格式2: [要插入的值 for i in 序列/列表 if 条件]
# list1 = [2,5,65,4,652,46,87,95,32,21,12]
# new_list = [i**2 for i in list1 if i%2 == 0]
# print(new_list)


#练习1:将下列多个列表合并为一个列表,并去重,升序后输出
# list1 =['A','P','W','S','B','E','M','Q','X','L']
# list2 =['V','D','G','A','S','O','C','B']
# list3 =['P','D','W','M','E','H']
# for i in list1:
#     list2.append(i)
# for u in list2:
#         list3.append(u)
# new_list =[]
# for i in list3:
#     if i not in new_list:
#         new_list.append(i)
# new_list.sort()
# print(new_list)

#练习2: 将下列表中能被3或5整除的元素提取出来,并获取
#这些数字对应的平方,组成一个新的列表
# list1 = [32,34,35,25,15,64,67,63,70,78,76,56,65,45
#          ,30,66,99,568,565,456,635,769,542,355]
# list2 = []
#
# for i in list1:
#     if i  % 3 ==0 or i % 5 ==0:
#
#         list2.append(i**2)
# print(list2)

#练习3: 将列表中的正数提取出来,封装为一个新的列表

list1 = [3,-5,34,-4,43,-562,32,-432,432,-32,12,-32]
new_list = []
for i in list1:
    if i>0:
        new_list.append(i)
print(new_list)


