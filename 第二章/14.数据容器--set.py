#集合 --> 无序,不可重复,可修改
#定义
# a = {1,243,2,3,2,53,64,43,1}
# print(a)
# print(type(a))
#
# #空集合
# s =set()
# print(s)
# print(type(s))






#
# #常见方法:
# #add():添加元素到集合
# a = {1,243,2,3,2,53,64,43,1}
# print(a)
#
# a.add(342)
# print(a)
#
# #remove(): 移除集合中的指定元素(指定元素不存在将报错)
# a.remove(342)
# print(a)
#
# # a.remove(3221)
# # print(a)# 控制台报错!
# #pop() :  随机删除集合中的元素并返回
# c =a.pop()
# print(c)
# print(a)
#
# #clear():  清空集合
# a.clear()
# print(a)
#
# #difference():  将两个集合的差集(存在于第一个集合,但不存在于第二个集合)
# s1 = {"A","B","C","D","E","F","G"}
# s2 = {"A","B","C","R"}
# print(s1.difference(s2))
# print(s2.difference(s1))
# #union():  求取两个集合的并集
# print(s1.union(s2))
# print(s2.union(s1))
#
# #intersection():  求取两个集合的交集
# print(s1.intersection(s2))
# print(s2.intersection(s1))




"""
根据提供的班级学生的选课情况，完成如下需求:
1.找出同时选修了法语和艺术的学生
2.找出同时选修了所有四门课程的学生
3.找出选修了足球，但是没有选修篮球的学生
4.统计每一个学生选修的课程数量
"""
#选秀足球名单
football = {"张三","妞妞","石原","七森","方圆","白夜"}
#选秀篮球名单
basketball = {"白夜", "希望", "永美", "张开", "方圆"}
#选秀法语名单
french = {"白夜","莉莉","张宁","希望","张开","张问"}
#选秀艺术名单
art = {"白夜","七森","三优","莉莉","石原","妞妞"}

# 1.找出同时选修了法语和艺术的学生
#方式一:
# fa =french.intersection(art)
# print(f"同时选修了法语和艺术的学生:{fa}")
#方式二:&-->与(交集)
fa1 = french & art
print(f"同时选修了法语和艺术的学生:{fa1}")

# 2.找出同时选修了所有四门课程的学生
all = french & basketball &football & art
print(f"同时选修了所有四门课程的学生:{all}")

# 3.找出选修了足球，但是没有选修篮球的学生--差集
#方式一:
# fb =football.difference(basketball)
# print(f"选修了足球，但是没有选修篮球的学生:{fb}")

#方式二:- --->减号(差集)
# fb = football - basketball
# print(f"选修了足球，但是没有选修篮球的学生:{fb}")

#方式三:集合推导式 -->快速构建集合,语法:{要往集合中添加的数据 for s in set if 条件}
fb = {s for s in football if s not in basketball}
print(f"选修了足球，但是没有选修篮球的学生:{fb}")

# 4.统计每一个学生选修的课程数量
#4.1 获取所有学生名单 -- 并集(|)
# total0 =football.union(basketball).union(french).union(art)
# print(total0)
total = french | basketball | football | art
print(total)
#4.2 获取每一个学生选修的课程数量
total_list =[*football,*basketball,*french,*art]#解包
for s in total:
    print(f"{s} 选修了{total_list.count(s)}个课程")



