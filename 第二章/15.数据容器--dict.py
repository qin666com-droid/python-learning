#字典 -- key 不能重复(若重复,后面的值会覆盖前面的值!!!),
#       key必须是不可变类型(str,int float,tuple)
#定义
# dict1 ={"七森":521,"邱邱":650,"扶苏":666,}
# print(dict1)
# print(type(dict1))
# #key必须是不可变类型(str,int float,tuple),不能是list,set,dict!!!
#
# # dict2 ={"七森":521,"邱邱":650,5:666,}
#
#
# #访问
# print(dict1["七森"]) #获取
# dict1["七森"] = 777  # 修改
# print(dict1)





#----------------------字典 常见操作---------------------------
# dict1 ={"七森":521,"邱邱":650,"扶苏":666}
# print(dict1)
#
# #添加 - key不存在就是添加
# dict1["乔松"]=777
# print(dict1)
#
# #修改- key存在就是修改
# dict1["乔松"]=1314
# print(dict1)
# #查询
# print(dict1["乔松"]) #根据key 获取value
# print(dict1.get("乔松")) # 根据key 获取value
#
# print(dict1.keys()) # 获取所有的key
# print(dict1.values()) # 获取所有的value
# print(dict1.items()) # 获取所有的键值对 key :value
#
# #删除
# sc = dict1.pop("七森")
# print(sc)
# print(dict1)
#
# del dict1["乔松"]
# print(dict1)
#
# # 遍历
# for l in dict1.keys():
#     print(f"{l} :{dict1[l]}")
#
# for item in dict1.items():
#      print(f"{item[0]} :{item[1]}")
#
# for k,v in dict1.items():
#     print(f"{k} :{v}")



#--------------------------------案例------------------------------------
"""
通过控制台菜单与用户交互。具体功能如下:
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据
1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
5.退出购物车

结构:shopping_cart = { 商品:{价格:  ,数量:  },xx:{...}}
"""
from operator import concat, countOf
from random import choice

# shopping_cart = {}
# print("欢迎使用购物车管理系统 ~")
#
# while True:
#     # 1.制作菜单
#
#     # shift+alt  控制多行!!!
#     menu = """
#     ##############################
#     #         1.添加购物车         #
#     #         2.修改购物车         #
#     #         3.删除购物车         #
#     #         4.查询购物车         #
#     #         5.退出购物车         #
#     ##############################
#     """
#     print(menu)
#
#     # 2.执行的具体操作
#     choice = input("请选择要执行的操作(1-5):")
#
#     match choice:
#         case "1":  # 添加购物车
#             gname = input("请输入商品名称:")
#             gprice = float(input("请输入商品价格:"))
#             gnum = int(input("请输入商品数量:"))
#
#             # 如果商品存在,则不执行添加,提示信息
#             if gname in shopping_cart:
#                 print("该商品已存在 !")
#             else:
#                 shopping_cart[gname] = {"price": gprice, "num": gnum}
#                 print("商品添加完毕!")
#         case "2":  # 修改购物车
#             gname = input("请输入需要修改商品名称:")
#             if gname not in shopping_cart:
#                 print("商品不存在,请重新选择!")
#                 continue
#             gprice = float(input("请输入商品最新价格:"))
#             gnum = int(input("请输入商品最新数量:"))
#             # 如果商品不存在,则提示错误信息,重新选择
#
#
#             shopping_cart[gname] = {"price": gprice, "num": gnum}
#             print("商品修改完毕!!!")
#         case "3":  # 删除购物车
#             gname = input("请输入需要删除的商品名称:")
#             if gname not in shopping_cart:
#                 print("商品不存在,请重新选择!!!")
#             else:
#                 del shopping_cart[gname]
#                 print("商品删除完毕!!!!")
#         case "4":  # 查询购物车
#             for gname in shopping_cart.keys():
#                 Gname = shopping_cart[gname]
#                 print(f"该商品名称为:{gname},商品价格为:{Gname["price"]},商品数量为:{Gname["num"]}")
#         case "5":  # 退出购物车
#             print("bye~")
#             break
#         case _:  # 匹配其他所有清空
#             print("非法操作,不支持!!!!!!!")

