"""
案例 : 闭包入门

闭包解释:
    概述:
        内部函数 使用了外部函数的变量,这种写法称之为闭包
    格式:
        def 外部函数(形参列表):
            外部函数(局部)变量

            def 内部函数(形参列表)
                使用外部函数的变量

            return 内部函数名
    前提条件:
        1.有嵌套       外部函数嵌套内部函数
        2.有引用       内部函数使用外部函数的变量
        3.有返回       外部函数中,返回 内部函数名(对象)

细节:
    1.函数名 何函数名() 是两个概念
    前者表示函数对象,后者表示 调用函数,获取返回值

"""
#案例:1.函数名 -->是对象
def get_sum(a,b):
    return a+b

print(get_sum) #<function get_sum at 0x00000256B5BAB530> ,是对象
print(get_sum(1,2))  #调用函数,获取返回值

#函数名可以赋值给变量,这个变量就是: 函数对象
my_sum = get_sum
print(my_sum) #<function get_sum at 0x0000019FC1C4B530>
print(my_sum(1,2))  #3


#案例: 2.演示闭包写法
#需求:定义求合的闭包,外部函数有参数num1,内部函数有参数num2,调用,求解两数之和,观察结果

#1.定义外部函数
def fun_out(num1):
    #2.定义内部函数
    def fun_in(num2):
        #3.求和
        sum = num1+num2
        print(sum)
    return fun_in

#4.调用上述函数
fun_in = fun_out(4)
fun_in(5)

# fun_out(8)(9)



