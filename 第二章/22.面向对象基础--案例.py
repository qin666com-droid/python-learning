"""
控制台菜单与用户交互，具体的功能如下:
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过
1.添加学生成绩:根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
2.修改学生成绩:根据输入的学生姓名，修改对应的学生成绩
3.删除学生成绩:根据输入的学生姓名，删除对应的学生成绩
4.查询指定学生成绩:根据输入的学生姓名，查找对应的学生成绩，并输出
5.展示全部学生成绩:展示出系统中所有学生的成绩
"""

#学生类
class Student:
    def __init__(self,name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english

    def __str__(self) :
        return f"姓名:{self.name} | 语文:{self.chinese} | 数学:{self.math} | 英语:{str(self.english)} | 总分:{self.chinese+self.math+self.english} "

    #修改学生成绩
    def update_score(self,chines=None,math=None,english=None):
        if chines is not None :
            self.chinese = chines
        if math is not None :
            self.math = math
        if english is not None :
            self.english = english

#教务管理系统
class EduMan:
    system_version = "1.0"
    system_name = "教务管理系统"
    def __init__(self):
        self.student_list = [] #列表.记录在校学生的成绩

    #添加学生成绩
    def add_student(self):
        name = input("请输入学生的姓名:")
        for s in self.student_list:
            if s.name == name:
                print(f"该学生{name}已经在教务管理系统中")
                return
        chinese = int(input("请输入学生语文成绩:"))
        math = int(input("请输入学生数学成绩:"))
        english = int(input("请输入学生英语成绩:"))
        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            stu =Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("学生添加成功")
        else:
            print("学生成绩必须在0-100之间 !  ")


    #修改学生成绩
    def update_student(self):
        name = input("请输入学生的姓名:")
        for s in self.student_list:
            if s.name == name:
                print(f"当前该学生成绩为:{s}")

                chinese = int(input("请输入学生修改后的语文成绩:"))
                math = int(input("请输入学生修改后的数学成绩:"))
                english = int(input("请输入学生修改后的英语成绩:"))

                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)

                    print("学生修改成功")
                    print(f"修改后的成绩:{s}")
                    return
                else:
                    print("学生成绩必须在0-100之间 !  ")
                    return
        print("未找到该学生,修改失败!")
    #删除学生成绩
    def delete_student(self):
        name = input("请输入学生的姓名:")

        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功!")
                return
        print("未找到该学生,删除失败!")


    #查询指定学生成绩
    def query_student(self):
        name = input("请输入学生的姓名:")

        for s in self.student_list:
            if s.name == name:

                print(f"学生信息:{s}")
                return
        print("未找到该学生!")




    #展示全部学生成绩
    def list_student(self):
        for s in self.student_list:
            print(s)




    def run(self):
        print(f"欢迎使用教务管理系统{EduMan.system_version}")

        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
            print("# 1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.查询所有学生  6.退出系统 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")

            choice = input("\n请选择需要执行的操作,输入1-6:")
            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.delete_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.list_student()
                    case "6":
                        print("bye~")
                        break
                    case _:
                        print("输入错误,请选择1-6之间的菜单功能!")
            except ValueError:
                print("输入的数据有问题,请重新输入!")
            except Exception :
                print("程序运行出错,请重新选择!!")

#测试
if __name__ == "__main__":
    edu_man = EduMan()
    edu_man.run()













# #练习:
# """
# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下:
# 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入
# 完成后修改该商品信息。
# 3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商
# 品数量:xxx”。
# 5.退出购物车
# """
# from random import choice
# from traceback import print_tb
# from unittest import case
#
#
# #商品类
# class Goods:
#     def __init__(self,name,price,count):
#         self.name = name
#         self.price = price
#         self.count = count
#
#     def __str__(self):
#         return f"商品名称:{self.name} | 商品价格:{self.price} | 商品数量:{self.count} "
#
#
#
#
#
#
#
#
#
#
#
# #购物车管理系统
# class Shopping:
#     system_version ="1.0"
#     system_name = "购物车管理系统"
#     def __init__(self):
#        self.shopping_list = []  #记录商品信息
#
#     #添加商品
#     def add_shopping(self):
#         name = input("请输入商品名称:")
#         for s in self.shopping_list:
#             if s.name == name:
#                 print(f"该商品{name}已经存在")
#                 return
#
#         price = float(input("请输入商品价格:"))
#         count = int(input("请输入商品数量:"))
#         sg = Goods(name,price,count)
#         self.shopping_list.append(sg)
#         print("商品添加成功")
#
#     #修改商品
#     def update_shopping(self):
#         name = input("请输入商品名称:")
#
#         for s in self.shopping_list:
#             if s.name == name:
#                 print(f"当前商品信息为:{s}")
#
#                 price = float(input("请输入修改后的商品价格:"))
#                 count = int(input("请输入修改后的商品数量:"))
#                 s.price = price
#                 s.count = count
#                 print("商品修改成功")
#                 print(f"修改后的信息为:{s}")
#                 return
#
#         print("改商品不存在,请重新输入!")
#     #删除商品
#     def delete_shopping(self):
#         name = input("请输入商品名称:")
#         for s in self.shopping_list:
#             if s.name == name:
#                 self.shopping_list.remove(s)
#                 print("商品删除成功!")
#                 return
#
#
#         print("该商品不存在,请重新输入!")
#
#     #查询购物车
#     def list_shopping(self):
#         for s in self.shopping_list:
#             print(s)
#
#
#     def run(self):
#         print(f"欢迎使用商品购物车系统{Shopping.system_version}")
#
#         while True:
#             print()
#             print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
#             print("* 1.添加购物车  2.修改购物车  3.删除购物车  4.查询购物车  5.退出购物车 * ")
#             print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ")
#
#             choice = input("\n请输入要执行的操作:")
#
#             match choice:
#                 case "1":
#                     self.add_shopping()
#                 case "2":
#                     self.update_shopping()
#                 case "3":
#                     self.delete_shopping()
#                 case "4":
#                     self.list_shopping()
#                 case "5":
#                     print("bye~")
#                     break
#                 case _:
#                     print("输入错误,请重新输入!")
#
# #测试
# if __name__ == "__main__":
#     shopping = Shopping()
#     shopping.run()