#
#
# """
# 通过控制台菜单与用户交互。具体功能如下:
# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据
# 1.添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2.修改购物车:要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3.删除购物车:要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4.查询购物车:将购物车中的商品信息展示出来，格式为:"商品名称:xxx，商品价格:xxx，商品数量:xxx"。
# 5.退出购物车
#
# 结构:shopping_cart = { 商品:{价格:  ,数量:  },xx:{...}}
# """
#
# shopping_cart = {}
# print("欢迎来到购物车管理系统!")
# while True:
#     menu = """
#     *******************************************
#     *                 1.添加购物车              *
#     *                 2.修改购物车              *
#     *                 3.删除购物车              *
#     *                 4.查询购物车              *
#     *                 5.退出购物车              *
#     *******************************************
#     """
#     print(menu)
#     choice = input("请选择步骤(1-5):")
#     match choice:
#         case "1":
#             gname = input("请输入商品名称:")
#             gprice = float(input("请输入商品价格:"))
#             gnum = int(input("请输入商品数量:"))
#             if gname in shopping_cart:
#                 print("商品已存在,请重新输入!")
#             else:
#                 shopping_cart[gname] = {"price": gprice, "num": gnum}
#                 print("商品添加成功!")
#         case "2":
#
#             gname = input("请输入需要修改的商品名称:")
#             if gname not in shopping_cart:
#                 print("商品不存在,请重新选择!")
#                 continue
#             gprice = float(input("请输入需要修改的商品价格:"))
#             gnum = int(input("请输入需要修改的商品数量:"))
#
#             shopping_cart[gname] = {"price": gprice, "num": gnum}
#             print("修改完毕!")
#         case "3":
#
#             gname = input("请输入需要删除的商品名称:")
#             if gname in shopping_cart:
#                 del shopping_cart[gname]
#                 print("删除完毕!")
#             else:
#                 print("商品不存在,请重新选择~")
#         case "4":
#
#             for gname in shopping_cart.keys():
#                 Gname = shopping_cart[gname]
#                 print(f"商品名称:{gname} 商品价格:{Gname["price"]} 商品数量:{Gname["num"]}")
#         case "5":
#             print("退出购物车系统")
#             break
#         case _:
#             print("非法操作,请重新输入!")







#练习:开发一个教务管理系统
"""
开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下:
1.添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
2.修改学生信息:要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
3.删除学生信息:要求输入要删除的学生姓名，根据姓名删除学生信息。
4.查询学生信息:要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
5.列出所有学生:遍历所有学生信息并输出。
6.统计班级成绩:统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学
员姓名。
7.退出系统。
"""
Students = {}

