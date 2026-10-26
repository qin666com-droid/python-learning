"""
案例 :多个装饰器装饰一个函数

记忆:多个装饰器装饰一个函数,是按照 由内向外的顺序进行装饰
    但,如果是用 装饰器的写法来,看到的效果是:从上到下的顺序
"""

#需求:发表评论前,需要先登录,在验证验证码,请用所学,模拟该功能
#1. 定义装饰器 ,表示:登录
def check_login(fun_name):
    #1.1定义内部函数,其格式必须和 被装饰的原函数 保持一致
    def fun_in():
        #1.2添加额外功能
        print("校验登录!")
        #1.3调用原函数
        fun_name()
    #1.4返回内部函数(对象)
    return fun_in

#2. 定义装饰器 ,表示:验证验证码
def check_verify_code(fun_name):
    #2.1定义内部函数,其格式必须和 被装饰的原函数 保持一致
    def fun_in():
        #2.2添加额外功能
        print("校验验证码!")
        #2.3调用原函数
        fun_name()
    #2.4返回内部函数(对象)
    return fun_in
#3.定义原函数
@check_login
@check_verify_code
def publish_comment():
    print("发表评论")



#4.测试
#传统方式:由内向外调用
# cc = check_verify_code(publish_comment)
# cg = check_login(cc)
# cg()


#语法糖:由外向内调用
publish_comment()











