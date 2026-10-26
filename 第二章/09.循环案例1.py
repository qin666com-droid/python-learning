"""需求:根据输入的用户名密码执行登录操作，具体要求如下:
1.正确的用户名和密码为admin/666888 、zhangsan/123456,taoge/888666
2.输入用户名和密码进行登录，直到登录成功，程序结束运行;如果登录失败，则继续输入用户名和密码进行登录
3.输入的用户名和密码不能为空!
4.登录成功:输出"登录成功，进入B站首页~"
5.登录失败:输出"用户名或密码错误，请重新输入!"

关键字:
    break,只能出现在循环中,表示结束,跳出循环的含义!
    (break跳出循环时,while后面的else中的代码将不会执行)
    continue:只能出现在循环中,表示中断本次循环,直接进入下一次循环

"""
# while True:
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#
#     if username == "" or password == "":
#         print("用户名或密码不能为空!!!请重新输入")
#         continue
#     if username == "qkw" and password =="00":
#         print("登录成功,欢迎进入X!")
#         break
#     elif username == "qq" and password =="66":
#         print("登录成功,欢迎进入X!")
#         break
#     elif username == "kk" and password =="22":
#         print("登录成功,欢迎进入X!")
#         break
#     elif username == "ww" and password =="11":
#         print("登录成功,欢迎进入X!")
#         break
#     else:
#         print("用户名或密码错误!!!请重新输入!")


#练习:用户名密码登录,5次登录机会,输入错误五次,不允许再操作了
# a = 5
# for i in range(a):
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     if username == "" or password == "":
#         print(f"用户名或密码不能为空!请重新输入!!")
#         continue
#     elif username == "qq" and password == "11":
#         print("登录成功!欢迎来到P!!!")
#         break
#     elif username == "kk" and password == "22":
#         print("登录成功!欢迎来到P!!!")
#         break
#     else:
#         print("用户名或密码错误!请重新输入!!!")
# 改进后
a = 5
for i in range(a):
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username == "" or password == "":
        print(f"用户名或密码不能为空!请重新输入!!还剩{a-1-i}次机会")
        continue
    elif username == "qq" and password == "11":
        print("登录成功!欢迎来到P!!!")
        break
    elif username == "kk" and password == "22":
        print("登录成功!欢迎来到P!!!")
        break
    else:
        remains = a-1-i
        if remains > 0:
            print(f"用户名或密码错误!请重新输入!!!还剩{remains}次机会")
        else:
            print("次数用尽!!账户已锁定!!!")