while True:
    menu = """
    ********************************
    *         1.添加学生信息         *
    *         2.修改学生信息         *
    *         3.删除学生信息         *
    *         4.查询学生信息         *
    *         5.列出所有学生         *
    *         6.统计班级成绩         *
    *         7.退出系统            *
    ********************************
    """
    print(menu)
    choice = input("请输入选项(1-7):")
    match choice:
        # 1.添加学生信息
        case "1":
            name = input("请输入学生姓名:")
            chinese = int(input("请输入语文成绩:"))
            math = int(input("请输入数学成绩:"))
            english = int(input("请输入英语成绩:"))
            if name in Students:
                print("学生信息已存在,请重新输入!")
            else:
                Students[name] = {"score_chinese": chinese, "score_math": math, "score_english": english}
                print(f"添加{name}成功!!!")
        # 2.修改学生信息
        case "2":
            name = input("请输入要修改的学生姓名:")
            if name not in Students:
                print("学生不存在,从重新输入!!")


            else:
                chinese = int(input("请输入语文成绩:"))
                math = int(input("请输入数学成绩:"))
                english = int(input("请输入英语成绩:"))
                print("修改完成!!!")
                Students[name] = {"score_chinese": chinese, "score_math": math, "score_english": english}

        # .3.删除学生信息
        case "3":
            name = input("请输入要删除的学生姓名:")
            if name not in Students:
                print("学生不存在,从重新输入!!")
            else:
                del Students[name]
                print("删除完成!!!")

        # 4.查询学生信息
        case "4":
            name = input("请输入要查询的学生姓名:")
            if name not in Students:
                print("学生不存在,从重新输入!!")
            else:
                # 注意：要从 Students 字典里通过键 name 取出成绩字典
                stu = Students[name]
                print(f"学生:{name},语文成绩:{stu['score_chinese']},数学成绩:{stu['score_math']},英语成绩:{stu['score_english']}")

        # 5.列出所有学生
        case "5":
            for name,scores in Students.items():
                print(
                    f"学生:{name},语文成绩:{scores['score_chinese']},数学成绩:{scores['score_math']},英语成绩:{scores['score_english']}")

        # 6.统计班级成绩
        case "6":
            #方法一: 列表推导式+解包y+max/min
            # if len(Students) == 0:
            #     print("当前暂无学生信息,无法统计!")
            # else:
            #     count = len(Students)
            #     #用列表推导式把成绩和姓名组合成元组(成绩,姓名)
            #     chinese_list = [(info['score_chinese'],name) for name, info  in Students.items()]
            #     math_list = [(info['score_math'],name ) for name,info  in Students.items()]
            #     english_list = [ (info['score_english'],name ) for name,info  in Students.items()]
            #     #利用max和min找出最大的元组,然后解包给变量
            #     max_c_score,max_c_name = max(chinese_list)
            #     min_c_score,min_c_name = min(chinese_list)
            #     avg_c = sum([score for score ,name in chinese_list]) / count
            #
            #     max_math_score,max_math_name = max(math_list)
            #     min_math_score,min_math_name = min(math_list)
            #     avg_math = sum([score for score,name in math_list]) / count
            #
            #     max_english_score,max_english_name = max(english_list)
            #     min_english_score,min_english_name = min(english_list)
            #     avg_english = sum([score for score,name in english_list]) / count
            #
            #     #输出结果
            #     print(f"语文最高分:{max_c_score} 学生姓名:{max_c_name} | 语文最低分:{min_c_score} 学生姓名:{min_c_name} | 平均分:{avg_c}")
            #     print(f"数学最高分:{max_math_score} 学生姓名:{max_math_name} | 数学最低分:{min_math_score} 学生姓名:{min_math_name} | 平均分:{avg_math}")
            #     print(f"英语最高分:{max_english_score} 学生姓名:{max_english_name} | 英语最低分:{min_english_score} 学生姓名:{min_english_name} | 平均分:{avg_english}")
            #方法二:循环遍历
            if not Students:
                print("暂无信息,无法统计!!")
            else:
                #初始化分数,名字
                max_chinese,max_math,max_english = 0,0,0
                min_chinese,min_math,min_english = 999999,999999,999999
                total_chinese,total_math,total_english =0,0,0
                max_chinese_name,max_math_name,max_english_name = "","",""
                min_chinese_name,min_math_name,min_english_name = "","",""
                count = len(Students)

                #遍历所有学生
                for name,scores in Students.items():
                    c = scores["score_chinese"]
                    m = scores["score_math"]
                    e = scores["score_english"]

                    total_chinese +=c
                    total_math +=m
                    total_english +=e

                    if c > max_chinese:
                        max_chinese = c
                        max_chinese_name = name
                    if c <min_chinese:
                        min_chinese = c
                        min_chinese_name = name

                    if m > max_math:
                        max_math = m
                        max_math_name =name
                    if m < min_math:
                        min_math = m
                        min_math_name =name

                    if e > max_english:
                        max_english = e
                        max_english_name =name
                    if e < min_english:
                        min_english = e
                        min_english_name =name

                avg_chinese = total_chinese/count
                avg_math = total_math/count
                avg_english = total_english/count

                print(f"语文最高分:{max_chinese} 姓名:{max_chinese_name} | 语文最低分:{min_chinese} 姓名:{min_chinese_name} | 平均分:{avg_chinese:.1f}")
                print(f"数学最高分:{max_math} 姓名:{max_math_name} | 数学最低分:{min_math} 姓名:{min_math_name} | 平均分:{avg_math:.1f }")
                print(f"英语最高分:{max_english} 姓名:{max_english_name} | 英语最低分:{min_english} 姓名:{min_english_name} | 平均分:{avg_english:.1f }")
        # 7.退出系统
        case "7":
            print("退出系统")
            print("bye~~~")
            break
        case _:
            print("非法输入,请重新选择!!!")
























