#元组的基本操作--tuple-->元素可以重复,有序,不可修改

#定义
# t1 = (1,7,56,865,45,2,32,1)
# print(t1)
# print(type(t1))
#
# #索引访问
#
# print(t1[0])
# print(t1[4])
#
# #切片
# print(t1[::2])
#
# #count() 统计元素的个数
# print(t1.count(1))
#
# #index() 获取元素的索引(第一个元素的位置)
# print(t1.index(2))
#
# #注意点:
# #如果定义氮元素的元组,单个元素要加上逗号,如(12,)
# t2 =(100)
# print(t2)
# print(type(t2))#类型为Int
# t3 =(100,)
# print(t3)
# print(type(t3))#类型为tuple





#------------组包和解包-----------------
#组包---元组就相当于一个组包过程
# t1 = (1,34,2,5,6)
# t2 = 1,2,4,5
#
# #解包
# #基础解包:变量数量与容器的元素个数一致
# a,b,x,s=t2
# print(a,b,x,s)# 分别对应
#
# #扩展解包
# k,*m,o=t1 #*收集剩余的元素,并生成列表
# print(k,m,o)# k:1;m:34,2,5;o:6

#案例1:交换两个变量,并输出
# a =1
# b =2
#组包
# t =b,a
# #解包
# # a,b=t
# a,b=b,a
# print(a,b)
#
# #案例2:交换三个变量,并输出
# a = 211
# b = 985
# c = 911
# c,a,b =a,b,c
# print(a)
# print(b)
# print(c)






"""
根据提供的学生成绩单，完成如下需求:
1.计算每个学生的总分、各科平均分，然后一并输出出来。
2.统计各科成绩的最低分、最高分、平均分，并输出。
3.查找成绩优秀(平均分大于90)的学生，并输出。
"""

students =(
        ("S001","wl",85,92,78),
        ("S002", "lmw",92, 88, 95),
        ("S003", "ss", 78, 85, 82),
        ("S004", "zn", 88, 79, 91),
        ("S005", "zy", 95, 96, 89),
        ("S006", "wz", 76, 82, 77),
        ("S007", "hd", 89, 91, 94),
        ("S008", "xlg",75, 69, 82),
        ("S009", "xm", 86, 89, 98),
        ("S0010", "dt",66, 59, 72)

)
# 1.计算每个学生的总分、各科平均分，然后一并输出出来。
#avg --->{avg:.1f} -->保留1位小数!
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
#方式一:
# for i in students:
#     total = i[2]+i[3]+i[4]
#     avg = total/3
#     print(f"{i[0]}\t{ i[1]}\t\t{i[2]}\t\t{i[3]}\t\t{i[4]}\t\t{total}\t\t{avg:.1f}")
#
# print()

#方式二:
for id,name,chinese,math,english in students:
    total = chinese+math+english
    avg = total/3
    print(f"{id}\t{name}\t\t{chinese}\t\t{math}\t\t{english}\t\t{total}\t\t{avg:.1f}")

print()
# 2.统计各科成绩的最低分、最高分、平均分，并输出。

chinese = [i[2] for i in students]
math = [i[3] for i in students]
english = [i[4] for i in students]
print(f"语文最低分:{min(chinese)},最高分:{max(chinese)},平均分:{sum(chinese)/len(chinese):.1f}")
print(f"数学最低分:{min(math)},最高分:{max(math)},平均分:{sum(math)/len(math):.1f}")
print(f"英语最低分:{min(english)},最高分:{max(english)},平均分:{sum(english)/len(english):.1f}")

print()
# # 3.查找成绩优秀(平均分大于90)的学生，并输出。
#方式一:
# for i in students:
#     if (i[2]+i[3]+i[4])/3>90:
#         print(f"优秀学生的学号:{i[0]} ,姓名:{i[1]}")

#方式二:
for id,name,chinese,math,english in students:
    if (chinese+math+english)/3>90:
        print(f"优秀学生的学号:{id} ,姓名:{name},平均分:{(chinese+math+english)/3:.1f}")






